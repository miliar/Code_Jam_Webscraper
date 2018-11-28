#include <fstream>
using namespace std;

unsigned int clip(int x)
{
    return max(0, x);
}


int main()
{
    const char ifname[] = "A-large.in";
    const char ofname[] = "A-large.out";
    ifstream inf(ifname);
    ofstream ouf(ofname);

    int T, t;
    int N, i;
    int P;
    char robot, prev_robot;

    long posO, posB;
    long time;
    long robot_time;
    long diff, need;

    long buffer_time;

    inf >> T;

    for (t = 0; t < T; t++)
    {
        inf >> N;

        posO = 1;
        posB = 1;

        time = 0;
        robot_time = 0;
        buffer_time = 0;
        for (i = 0; i < N; i++)
        {
            inf >> robot;
            inf >> P;

            if (i == 0) prev_robot = robot;

            if (robot != prev_robot) {
                time += robot_time;
                buffer_time = robot_time;
                robot_time = 0;
                prev_robot = robot;
            } else  {
                buffer_time = 0;
            }

            switch (robot) {
                case 'O':
                    diff = abs(P - posO);
                    need = clip(diff - buffer_time);
                    robot_time += need + 1;
                    posO = P;
                    break;
                case 'B':
                    diff = abs(P - posB);
                    need = clip(diff - buffer_time);
                    robot_time += need + 1;
                    posB = P;
            }
        }
        time += robot_time;
        ouf << "Case #" << t + 1 << ": " << time << endl;
    }
    
    inf.close();
    ouf.close();
    return 0;
}
