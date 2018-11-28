#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<queue>
#include<map>
#include<set>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define Pi acos(-1.0)
#define Eps (1e-9)
#define pb push_back
#define mp make_pair
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define sqr(a) ((a)*(a))
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a))
pii ar[3];
int main()
{
	freopen("F.in","r",stdin);
	freopen("F.out","w",stdout);
	int T,ind=0;
	cin>>T;

	while(T)
	{
		T--;
		ind++;
		int N,M,a;
		cin>>N>>M>>a;
		ar[0].first=0;
		ar[1].second=0;
		bool f=false;
		for(ar[1].first=0;ar[1].first<=N;ar[1].first++)
		{
			if(f)break;
			for(ar[2].first=0;ar[2].first<=N;ar[2].first++)
			{
				if(f)break;
				for(ar[0].second=0;ar[0].second<=M;ar[0].second++)
				{
					if(f)break;
					for(ar[2].second=0;ar[2].second<=M;ar[2].second++)
					{
						int s=0;
						for(int i=0;i<3;i++)
							s+=ar[i].first*ar[(i+1)%3].second-ar[i].second*ar[(i+1)%3].first;
						s=abs(s);
						//cout<<s;
						if(s==a)
						{
							f=true;	
							cout<<"Case #"<<ind<<":";
							for(int i=0;i<3;i++)cout<<" "<<ar[i].first<<" "<<ar[i].second;
							cout<<endl;
							break;
						}
					}
				}
			}
		}
		if(!f)cout<<"Case #"<<ind<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}

