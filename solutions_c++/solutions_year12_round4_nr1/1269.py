#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
vector <pair <int,int> > V;
vector <int> T;
int n,d,l,k;
int lastort=0;
void read()
{
	scanf ("%d", &n);
	while (n--)
	{
		scanf ("%d %d", &d,&l);
		V.push_back(make_pair(d,l));
	}
	scanf ("%d", &k);
	T.resize(V.size());
}
int main ()
{
	int t;
	scanf ("%d", &t);
	for (int r=1; r<=t; r++)
	{
		read();
		lastort=V[0].first;
		T[0]=lastort;
		for (int i=0; i<V.size(); i++)
		{
			int pozi=V[i].first;
//			printf ("i=%d vi=%d\n", i, vi);
			if (T[i]==0) continue;
			for (int j=i+1; j<V.size(); j++)
			{
				int pozj=V[j].first;
//				printf (" vj=%d T[vj]=%d, %d\n", vj,T[vj].first, T[vj].second);
				if (pozj<=pozi+T[i])
				{
					T[j]=max(T[j], pozj-pozi);
					T[j]=min(T[j], V[j].second);
					lastort=max(lastort,pozj+T[j]);
				}
				else break;
				if (lastort>=k) break;
			}
			if (lastort>=k) break;
		}
		if (lastort<k)
		{
			for (int i=0; i<V.size(); i++)
			{
//				printf ("i=%d V[i]=%d T[i]=%d\n", i,V[i].first, T[i]);
				if (V[i].first+T[i]>=k) 
				{
					lastort=k;
					break;
				}
			}
		}
		printf ("Case #%d: ", r);
		if (lastort>=k) printf ("YES\n");
		else printf ("NO\n");
		T.clear();
		V.clear();
	}
	return 0;
}
