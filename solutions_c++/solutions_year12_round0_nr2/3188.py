#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

void main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int T;
	cin>>T;

	for(int Case=0;Case<T;Case++)
	{
		int N,S,P,T;
		int answer = 0;
		scanf("%d %d %d",&N,&S,&P);

		vector<int> t;
		t.resize(N);

		for(int i=0;i<N;i++)
		{
			scanf("%d",&t[i]);
			T = t[i]/3;
			if(t[i]%3 == 0)
			{
				if(T >= P)
					answer++;
				else if(T !=0 && S>0 && T+1 >= P)
				{
					answer++;
					S--;
				}
			}
			else if(t[i]%3 == 1)
			{
				if(T + 1 >= P)
					answer++;
			}
			else //if(t[i]%3 ==2 )
			{
				if(T + 1 >= P)
					answer++;
				else if(S>0 && T + 2 >= P)
				{
					answer++;
					S--;
				}
			}
		}

		printf("Case #%d: %d\n",Case+1,answer);
	}

}