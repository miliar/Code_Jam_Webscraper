#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int N;
int M;
int like[2048][2048];
int nlike[2048];
int special[2048];//which special flavor with 1
int sat;
int res[2048];
bool consider[2048];

int main()
{
	//freopen("test.in","r",stdin);
	//freopen("B-small-attempt2.out","w",stdout);

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T = 0;
	scanf("%d",&T);
	int tmp;
	int a,b;
	for(int i=0;i<T;i++)
	{
		scanf("%d",&N);
		scanf("%d",&M);
		memset(like,-1,sizeof(like));
		memset(nlike,0,sizeof(nlike));
		memset(res,0,sizeof(res));
		memset(special,-1,sizeof(special));
		for(int k=0;k<2048;k++)
		{
			consider[k] = true;
		}
		sat = 0;
		for(int j=0;j<M;j++)
		{
			scanf("%d",&tmp);
			for(int k=0;k<tmp;k++)
			{
				scanf("%d",&a);
				a--;
				scanf("%d",&b);
				if(like[j][a] == -1)
				{
					like[j][a] = b;
				}
				else
				{
					consider[j] = false;

				}
				if(b==0) 
				{
					nlike[j]++;
					if(nlike[j]==1)
					{
						sat++;
					}
				}
				else{
					special[j] = a;
				}
			}

		}
		bool pos = true;
		while(sat != M)
		{
			//cout<<sat<<endl;
			for(int j=0;j<M;j++)
			{
				if(nlike[j]==0  && consider[j])
				{
					if(special[j]<0)
					{
						pos = false;
						goto here;
					}
					res[special[j]]=1;
					nlike[j]++;
					sat++;
					for(int k=0;k<M;k++)
					{
						if(consider[k])
						{
							if(like[k][special[j]]==0 && k!=j)
							{
								nlike[k]--;
								if(nlike[k]==0)
									sat--;
							}
							if(special[k] == special[j] && k!=j)
							{
								nlike[k]++;
								if(nlike[k]==1)
									sat++;
							}
						}
					}
					//if(sat==M)
					//	break;
				}

			}
		}
here:
		if(pos)
		{
			printf("Case #%d:",i+1);
			for(int j=0;j<N;j++)
			{
				printf(" %d",res[j]);

			}
			printf("\n");

		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		}


		
		
		

	}

	
	
	return 0;
}