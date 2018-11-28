#include <deque>
#include <iostream>
#include <queue>
#include <string>

// Using boost version 1.45.0 from
// http://www.boost.org/users/history/
#include <boost/lexical_cast.hpp>

// Using google-gflags version 1.5 from
// http://code.google.com/p/google-gflags/
#include <gflags/gflags.h>

// Using google-glog version 0.3.1-1 from
// http://code.google.com/p/google-glog/
#include <glog/logging.h>

#include "input.hpp"

class Robot {
public:
    // Reset the static members before each test case
    static void initialize();

    // Increment the global sequence if one of the robots
    // pushed a button
    static void increment_seq();

    Robot(const std::string& color);

    // Tell the robot to push a button at a certain sequence
    void add_button(int seq, int button);

    // Determine if the robot is done pushing all of its buttons
    bool done();

    // Execute a step
    void step();

    friend std::ostream& operator<<(std::ostream& os, const Robot& r);
private:
    static bool increment_seq_;
    static int global_seq_;
    std::string color_;
    int current_position_;
    std::queue<std::pair<int, int> > buttons_;
};

bool Robot::increment_seq_ = false;
int Robot::global_seq_ = 1;

std::ostream& operator<<(std::ostream& os, const Robot& r)
{
    os << "Robot(" << r.color_ << ")";
    return os;
}

void Robot::initialize()
{
    increment_seq_ = false;
    global_seq_ = 1;
}

void Robot::increment_seq()
{
    if (increment_seq_) {
        ++global_seq_;
        increment_seq_ = false;
    }
}

Robot::Robot(const std::string& color):
    color_(color),
    current_position_(1),
    buttons_()
{
}

void Robot::add_button(int seq, int position)
{
    LOG(INFO) << *this << " should push button at " << position << " at sequence " << seq;
    buttons_.push(std::make_pair(seq, position));
}

bool Robot::done()
{
    return buttons_.empty();
}

void Robot::step()
{
    std::pair<int, int> instruction = buttons_.front();
    int seq = instruction.first;
    int button = instruction.second;
    LOG(INFO) << *this << " is currently at " << current_position_;
    LOG(INFO) << *this << " is trying to get to button " << button;
    if (global_seq_ == seq && current_position_ == button) {
        LOG(INFO) << *this << " is pushing button " << button;
        buttons_.pop();
        increment_seq_ = true;
    } else {
        if (current_position_ == button) {
            LOG(INFO) << *this << " is waiting at " << button;
        } else {
            if (current_position_ > button) {
                LOG(INFO) << *this << " is moving backward";
                --current_position_;
            } else {
                LOG(INFO) << *this << "is moving forward";
                ++current_position_;
            }
        }
    }
}

int code_jam_main(int argc, char ** argv, int test_case)
{
    Robot::initialize();
    std::deque<std::string> instructions;
    input::read<std::deque<std::string>, std::string>(&instructions);
    int number_of_button_pushes = boost::lexical_cast<int>(instructions.front());
    instructions.pop_front();
    LOG(INFO) << "Number of button pushes: " << number_of_button_pushes;
    Robot orange("orange");
    Robot blue("blue");
    for (int i = 1; i <= number_of_button_pushes; ++i) {
        std::string color = instructions.front();
        instructions.pop_front();
        int button = boost::lexical_cast<int>(instructions.front());
        instructions.pop_front();
        if (color == "O") {
            orange.add_button(i, button);
        } else {
            blue.add_button(i, button);
        }
    }
    int step = 0;
    while (! orange.done() || ! blue.done()) {
        ++step;
        LOG(INFO) << "Step: " << step;
        if (! orange.done()) {
            orange.step();
        }
        if (! blue.done()) {
            blue.step();
        }
        Robot::increment_seq();
    }
    LOG(INFO) << "Done at step " << step;
    std::cout << "Case #" << test_case << ": " << step << std::endl;
    return 0;
}
