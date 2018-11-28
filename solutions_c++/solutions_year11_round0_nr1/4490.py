#include <stdio.h>
#include <vector>

using namespace std;


vector <int> p1,p2,t1,t2;


int t,o,k,a;
char ch;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    scanf("%d",&t);
    
    for (int i = 1; i <= t; i++)
    {
        scanf("%d ",&o);
        p1.clear(); t1.clear();
        p2.clear(); t2.clear();
        
        for (k=0; k<o; k++)
        {
            scanf("%c %d ",&ch,&a);
            if (ch=='O') { p1.push_back(a); t1.push_back(k); } else
                         { p2.push_back(a); t2.push_back(k); }    
        }
        
        int pt1, pt2, step, c1, c2;
        pt1 = pt2 = step = 0;
        c1 = c2 = 1;
        
        while (pt1 < p1.size() || pt2 < p2.size())
        {
             if (pt1 >= p1.size())
             {
               if (p2[ pt2 ] < c2) c2--; else
               if (p2[ pt2 ] > c2) c2++; else
               pt2++;
             } else
             if (pt2 >= p2.size())
             {
                       if (p1[ pt1 ] < c1) c1--; else
               if (p1[ pt1 ] > c1) c1++; else
               pt1++;
               
             } else
             if ( t1[pt1] < t2[pt2])
             {
               if (p1[ pt1 ] < c1) c1--; else
               if (p1[ pt1 ] > c1) c1++; else
               pt1++;
               
               if (p2[ pt2 ] < c2) c2--; else
               if (p2[ pt2 ] > c2) c2++;
             } 
             else
             {
               if (p2[ pt2 ] < c2) c2--; else
               if (p2[ pt2 ] > c2) c2++; else
               pt2++;
               
               if (p1[ pt1 ] < c1) c1--; else
               if (p1[ pt1 ] > c1) c1++;
             }
             step++;
        }
        
        printf("Case #%d: %d\n",i, step);
    }
    
    

    return 0;
}
