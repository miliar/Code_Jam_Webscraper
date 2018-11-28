#include <iostream>
#include <stdio.h>

using namespace std;

#define abs(a) (((a) > 0) ? (a) : -(a))
int n, t, bp, op, p, bl, ol;
int tc;
char c;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin>>tc;
    for(int test = 1; test <= tc; test++)
    {
        t = bl = ol = 0;
        bp = op = 1;
        cin>>n;
        for(int i = 0; i < n; i++)
        {
            cin>>c>>p;
            if(c == 'O')
            {
                if(t - ol < abs(op - p))
                {
                    int dt = abs(op - p) - (t - ol);
                    t += dt;
                }    
                t += 1;
                op = p;
                ol = t;
            }
            else
            {
                if(t - bl < abs(bp - p))
                {
                    int dt = abs(bp - p) - (t - bl);
                    t += dt;
                }
                t += 1;
                bp = p;
                bl = t;

            }
        }
        cout<<"Case #"<<test<<": "<<t<<endl;
    }
    return 0;
}