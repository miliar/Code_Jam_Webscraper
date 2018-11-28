#include "../common.h"

using namespace std;
int fn[1000];
int N,L,H;
int main()
{
	FILE *fp = NULL;
	fp = freopen("C-small-attempt2.in","r",stdin);
	fp = freopen("c.out","w",stdout);
	int testcase;
	int T;
	cin>>T;
	for (testcase = 1;testcase<=T;testcase++)
	{
		cin>>N;
		cin>>L;
		cin>>H;
		for (int i=0;i<N;i++)
		{
			cin>>fn[i];
		}
		int rsl = 0;

		for (int j = L;j<=H;j++)
		{
			rsl = 1;
			for (int k =0;k <N;k++)
			{
				if ((j!=fn[k] || 1) && (((fn[k]% j) == 0) || ((j%fn[k]) == 0)))
				{
					
				}
				else
				{
					rsl = 0;
					break;
				}
			}
			if (rsl == 1)
			{
				rsl = j;
				goto goto_1;
			}
		}

goto_1:

		cout<<"Case #"<<testcase<<": ";
		cerr<<"Case #"<<testcase<<": ";
		if (rsl > 0)
		{
			cout<<rsl<<endl;
			cerr<<rsl<<endl;
		}
		else
		{
			cout<<"NO"<<endl;
			cerr<<"NO"<<endl;
		}
		
	}


	return 0;
}
