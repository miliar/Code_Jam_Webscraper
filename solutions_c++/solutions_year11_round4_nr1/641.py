#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;
double ans;
int v[1000005];
int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);
    int tc,cases = 1;
    int x,s,r,t,n;
    int i,j;
    int a,b,w;
    scanf("%d",&tc);
    double tt;
    double anst;
    while(tc--)
    {
        scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
        ans = 0;
        for(i=1;i<=x;i++) v[i] = s;
        for(i=0;i<n;i++)
        {
            scanf("%d%d%d",&a,&b,&w);
            for(j=a+1;j<=b;j++)
            {
                v[j] = s+w;
            }
        }
        sort(v+1,v+x+1);
        anst = 0;
        tt = t;
        for(i=1;i<=x;i++)
        {
//            cout<<tt<<endl;
            if(tt>0)
            {
                if(tt>1.0/(r+v[i]-s))
                {
                    anst+=1.0/(r+v[i]-s);
                    tt -= 1.0/(r+v[i]-s);
                }
                else
                {
                    anst += tt;
                    anst += (1.0-tt*(r+v[i]-s))/v[i];
                    tt = 0;
                }
            }
            else anst += 1.0/v[i];
        }
        printf("Case #%d: %.6f\n",cases++,anst);
    }
	return 0;
}
