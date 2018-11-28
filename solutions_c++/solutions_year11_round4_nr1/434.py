#include <iostream>
#include <fstream>
#include <cstring>
#include <climits>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <climits>
#include <algorithm>



using namespace std;

const double EPS = 1e-9;

typedef pair<double , double> pii;

int X,N;
double t;
double S, R;

pii speed[1100000];

//double array[110][3];


bool cmp(pii a, pii b)
{
    return a.second < b.second;
}



int main()
{
    freopen("A-large (3).in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T;
    scanf("%d ", &T);
    double B,E,W;

    for(int loop = 1; loop <= T; loop++)
    {
        scanf("%d %lf %lf %lf %d", &X, &S, &R, &t, &N);

        double sum = 0;
        for(int i = 0; i < N; i++)
        {
            scanf("%lf %lf %lf", &B, &E, &W);
//            printf("%lf %lf %lf\n", B, E, W);
            speed[i].first = E- B;
            speed[i].second = W;
            sum += speed[i].first;
        }
        double x = double(X);
        if(x - sum > 0)
        {
            speed[N].first = x - sum;
            speed[N].second = 0;
            N++;
        }

        double res = 0;
        sort(speed, speed + N, cmp);
//        for(int i = 0; i < N; i++)
//        {
//            printf("%lf %lf\n", speed[i].first, speed[i].second);
//        }

        for(int i = 0; i < N; i++)
        {
            if(t < EPS)
            {
                res += (speed[i].first) / (speed[i].second + S);
                continue;
            }
            if((speed[i].second + R) * t > speed[i].first)
            {
                res += (speed[i].first) / (speed[i].second + R);
                t -=  (speed[i].first) / (speed[i].second + R);
            }
            else
            {
                res += t;
                speed[i].first -= t * ((speed[i].second + R));
                t = 0;
//                printf("...%lf\n", speed[i].first);
//                printf("res %lf\n", res);
                res += speed[i].first / (speed[i].second + S);
            }
        }

        printf("Case #%d: %0.10lf\n", loop, res);




    }
















    return 0;
}
