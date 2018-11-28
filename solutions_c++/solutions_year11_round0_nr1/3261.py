#include<fstream>
#include<iostream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int T, N;

int main()
{
    in >> T;
    for(int t = 0; t < T; t++)
    {
        int answer = 0;
        in >> N;
        vector<int> orange(N + 1, -1);
        vector<int> blue(N + 1, -1);
        int orange_pos = 1, blue_pos = 1;
        for(int i = 0; i < N; i++)
        {
            string robot;
            int button;
            in >> robot >> button;
            if(robot == "O")
                orange[i] = button;
            else
                blue[i] = button;
        }
        for(int i = 0; i < N; i++)
        {
            if(orange[i] > 0)
            {
                int steps = abs(orange_pos - orange[i]) + 1;
                orange_pos = orange[i];
                int p;
                for(p = i + 1; p <= N; p++)
                    if(blue[p] > 0)
                        break;
                if(blue[p] > blue_pos)
                    blue_pos = min(blue[p], blue_pos + steps);
                else
                    blue_pos = max(blue[p], blue_pos - steps);
                answer += steps;
            }
            else
            {
                int steps = abs(blue_pos - blue[i]) + 1;
                blue_pos = blue[i];
                int p;
                for(p = i + 1; p <= N; p++)
                    if(orange[p] > 0)
                        break;
                if(orange[p] > orange_pos)
                    orange_pos = min(orange[p], orange_pos + steps);
                else
                    orange_pos = max(orange[p], orange_pos - steps);
                answer += steps;
            }
        }
        out << "Case #" << t + 1 << ": " << answer << endl;
    }
    return 0;
}
