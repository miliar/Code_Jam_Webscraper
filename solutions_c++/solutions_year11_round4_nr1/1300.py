#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <ctime>
#include <string>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>
#include <algorithm>

#define inputfilename "a.in"
#define outputfilename "a.out"

using namespace std;

int s, r;
int n;
double t;
double x;
struct node
{
    int b, e, w;
}a[1010];

bool operator<(const node &a, const node&b)
{
    return a.w < b.w;
}

int main ()
{
    //freopen(inputfilename , "r" , stdin);
	//freopen(outputfilename , "w" , stdout);
    
    int number, times;
    cin >> number;
    for (times = 0; times < number; times++)
    {
        cin >> x >> s >> r >> t >> n;
        int i;
         //if (times == 10)
        //{
            //cout <<"..." << x <<" "<< s <<" " << r <<endl;
        //}

        for (i = 0; i < n; i++)
        {
            cin >> a[i].b >> a[i].e >> a[i].w;
            x -= (a[i].e - a[i].b);
        }
        sort(a, a + n);
        double res = 0;
        
       
        if (t > 0)
        {
            double t0 = x / (r);
            if (t0 <= t)
            {
                res += t0;
                t -= t0;
            }
            else
            {
                res += t + (x - (r) * t)/s;
                t = 0;
            }
        }
        else
        {
            res += x / s;
        }



        for (i = 0 ; i < n; i++)
        {
            double d = a[i].e-a[i].b;
            if (t <= 0)
            {
                res += d/(s+a[i].w);
            }
            else
            {
                double t0 = d / (a[i].w + r);
                if (t0 <= t)
                {
                    res += t0;
                    t -= t0;
                }
                else
                {
                    res += t + (d - (a[i].w + r) * t)/(s+a[i].w);
                    t = 0;
                }
            }
            x -= d;
        }
        printf("Case #%d: %.6lf\n", times+1, res);
    }


	return 0;
}

 
