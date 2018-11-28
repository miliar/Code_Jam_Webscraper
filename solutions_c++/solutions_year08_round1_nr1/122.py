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
		int n;
		cin>>n;
		vector<ll> a(n),b(n);
		int i;
		int tmp;
		for(i=0;i<n;i++)
		{
			scanf("%d",&tmp);
			a[i]=tmp;
		}
		for(i=0;i<n;i++)
		{
			scanf("%d",&tmp);
			b[i]=tmp;
		}
		SORT(a);
		SORT(b);
		long long res=0;
		for(i=0;i<n;i++)res+=a[i]*b[n-1-i];
		cout<<"Case #"<<ind<<": "<<res<<endl;
	}
	return 0;
}

