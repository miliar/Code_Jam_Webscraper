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
int f(string s)
{
	int i=1;
	while(i<s.length())
	{
		if(s[i-1]==s[i])
			s.erase(s.begin()+i-1);
		else i++;
	}
	return s.length();
}
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
		int k;
		string s;
		cin>>k>>s;
		vector<int> per;
		int i;
		for(i=0;i<k;i++)per.pb(i);
		int kil=1;
		for(i=2;i<=k;i++)kil*=i;
		int r=10000;
		for(i=0;i<kil;i++)
		{
			string ss=s;
			for(int j=0;j<s.length();j++)ss[j]=s[k*(j/k)+per[j%k]];
			r=MIN(r,f(ss));
			next_permutation(ALL(per));
		}
		cout<<"Case #"<<ind<<": "<<r<<endl;
	}
	return 0;
}

