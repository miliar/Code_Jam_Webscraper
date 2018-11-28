#include "../common.h"

using namespace std;
int R,C;
char a[55][55];
char b[55][55];
int main()
{
	FILE *fp = NULL;
	fp = freopen("A-large.in","r",stdin);
	fp = freopen("a1.out","w",stdout);
	int testcase;
	int T;
	cin>>T;
	for (testcase = 1;testcase<=T;testcase++)
	{
		cin>>R;
		cin>>C;
		memset(a,0,sizeof a);
		for (int i=0;i<R;i++)
		{
			cin>>a[i];
		}
		int rsl = 1;
		for (int i=0;i<R;i++)
		{
			for (int j=0;j<C;j++)
			{
				if (a[i][j] == '#')
				{
					if (i< (R-1) && j < (C-1))
					{
						if (a[i][j+1] == '#' && a[i+1][j] == '#' && a[i+1][j+1] == '#')
						{
							a[i][j] = '\/'; a[i][j+1] = '\\'; a[i+1][j] = '\\'; a[i+1][j+1] = '\/';
						}
						else
						{
							rsl = 0;
							goto goto_1;
							
						}
					}
					else
					{
						rsl = 0;
						goto goto_1;
						
					}
				}
			}
		}
goto_1:
		cout<<"Case #"<<testcase<<":"<<endl;
		cerr<<"Case #"<<testcase<<":"<<endl;
		if (rsl == 0)
		{
			cout<<"Impossible"<<endl;
			cerr<<"Impossible"<<endl;
		}
		else
		{
			for (int i=0;i<R;i++)
			{
				cout<<a[i]<<endl;
				cerr<<a[i]<<endl;
			}
		}
	}


	return 0;
}
