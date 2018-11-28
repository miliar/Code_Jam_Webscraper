#include <iostream>
#include <cmath>
using namespace std;

const int N = 110;
int n;
char col[N][2];
int stp[N];
int ans;

int main()
{
	//freopen("F:\\DownLoad\\A-large.in","r",stdin);
	//freopen("F:\\A-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for ( int c = 1; c <= t; c++ )
	{
		ans = 0;
		scanf("%d",&n);
		for ( int i = 0; i < n; i++ )
		{
			scanf("%s",&col[i]);
			scanf("%d",&stp[i]);
		}
		int t1=0,t2=0;
		int loc1=1,loc2=1;
		int flag;
		
		if ( col[0][0]=='O' )
		{
			flag = 0;
			t1 = abs(stp[0] - loc1) + 1;
			loc1 = stp[0];
			ans += t1;
		}
		else
		{
			flag = 1;
			t2 = abs(stp[0] - loc2) + 1;
			loc2 = stp[0];
			ans += t2;
		}
		for ( int i = 1; i < n; i++ )
		{
			if ( col[i][0]=='O' )
			{
				if ( flag==0 )
				{
					t1 += abs(stp[i] - loc1) + 1;
					ans += (abs(stp[i] - loc1) + 1);
				}
				else
				{
					t1 = abs(stp[i] - loc1);
					if ( t1>t2 )
						t1 = t1 - t2 + 1;
					else
						t1 = 1;
					ans += t1;
				}
				flag = 0;
				loc1 = stp[i];
				
			}
			else
			{
				if ( flag==1 )
				{
					t2 += abs(stp[i] - loc2) + 1;
					ans += (abs(stp[i] - loc2) + 1); 
				}
				else
				{
					t2 = abs(stp[i] - loc2);
					if ( t2>t1 )
						t2 = t2 - t1 + 1;
					else
						t2 = 1;
					ans += t2;
				}
				flag = 1;
				loc2 = stp[i];
				
			}
		}
		printf("Case #%d: %d\n",c,ans);
	}
}