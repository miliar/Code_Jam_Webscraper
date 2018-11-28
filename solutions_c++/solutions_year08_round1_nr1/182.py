#include <iostream>
#include <vector>

using namespace std;
#define pb push_back
#define LL long long

int main()
{
	int T;
	scanf("%d",&T);
	int c=0;
	while(T--)
	{
		int N;
		scanf("%d",&N);
		vector<int> a(N),b(N);
		for(int i=0;i<N;i++)
			cin>>a[i];
		for(int i=0;i<N;i++)
			cin>>b[i];

		vector<LL> a1,a2,b1,b2;
		for(int i=0;i<N;i++)
		{
			if(a[i]>0) a1.pb(a[i]);
			if(a[i]<0) a2.pb(-a[i]);
			if(b[i]>0) b1.pb(b[i]);
			if(b[i]<0) b2.pb(-b[i]);
		}

		sort(a1.begin(),a1.end());
		sort(a2.begin(),a2.end());
		sort(b1.begin(),b1.end());
		sort(b2.begin(),b2.end());

		LL ret = 0;
		int na1 = a1.size();
		int na2 = a2.size();
		int nb1 = b1.size();
		int nb2 = b2.size();
		int nz1 = N - na1 - na2;
		int nz2 = N - nb1 - nb2;
		vector<LL> aa,bb;
 		for(int i=0; i< min(na1,nb2); i++)
			ret-= a1[na1-1-i]*b2[nb2-1-i];
		for(int i=0;i< min(na2,nb1); i++)
			ret-= a2[na2-1-i]*b1[nb1-1-i];
		for(int i=0;i<min(na1 - nb2 - nz2, nb1 - na2 - nz1);i++)
		{
			aa.pb( a1[i]);
			bb.pb( b1[i]);
		}
		for(int i=0;i<min(na2 - nb1 - nz2, nb2 - na1 - nz1);i++)
		{
			aa.pb( a2[i]);
			bb.pb( b2[i]);
		}
		reverse( bb.begin(), bb.end());
		for(int i=0;i<aa.size();i++)
			ret += aa[i]*bb[i];

		cout<<"Case #"<<++c<<": "<<ret<<"\n";
	}
	return 0;
}
