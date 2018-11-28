#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int P;
int K;
int L;
vector<int> F;

void main()
{

	int i,j;
	int f,t,len;
	int result;
	bool done;
	scanf("%d",&N);

	for(i=1;i<=N;i++)
	{
		result=0;
		done=false;
		scanf("%d%d%d",&P,&K,&L);
		for(j=0;j<L;j++)
		{
			scanf("%d",&t);
			F.push_back(t);
		}

		sort(F.begin(),F.end());
		len=F.size();
		f=1;
		while(!done)
		{
			for(j=0;j<K;j++)
			{
				result+=F[len-1]*f;
				len--;
				if(len<1)
				{
					done=true;
					break;
				}
			}
			f++;
		}

		printf("Case #%d: %d\n",i,result);
		F.clear();
	}
}