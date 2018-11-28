#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <cstdio>

using namespace std;

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
}

void solve()
{
	int tests;
	cin>>tests;
	for (int q=1;q<=tests;++q)
	{
		long double EPS = 1e-6;
		int r,c,d;
		cin>>r>>c>>d;
		int cont=1;
		vector< vector<int> > v (r, vector<int> (c));
		char ch;
		for (int i=0;i<r;++i)
			for (int j=0;j<c;++j)
			{
				cin>>ch;
				v[i][j]=ch-'0';
			}
		cout<<"Case #"<<q<<": ";
		for (int k=min(r,c);k>2&&cont;--k)
		{
			for (int vl=0; vl<r-k+1&&cont;++vl)
				for (int vr=0; vr<c-k+1&&cont;++vr)
				{
					double sum1x=0,sum2=0,sum1y=0;
					for (int i=0;i<k;++i)
						for (int j=0; j<k;++j)
						{
							if ((i==0&&j==0) || (i==k-1 &&j==0)||(i==0&&j==k-1)||(i==k-1 &&j==k-1))
								;
							else
							{
								sum1x+=(i+.5)*(d+v[vl+i][vr+j]);
								sum1y+=(j+.5)*(d+v[vl+k-1-i][vr+k-1-j]);
								sum2+=d+v[vl+i][vr+j];
							}
							
						}
					//cout<<sum1x/sum2<<" " <<sum1y/sum2<<endl;
					if (abs(2*sum1x/sum2-k)<EPS && abs(2*sum1y/sum2-k)<EPS)
					{
						cout<<k<<endl;
						cont=0;
					}
				}

		}
		if (cont)
			cout<<"IMPOSSIBLE"<<endl;
	}
}

int main()
{
	prepare();
	solve();
	return 0;
}
