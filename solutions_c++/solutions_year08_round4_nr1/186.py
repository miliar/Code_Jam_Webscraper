#include <iostream>
#include <fstream>
#include <set>
#include <string>

using namespace std;

const int INF=99999;

#define OR 0
#define AND 1
template <class T>
inline const T& TMIN(const T& x, const T& y)
{ return (y<x ? y : x); }

template <class T>
inline const T& TMIN(const T& x, const T& y, const T& z)
{ return (y<x ? TMIN(y,z) : TMIN(x,z)); }

void main()
{
	ofstream ofs("A-large.out");
	int i,j,k;
	int n;
	cin>>n;

	int x,v,m;

	int gate[10000];
	int change[10000];
	int one[10000];
	int zero[10000];

	for(i=0; i<n; i++)
	{
		cin>>m>>v;
		int ii=(m-1)/2;
		for(j=1; j<=ii; j++)
		{
			cin>>gate[j]>>change[j];
		}
		for(; j<=m; j++)
		{
			cin>>x;
			if(x==0)
			{
				one[j]=INF;
				zero[j]=0;
			}
			else
			{
				one[j]=0;
				zero[j]=INF;
			}
		}

		for(j=(m-1)/2; j>=1; j--)
		{
			if(gate[j]==OR)
			{
				one[j]=TMIN(one[j*2]+one[j*2+1] , one[j*2]+zero[j*2+1] , zero[j*2]+one[j*2+1]);
				zero[j]=zero[j*2]+zero[j*2+1];
				if(change[j])
					zero[j]=TMIN(zero[j], TMIN(zero[j*2]+zero[j*2+1] , one[j*2]+zero[j*2+1] , zero[j*2]+one[j*2+1])+1);

			}
			else
			{
				one[j]=one[j*2]+one[j*2+1];
				zero[j]=TMIN(zero[j*2]+zero[j*2+1] , one[j*2]+zero[j*2+1] , zero[j*2]+one[j*2+1]);
				if(change[j])
					one[j]=TMIN(one[j], TMIN(one[j*2]+one[j*2+1] , one[j*2]+zero[j*2+1] , zero[j*2]+one[j*2+1])+1);
			}
		}

		int ret;
		if(v==0)
			ret=zero[1];
		else
			ret=one[1];
		
		ofs<<"Case #"<<i+1<<": ";
		if(ret>=INF)
			ofs<<"IMPOSSIBLE"<<endl;
		else
			ofs<<ret<<endl;
	}
}
