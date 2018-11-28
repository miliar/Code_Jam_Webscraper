#include<fstream>
#include<iostream>
#include<vector>
#include<algorithm>
#include<iomanip>
//#include<stdlib.h>
//#include<math.h>


using namespace std;

ifstream in("A-large.in");
ofstream out("output.txt");

int T;

int main()
{
    in >> T;
    for(int test = 0; test < T; test++)
    {
        double answer = 0;
        double X, S, R, t;
        int N;
        in >> X >> S >> R >> t >> N;
        vector<double> speeds(101, 0);
        double noway = X;

        for(int i = 0; i < N; i++)
        {
            int a, b, w;
            in >> a >> b >> w;
            noway -= double(b - a);
            speeds[w] += double(b - a);
        }
        speeds[0] = noway;
        for(int i = 0; i <= 100; i++)
        {
            if(t > 0)
            {
                double need_t = speeds[i]/double(i + R);
                if(need_t > t)
                    need_t = t + (speeds[i] - double(i + R)*t)/double(i + S);
                answer += need_t;
                t -= need_t;
            }
            else
                answer += speeds[i]/double(i + S);
        }
        out << "Case #" << test + 1 << ": " << setprecision(8) << fixed << answer << endl;
    }
    return 0;
}
