#include <iostream>
#include <vector>

using namespace std;

class event
{
	public:
		int ind;
		int inc;
		int time;
};

bool lt( event a, event b)
{
	return ( a.time < b.time || (a.time == b.time && a.inc > b.inc));
}

vector<event> v;

bool simulate(int arr[2])
{
	for(int i=0;i<v.size();i++)
	{
		arr[v[i].ind]+=v[i].inc;
		for(int j=0;j<2;j++)
			if(arr[j]<0) return 0;
	}
	return 1;
}

int main()
{
	int N;
	scanf("%d",&N);
	int cnt = 0;
	while(N--)
	{
		cnt++;
		int T,NA,NB;
		v.clear();
		scanf("%d",&T);
		scanf("%d %d",&NA,&NB);
		for(int i=0;i<NA;i++)
		{
			int h1,m1,h2,m2;
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			m1 += 60*h1;
			m2 += 60*h2;
			m2 += T;
			event e1,e2;
			e1.ind = 0;
			e2.ind = 1;
			e1.inc = -1;
			e2.inc = 1;
			e1.time = m1;
			e2.time = m2;
			v.push_back(e1);
			v.push_back(e2);
		}
		
		for(int i=0;i<NB;i++)
		{
			int h1,m1,h2,m2;
			scanf("%d:%d %d:%d",&h1,&m1,&h2,&m2);
			m1 += 60*h1;
			m2 += 60*h2;
			m2 += T;
			event e1,e2;
			e1.ind = 1;
			e2.ind = 0;
			e1.inc = -1;
			e2.inc = 1;
			e1.time = m1;
			e2.time = m2;
			v.push_back(e1);
			v.push_back(e2);
		}
		sort( v.begin(), v.end() ,lt);
		bool f = 1;
		for(int i=0;f;i++)
			for(int j=0;j<=NB && f;j++)
			{
				int arr[2];
				arr[0] = i; arr[1] = j;
				if(simulate(arr))
				{
					printf("Case #%d: %d %d\n",cnt,i,j);
					f = 0;
				}
							
		  }
	}
}
