#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

long long sm[1001];
int nm[1001];
int in[1001];
int R,K,N;

int main ()
{

	freopen ("input", "r", stdin);
	freopen ("output", "w", stdout);

	int cases=0;

	scanf ("%d", &cases);

	for (int c=1;c<=cases;c++)
	{
		scanf ("%d%d%d",&R, &K, &N); 
		for (int i=0;i<N;i++)
			scanf ("%d", &in[i]);

		long long sum=0;

		memset (sm,-1,sizeof (sm));
		int num=0;
		bool done=0;
		int now=0;

		while (R>0)
		{
			num++;
			if (sm[now]!=-1 && !done)
			{
				sum+=((long long)R/(num-nm[now]))*(sum-sm[now]);
				R%=(num-nm[now]);
				done=1;
			}
			if (R==0)
				break;
			if (!done) 
			{
				sm[now]=sum;
				nm[now]=num;
			}
			long long coaster=0;
			int tmp;
			bool flag=0;
			for (tmp=now;!(flag&&tmp==now);tmp=(tmp+1)%N)
			{
				if (coaster+in[tmp]>K) break;
				coaster+=in[tmp];
				flag=1;
			}
			sum+=coaster;
			now=tmp;
			R--;
		}
		cout<<"Case #"<<c<<": "<<sum<<endl;
	}
}
