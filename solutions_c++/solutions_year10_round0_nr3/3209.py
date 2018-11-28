#include <stdio.h>
#include <deque>
#include <vector>

using namespace std;
typedef unsigned int uint;
typedef unsigned long ulong;
typedef unsigned long long ull;

int T = 0;

uint R=0, k=0, N=0;
deque<uint> q;
deque<pair<ulong,int>> data;
ulong y=0;

inline void doWork();

int main()
{
	FILE* fi = fopen("cj.in","r");
	FILE* fo = fopen("cj.out","wb");
	if (fi && fo)
	{
		fscanf(fi,"%i\n",&T);
		for (int t=1; t<=T; t++)
		{
			fscanf(fi, "%u %u %u\n", &R, &k, &N);
			q.resize(N);
			for (int n=0; n<N; n++)
			{
				fscanf(fi,"%u", &q[n]);
			}
			doWork();
			fprintf(fo, "Case #%i: %lu\n", t, y);
		}
	}
	if (fo) fclose(fo);
	if (fi) fclose(fi);
	return 0;
}

void doWork()
{
	data.resize(q.size());
	for (int i=0; i<data.size(); i++)
	{
		data[i].first  = 0; // max allowable sum for index i
		data[i].second = i; // the next if total sum <= k
		for (int j=0; j<q.size(); j++)
		{
			data[i].first += q[j];
			if (data[i].first  > k)
			{
				data[i].first -= q[j];
				data[i].second = (i+j)%data.size();
				break;
			}
		}
		q.push_back(q.front());
		q.pop_front();
//		printf("max allowable sum for index %d is %d\n",i,data[i].first);
	}
//	printf("\n");

	y = 0;
	for (int r=0, next=0; r<R; r++, next = data[next].second)
	{
		y += data[next].first;
	}
}
