#include <cstdio>
#include <string>

using namespace std;

int pr()
{
    char fr[510];
    int ans[510][19];
    string c="welcome to code jam";
    int i=0, j, n;
    if(fr[0]=='\n')
    {
	   printf("#####");
    }
    i=-1;
    do
    {
	   i++;
	   scanf("%c",&fr[i]);
    }while(fr[i]!='\n');
    n=i;
    for(i=0; i<n; i++)
    {
	   for(j=0; j<19; j++)
	   {
		  ans[i][j]=0;
	   }
    }
    if(fr[n-1]=='m')
    {
	   ans[n-1][18]=1;
    }
    for(i=n-2; i>-1; i--)
    {
	   for(j=0; j<19; j++)
	   {
		  ans[i][j]=ans[i+1][j];
	   }
	   if(fr[i]=='m')
	   {
		  ans[i][18]=(ans[i][18]+1)%1000;
	   }
	   for(j=0; j<18; j++)
	   {
		  if(fr[i]==c[j])
		  {
			 ans[i][j]=(ans[i][j]+ans[i][j+1])%1000;
		  }
	   }
    }
    return ans[0][0];
}

int main()
{
    freopen("cosa.in","r",stdin);
    freopen("cosa.txt","w",stdout);
    int i, n, j;
    scanf("%d",&n);
    char w;
    scanf("%c",&w);
    for(i=1; i<=n; i++)
    {
	   j=pr();
	   printf("Case #%d: ",i);
	   if(j<1000)
	   {
		  printf("0");
	   }
	   if(j<100)
	   {
		  printf("0");
	   }
	   if(j<10)
	   {
		  printf("0");
	   }
	   printf("%d\n",j);
    }
    return 0;
}