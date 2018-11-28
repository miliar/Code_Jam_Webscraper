#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int v[1000000],c,d,p,n,k;

int check(double ans)
{
	double x = v[0]-ans;
	for(int i=1;i<k;i++){
		if (x+d>v[i]+ans) return 0;
		x=max(v[i]-ans,x+d);
	}
	return 1;
}
int main()
{
    int t,T,i,j;

    freopen("B-small-attempt0.in","r",stdin);
   freopen("output.txt","w",stdout);   
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%d",&c,&d);
        for(i=0,k=0;i<c;i++)
        {
            scanf("%d%d",&p,&n);
            for(j=0;j<n;j++)
                v[k++]=p;
            //cout<<"ok";
        }
        sort(v,v+k);
        double u=1e+12,l=0.0,mid;
        while(fabs(u-l)>1e-9)
        {
            mid=(l+u)/2.0;
            if(check(mid)) u=mid;
            else l=mid;
        }
        printf("Case #%d: %.9f\n",t,u);
    }
//system("pause");

    return 0;
}
