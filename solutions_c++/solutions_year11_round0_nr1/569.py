#include <queue>
#include <cstdlib>
#include <cassert>
#include <fstream>
using namespace std;

class Robot {
    int m_currentPosition;
    int m_seconds;
    queue<int> m_positions;
public:
    Robot() : m_currentPosition(1), m_seconds(0) {
    }

    void pushOrder(int position) {
        m_positions.push(position);
    }

    void pushButton() {
        gotoNext();
        ++m_seconds;
        m_positions.pop();
    }

    void prepare(int seconds) {
        if (m_positions.empty())
            return;

        moveToNext(seconds);
    }

    int totalSeconds() const {
        return m_seconds;
    }

private:
    void moveToNext(int seconds) {
        int nextPosition = m_positions.front();
        int delta = nextPosition - m_currentPosition > 0 ? 1 : -1;

        for (int i = 0; i < seconds; ++i) {
            if (nextPosition == m_currentPosition)
                break;
            m_currentPosition += delta;
        }
    }

    void gotoNext() {
        int distance = abs(m_currentPosition - m_positions.front());
        m_seconds = distance;
        m_currentPosition = m_positions.front();
    }
};

class RobotsManager {
    int m_buttons;
    Robot m_orange, m_blue;
    vector<char> m_nextRobots;
    int m_seconds;
public:
    RobotsManager(int buttons) : m_buttons(buttons), m_seconds(0) {
    }

    void nextButton(char robot, int button) {
        m_nextRobots.push_back(robot);
        if (robot == 'O')
            m_orange.pushOrder(button);
        else if (robot == 'B')
            m_blue.pushOrder(button);
        else
            assert(false);
    }

    void execute() {
        for (int i = 0; i < m_nextRobots.size(); ++i) {
            char robot = m_nextRobots[i];
            if (robot == 'O') {
                m_orange.pushButton();
                m_blue.prepare(m_orange.totalSeconds());
                m_seconds += m_orange.totalSeconds();
            }
            else if (robot == 'B') {
                m_blue.pushButton();
                m_orange.prepare(m_blue.totalSeconds());
                m_seconds += m_blue.totalSeconds();
            }
            else
                assert(false);
        }
    }

    int totalSeconds() const {
        return m_seconds;
    }
};

void execute(istream& in, ostream& out) {
    int T, N;
    in >> T;
    for (int i = 0; i < T; ++i) {
        in >> N;
        RobotsManager m(N);
        for (int j = 0; j < N; ++j) {
            char robotType;
            int buttonNumber;
            in >> robotType >> buttonNumber;
            m.nextButton(robotType, buttonNumber);
        }
        m.execute();
        out << "Case #" << (i+1) << ": " << m.totalSeconds() << endl;
    }
}

int main(int argc, char** argv) {
  ifstream ifs(argv[1], ifstream::in);
  ofstream ofs(argv[2], ofstream::out);
  execute(ifs, ofs);
  return 0;
}
