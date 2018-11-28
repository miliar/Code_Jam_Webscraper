#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <cctype>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

struct point
{
    double x, y;
    point()
    {
    }
    point(double xx, double yy) : x(xx), y(yy)
    {
    }
};

const int MAXP = 110;
point lpt[MAXP], upt[MAXP], pnt[MAXP];

int main()
{
    freopen("Al.in", "r", stdin);
    freopen("outa_l.txt", "w", stdout);
    int T, W, L, U, G;
    scanf("%d", &T);
    
    for(int t = 1; T--; ++t)
    {
        scanf("%d%d%d%d", &W, &L, &U, &G);
        
        for(int i = 0; i < L; i++)
            scanf("%lf%lf", &lpt[i].x, &lpt[i].y); 
        for(int i = 0; i < U; i++)
            scanf("%lf%lf", &upt[i].x, &upt[i].y);
        
        printf("Case #%d:\n", t);
        double prel = -1, tot = 0, target = 0, area;
        
        int pcnt = 0;
        //calculate for total area
        for(int i = 0; i < L; i++)
            pnt[pcnt++] = lpt[i];
        for(int i = U-1; i >= 0; i--)
            pnt[pcnt++] = upt[i];
                
        for(int i = 0; i < pcnt; i++)
            tot += pnt[i].x * pnt[(i+1)%pcnt].y - pnt[(i+1)%pcnt].x * pnt[i].y;
        tot = abs(tot);
        target = tot/G;
        //printf("%f YO %f\n", tot, target);
        
        //solution
        for(int i = 1; i < G; i++)
        {
            double low = i-1? prel : 0, up = W, mid, ans = -1;
            int cnt = 60;
            
            while(cnt--)
            {
                mid = (low+up)/2.0;
                pcnt = 0;
                                
                for(int j = 1; j < L; j++)                
                    if(prel > lpt[j-1].x && prel < lpt[j].x)
                    {
                        double a = prel-lpt[j-1].x, b = lpt[j].x-prel, paa = a/(a+b), pbb = b/(a+b);
                        pnt[pcnt++] = point(paa*lpt[j].x+pbb*lpt[j-1].x, paa*lpt[j].y+pbb*lpt[j-1].y);
                        break;
                    }
                    
                for(int j = 0; j < L; j++)
                    if(lpt[j].x >= prel && lpt[j].x <= mid)
                        pnt[pcnt++] = lpt[j];
                
                
                for(int j = 1; j < L; j++)                
                    if(mid > lpt[j-1].x && mid < lpt[j].x)
                    {                        
                        double a = mid-lpt[j-1].x, b = lpt[j].x-mid, paa = a/(a+b), pbb = b/(a+b);
                        pnt[pcnt++] = point(paa*lpt[j].x+pbb*lpt[j-1].x, paa*lpt[j].y+pbb*lpt[j-1].y);
                        break;
                    }
                    
                reverse(pnt, pnt+pcnt);
                
                for(int j = 1; j < U; j++)
                    if(prel > upt[j-1].x && prel < upt[j].x)
                    {                        
                        double a = prel-upt[j-1].x, b = upt[j].x-prel, paa = a/(a+b), pbb = b/(a+b);
                        pnt[pcnt++] = point(paa*upt[j].x+pbb*upt[j-1].x, paa*upt[j].y+pbb*upt[j-1].y);
                        break;
                    }
                
                for(int j = 0; j < U; j++)
                    if(upt[j].x >= prel && upt[j].x <= mid)
                        pnt[pcnt++] = upt[j];
                
                for(int j = 1; j < U; j++)
                    if(mid > upt[j-1].x && mid < upt[j].x)
                    {
                                 
                        double a = mid-upt[j-1].x, b = upt[j].x-mid, paa = a/(a+b), pbb = b/(a+b);
                        pnt[pcnt++] = point(paa*upt[j].x+pbb*upt[j-1].x, paa*upt[j].y+pbb*upt[j-1].y);
                        break;
                    }
                
                area = 0;
                for(int j = 0; j < pcnt; j++)
                    area += pnt[j].x * pnt[(j+1)%pcnt].y - pnt[(j+1)%pcnt].x * pnt[j].y;
                area = abs(area);
                
                //printf("HEY MAN %d %f\n", pcnt, mid);
                if(area-target < -1e-8) low = mid;
                else if(area-target > 1e-8) up = mid;
                else
                {
                    ans = mid;
                    break;
                }
            }
            
            printf("%f\n", ans);
            prel = ans;
        }
    }
    return 0;
}
