#include <iostream>
#include <fstream>
#include <list>
using namespace std;
void main()
{
	freopen("C-small-attempt0.in.txt","r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);

	for (int ctr = 1; ctr <= T; ctr++)
	{
		int R;
		scanf("%d", &R);
		int K;
		scanf("%d", &K);
		int N;
		scanf("%d", &N);

		list<int> glist;
		for(int i = 0; i < N; i++)
		{
			int G;
			scanf("%d", &G);
			glist.push_back(G);
		}

		int money = 0;
		for(int j = 0; j < R; j++)
		{
			int n=0;
			int pos=0;
			while(n < K && pos < N)
			{
				int p=*glist.begin();
				if((n+p) > K)
					break;
				glist.pop_front();
				glist.push_back(p);
				n+=p;
				pos++;
			}
			money+=n;
		}
		cout<<"Case #"<<ctr<<":  "<<money<<endl;
	}

}