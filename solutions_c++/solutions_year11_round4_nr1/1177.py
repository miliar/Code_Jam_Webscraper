#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <set>

using namespace std;


class Interval
{
    public : int x;
             int y;
             int v;
};

bool cmp(Interval a, Interval b)
{
    return a.x < b.x;
}

int n,i,p,l,k,t,x,s,R,r;
double T;

Interval m[2000000], M[2000000];

int main()
{
    
    
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
    scanf("%d",&t);
    for (i = 1; i <= t; i++)
    {
        cin>>x>>s>>R>>T>>n;
        for (l=0; l<n; l++) scanf("%d%d%d",&m[l].x, &m[l].y, &m[l].v);
        printf("Case #%d: ",i);
        
        int speed, beg = 0;
        sort(m,m+n,cmp);
        
        r = 0;
        for (l=0; l<n; l++)
        {
            if (m[l].x>beg) { M[r].x = 0; M[r++].y = m[l].x - beg; }
            M[r].x = m[l].v; M[r++].y = m[l].y - m[l].x;
            beg = m[l].y;
        }
        M[r].x =0;
        M[r++].y =  x - beg;
        
        sort(M,M + r,cmp);
               
       double ans = 0., curt = 0, curs = 0;
       for (l=0; l<r; l++)
       {

            speed = M[l].x + R;
            if (T < 0.0000001) 
            {
                speed -= R - s;
                ans += (double) (M[l].y) / speed;
            }
            else
            {
            
                curt = (double) (M[l].y) / speed;
                if (curt > T)
                {
                    curs = 1.0 * M[l].y - T * speed;
                    ans += T + curs / (1.*(speed - R + s));
                    T = 0;
                }   
                else
                {
                 T -= curt;
                ans += curt;
               }
            }
       }      
       
       printf("%.7f\n", ans);
    }
    
    return 0;
}
