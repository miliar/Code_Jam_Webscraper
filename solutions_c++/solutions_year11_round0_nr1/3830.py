#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int tests(0);
    fin >> tests;
    for (int test = 1; test <= tests; test++)
    {
        int n(0);
        fin >> n;
        int time = 0;
        int robot_time[2] = {0, 0};
        int robot_pos[2] = {1, 1};
        while (n-- > 0)
        {
            char robot('\0');
            int button(0);
            fin >> robot >> button;
            int index = (robot == 'O') ? 0 : 1;
            int steps = abs(robot_pos[index] - button);
            if (robot_time[index] + steps > time)
            {
                time = robot_time[index] + steps;
            }
            robot_pos[index] = button;
            robot_time[index] = ++time;
        }
        fout << "Case #" << test << ": " << time << endl;
    }
    return 0;
}