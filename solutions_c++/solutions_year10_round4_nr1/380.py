#include <iostream>
#include <math.h>
using namespace std;
const int maxint = -1u>>1;
int map[200][200];
int k;
bool check(int x,int y)
{
	int i,j,a,b;
	for(i=1;i<=k;i++)
	{
		for(j=k+1-i;j<=k+i-1;j+=2)
		{
			a=2*x-i;
			b=2*y-j;
			if(a>=1 && a<=2*k-1 && b>=1 && b<=2*k-1 && map[a][b]!=-1 && map[a][b]!=map[i][j])
			{
				return false;
			}
			a=2*x-i;
			b=j;
			if(a>=1 && a<=2*k-1 && b>=1 && b<=2*k-1 && map[a][b]!=-1 && map[a][b]!=map[i][j])
			{
				return false;
			}
			a=i;
			b=2*y-j;
			if(a>=1 && a<=2*k-1 && b>=1 && b<=2*k-1 && map[a][b]!=-1 && map[a][b]!=map[i][j])
			{
				return false;
			}
		}
	}
	for(i=k-1;i>=1;i--)
	{
		for(j=k+1-i;j<=k+i-1;j+=2)
		{
			a=2*x-(2*k-i);
			b=2*y-j;
			if(a>=1 && a<=2*k-1 && b>=1 && b<=2*k-1 && map[a][b]!=-1 && map[a][b]!=map[2*k-i][j])
			{
				return false;
			}
			a=a=2*x-(2*k-i);
			b=j;
			if(a>=1 && a<=2*k-1 && b>=1 && b<=2*k-1 && map[a][b]!=-1 && map[a][b]!=map[2*k-i][j])
			{
				return false;
			}
			a=2*k-i;
			b=2*y-j;
			if(a>=1 && a<=2*k-1 && b>=1 && b<=2*k-1 && map[a][b]!=-1 && map[a][b]!=map[2*k-i][j])
			{
				return false;
			}

		}
	}
	return true;
}
int get(int x,int y)
{
	int ans;
	ans=abs(x-k)+abs(y-k)+k;
	return ans*ans-k*k;
}
	
	
			
int main()
{
	freopen("out.txt","w",stdout);
	int t,i,j,x,y,ca=0;
	cin>>t;
	bool find;
	int mm,rem;
	while(t--)
	{
		cin>>k;
		for(i=1;i<=2*k-1;i++)
		{
			for(j=1;j<=2*k-1;j++)
			{
				map[i][j]=-1;
			}
		}
		for(i=1;i<=k;i++)
		{
			for(j=k+1-i;j<=k+i-1;j+=2)
			{
				cin>>map[i][j];
			}
		}
		for(i=k-1;i>=1;i--)
		{
			for(j=k+1-i;j<=k+i-1;j+=2)
			{
				cin>>map[2*k-i][j];
			}
		}
		find=0;
		for(i=0;i<k;i++)
		{
			mm=maxint;
			for(j=k-i;j<=k+i;j++)
			{
				x=k-i;
				y=j;
				if(check(x,y))
				{
					find=1;
					rem=get(x,y);
					if(rem<mm)
						mm=rem;
				}
				x=k+i;
				y=j;
				if(check(x,y))
				{
					find=1;
					rem=get(x,y);
					if(rem<mm)
						mm=rem;
				}
				x=j;
				y=k-i;
				if(check(x,y))
				{
					find=1;
					rem=get(x,y);
					if(rem<mm)
						mm=rem;
				}
				x=j;
				y=k+i;
				if(check(x,y))
				{
					find=1;
					rem=get(x,y);
					if(rem<mm)
						mm=rem;
				}
			}
			if(find==1)
			{
				break;
			}


		}
		printf("Case #%d: %d\n",++ca,mm);
	}
	return 0;
}
