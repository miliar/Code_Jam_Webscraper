#include <iostream>

using namespace std;

int n,m;
char c[100][100];

bool check()
{
	scanf("%d %d\n",&n,&m);
	for (int i=0;i<n;i++) gets(c[i]);
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
		if (c[i][j]=='#')
		{
			if((j+1<m)&& (i+1<n) && (c[i][j+1]=='#') && ( c[i+1][j]=='#') && ( c[i+1][j+1]=='#'))
			{
				c[i][j]=c[i+1][j+1]='/';
				c[i][j+1]=c[i+1][j]='\\';
			}
			else return false;
		}
	return true;
}


int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int casenum;
	scanf("%d\n",&casenum);
	for (int cc=1;cc<=casenum;cc++)
	{
		printf("Case #%d:\n",cc);
		if (check()) 
		{
			for (int i=0;i<n;i++)
			{
   				puts(c[i]);
   				cout <<endl;
			}	
		}
		else printf("Impossible\n");
	}
}
