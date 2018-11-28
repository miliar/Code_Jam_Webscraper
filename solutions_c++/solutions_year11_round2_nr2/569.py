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

#define inputfilename "a.in"
#define outputfilename "a.out"

using namespace std;

int d, c;
int a[1000][2];

int main ()
{
    //freopen(inputfilename , "r" , stdin);
	//freopen(outputfilename , "w" , stdout);
    
    int number, times;
    cin >> number;
    for (times = 0; times < number; times++)
    {
        int i, j;
        cin >> c >> d;
        for (i = 0; i < c; i++)
        {
            cin >> a[i][0] >> a[i][1];//P and V
        }
        double b= 0, e = 1e15, mid;
        double res = e;
        while (b < e)
        {
            if (fabs(e - b) < 1e-6)
            {
                break;
            }
            mid = (b + e) / 2;
            if (mid < 1.5  && mid > 1)
            {
                int x;
                x = 3;
            }
            double left;
            bool flag = true;
            for (i = 0 ; i < c; i++)
            {
                for (j = 0; j < a[i][1]; j++)
                {
                    if (i == 0 && j == 0)
                    {
                        left = a[i][0] - mid;
                    }
                    else
                    {
                        double pos = left + d;
                        double dis = fabs(pos - a[i][0]);
                        if (dis > mid)
                        {
                            if (pos < a[i][0])
                            {
                                left = a[i][0] - mid;
                            }
                            else
                            {
                                flag = false;
                                break;
                            }
                        }
                        else
                        {
                            left = pos;
                        }
                    }
                }
                if (flag == false)
                {
                    break;
                }
            }
            if (flag)
            {
                res = min(res, mid);
                e = mid;
            }
            else
            {
                b = mid;
            }
        }
        cout <<"Case #"<< times+1<<": ";
        cout << res << endl;
    }



	return 0;
}

 
