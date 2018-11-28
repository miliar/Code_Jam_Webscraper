#include<stdio.h>
#include<algorithm>
using namespace std;

int v[101], m[101];

void swap(int a, int b)
{
	int t = v[a];
	v[a] = v[b];
	v[b] = t;
}

void quick_sort(int beg, int end)
{
	if (end > beg + 1)
	{
		int pivot = beg, l = beg + 1, r = end;
		while (l < r)
		{
			if (v[l] <= v[pivot])
				l++;
			else
				swap(l,--r);
		}
		swap(--l, beg);
		quick_sort(beg, l);
		quick_sort(r, end);
  	}
}

int main()
{
	int T, c=0, i, N, S, p, max;
//	int m[101];
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d %d %d",&N,&S,&p);
		for(i=0; i<N; ++i)
			scanf("%d",&v[i]);
		//quick_sort(0, N);
		v[N]=1800000011;
		std::sort(v,v+N);
		for(i=0; i<N; ++i)
			m[i]=0;
		for(i=0; i<N; ++i)
		{
			if(v[i]==3*(p-1) && p<10 && S)
			{	m[i] = p+1; S--; }
			if(v[i]==3*(p-1)-1 && p<10 && S)
			{	m[i] = p+1; S--; }
		}
		for(i=0; i<N; ++i)
		{
			if(v[i]>28)
				m[i]=10;
			else if(v[i]<2)
				m[i]=v[i];
			else if(S && !m[i])
			{
				if(v[i]%3==0)
				{	m[i]=1+v[i]/3; S--; }
				if(v[i]%3==1)
					m[i]=1+v[i]/3;
				if(v[i]%3==2)
				{	m[i]=2+v[i]/3; S--; }
			}
			else if(!m[i])
			{
				if(v[i]%3==0)
					m[i]=v[i]/3;
				if(v[i]%3==1)
					m[i]=1+v[i]/3;
				if(v[i]%3==2)
					m[i]=1+v[i]/3;
			}
		}
		max=0;
		for(i=0; i<N; ++i)
			if(m[i]>=p) max++;
		printf("Case #%d: %d\n",++c,max);
	}
	return 0;
}