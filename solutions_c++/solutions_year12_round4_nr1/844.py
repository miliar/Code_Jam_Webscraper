#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

#define MAXN 10000

class Liane
{
	public:
	int l, p, s;
	Liane(int p, int l) : p(p), l(l) {s=0;};
	bool operator< (const Liane& rhs) const
	{ return p<rhs.p; }
};

int main()
{
	int T;
	int N, D, p, l, h, k;
	vector<Liane> lians;
	cin>>T;
	for (int t=1; t<=T; t++)
	{
		lians.clear();
		cin>>N;
		for (int i=0; i<N; i++)
		{
			cin>>p>>l;
			lians.push_back( Liane(p,l) );
		}
		cin>>D;
		sort( lians.begin(), lians.end() );
		
		lians[0].s = min( lians[0].p, lians[0].l );
		for (int i=0; i<N; i++)
			for (int j=i+1; j<N; j++)
				if (lians[i].p+lians[i].s >= lians[j].p)
					lians[j].s = max( lians[j].s, min( lians[j].p-lians[i].p, lians[j].l ) );
				else
					break;

		for (int i=0; i<N; i++)
			if (lians[i].p + lians[i].s >= D)
			{
				cout<<"Case #"<<t<<": YES"<<endl;
				goto done;
			}
		cout<<"Case #"<<t<<": NO"<<endl;
		done: ;
	}
	return 0;
}

