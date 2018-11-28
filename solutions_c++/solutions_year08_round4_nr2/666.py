#include<iostream>
#include<cmath>
#include<math.h>
using namespace std;

int main(){
    freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\in.txt","r",stdin);
	freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\out.txt","w",stdout);
	int i, j, k, r, s, t, n, m, a;
	scanf("%d",&t);
	for(i=1; i<=t; i++)
	{
         scanf("%d%d%d",&n,&m,&a);
         printf("Case #%d: ",i);
         for(j=0; j<=n; j++)
         {
             for(k=0; k<=m; k++)
             {
                 for(r=0; r<=n; r++)
                 {
                     for(s=0; s<=m; s++)
                     {
                         double d = sqrt((double)(r*r+s*s));
                         double b = sqrt((double)(j*j+k*k));
                         double c = sqrt((double)((r-j)*(r-j)+(s-k)*(s-k)));
                         double p = (d+b+c)/2;
                         double area = sqrt(p*(p-d)*(p-b)*(p-c));
                         //if(j==1&&k==0&&r==1&&s==1) cout<<area<<endl;
                         if( fabs(2*area-a) < 1e-6) break;
                     }
                     if(s<=m) break;
                 }
                 if(r<=n) break;
             }
             if(k<=m) break;
         }
         if(j>n) printf("IMPOSSIBLE\n");
         else printf("0 0 %d %d %d %d\n",j,k,r,s);
     }
                     
    return 0;
}
