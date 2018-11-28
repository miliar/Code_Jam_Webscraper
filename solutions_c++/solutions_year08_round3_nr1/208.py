#include<iostream>
#include<algorithm>
using namespace std;
int test;
int p,k,l;
int bet[101];
int a[15][15];
int total;
bool __inline cmp(int x,int y)
{
if (x>y) return true;
else return false;
}


int main()
{
int i,j,flag,jj,ii;
freopen("A-small.in.txt","r",stdin);
freopen("1.out","w",stdout);
cin>>test;
for(ii=1;ii<=test;ii++)
{
total=0;
cin>>p>>k>>l;
for(i=1;i<=l;i++) cin>>bet[i];
sort(bet+1,bet+l+1,cmp);
for(i=1;i<=k;i++)
 for(j=1;j<=p;j++)
	 a[i][j]=0;
 for(i=1;i<=l;i++)
 {
     flag=0;
	 for(j=1;j<=p;j++)
	{
	   for(jj=1;jj<=k;jj++)
		   if (a[jj][j]==0) 
		   {
			   
			   a[jj][j]=bet[i];
		       flag=1;
			   total+=bet[i]*j;
			   break;
		   }
	    if (flag) break;
	 }
}
printf("Case #%d: ",ii);
printf("%d\n",total);
}
return 0;
}