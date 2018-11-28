#include <list>
#include<vector>
#include <sstream>
#include <ioStream>
#include <cmath>

enum RobotName{
    Orange,
    Blue
};

class Goals{
public:
    struct GoalData{
        RobotName robot;
        int button;
    };
    static const int END = -1;
    void addGoals(std::string goal);
    int size();
    GoalData getNextGoal();

private:
    std::list<GoalData> goals;
};

int Goals::size(){
    return goals.size();
}

Goals::GoalData Goals::getNextGoal(){
    GoalData data= goals.front();
    goals.pop_front();
    return data;
}

void Goals::addGoals(std::string goalstr){
    std::istringstream stream(goalstr);
    int size;
    char robchar;
    int button;
    stream >> size;
    for( int i=0; i<size; i++){
        stream >> robchar;
        stream >> button;

        GoalData goal;
        if( robchar == 'O' ){
            goal.robot = Orange;
        }else{
            goal.robot = Blue;
        }
        goal.button = button;
        goals.push_back(goal);
    }
}



class Robot{
    RobotName me;
    int position;
    int time;

public:
    Robot(RobotName me);
    int push(int button);
    void addTime( int seconds );
};

Robot::Robot(RobotName me): me(me), position(1), time(0){
}

int Robot::push(int button){
    int timeToPush = abs(button - position);
    timeToPush = timeToPush > time? timeToPush - time : 0;
    time = 0;
    position = button;
    return timeToPush + 1;
}

void Robot::addTime(int seconds){
    time += seconds;
}


int main(int argc, char *argv[])
{
    int NTest;
    std::cin >> NTest;
    int test;
    std::string line;
    std::getline(std::cin, line);
    for ( test = 1 ; test <= NTest; test++){
        std::getline(std::cin, line);
        Goals goals;
        // primero carga goals
        goals.addGoals(line);

        Robot orange(Orange);
        Robot blue(Blue);

        int size = goals.size();
        int total=0;
        int movement;

        for( int i=0 ; i < size ; i++){
            Goals::GoalData nextGoal = goals.getNextGoal();
            if( nextGoal.robot == Orange){
                movement = orange.push(nextGoal.button);
                blue.addTime(movement);
            }else{
                movement = blue.push(nextGoal.button);
                orange.addTime(movement);
            }
            total += movement;
        }
        std::cout << "Case #" << test << ": " << total << std::endl;
    }

    return 1;
}
