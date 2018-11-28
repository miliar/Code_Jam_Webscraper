#include <stdio.h>
#include <string>

using namespace std;

long long int ug=0;
long long int A[13][13];
char s[13];
int rec(int r,long long sum)
{
	if(r==strlen(s))
	{
		if((sum%2==0)||(sum%3==0)||(sum%5==0)||(sum%7==0)||(sum==0))
			ug++;
		return 0;
	}
	for(int i=r;i<strlen(s);i++)
	{
		sum+=A[r][i];
		rec(i+1,sum);
		sum-=2*A[r][i];
		rec(i+1,sum);
		sum+=A[r][i];
	}
	return 0;
}
		

int main()
{
	long long int ch;
	int N;
	freopen("B-small.in","r",stdin);
	freopen("out.in","w",stdout);
	scanf("%d",&N);
	for(int h=0;h<N;h++)
	{
		ug=0;
		scanf("%s",s);
		for(int i=0;i<strlen(s);i++)
		{
			for(int j=i;j<strlen(s);j++)
			{
				ch=0;
				for(int z=i;z<=j;z++)
				{
					ch*=10;
					ch+=(s[z]-'0');
				}
				A[i][j]=ch;
			}
		}
		rec(0,0);
		printf("Case #%d: %ld\n",h+1,ug/2);
	}		
				
	return 0;
}
