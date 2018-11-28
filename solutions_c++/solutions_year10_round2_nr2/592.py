#include <fstream>
#include <set>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#define LL long long
using namespace std;
using namespace std;

int main()
{
	fstream cin("input.txt");
	ofstream cout("output.txt");
	int T=0;
	cin>>T;
	for(LL ti=1;ti<=T;ti++)
	{
		int N,K,T,B;
		cin>>N>>K>>B>>T;
		vector<int> V(N),X(N);
		vector<int> mozet;
		for(int i=0;i<N;i++) cin>>X[i];
		for(int i=0;i<N;i++) cin>>V[i];
		for(int i=V.size()-1;i>=0 && mozet.size()<K;i--)
		if((B - X[i]) <= T * V[i])mozet.push_back(V.size() - i - 1);
		cout<<"Case #"<<ti<<": ";
		if(mozet.size()<K)
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		int res = 0;
		for(int i=0;i<mozet.size();i++)
			res += mozet[i] - i;
		cout<<res<<endl;
	}
	cout.close();
	cin.close();
	return 0;
}

/*#include <fstream>
#include <set>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#define LL long long
using namespace std;
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T=0;
	cin>>T;
	for(LL ti=1;ti<=T;ti++)
	{
		int n;
		cin>>n;
		map<int,int> p,pb;
		vector<int> p_;
		vector<char> prime (4020, true);
		int kp=1;
		for (int i=2; i<=4000; ++i)
			if (prime[i])
			{
				p[i]=kp;
				pb[kp]=i;
				kp++;
				p_.push_back(i);
				for (int j=i+i; j<=4000; j+=i)
					prime[j] = false;
			}
		int cur=1;
		int cnt=0;
		while(p[cur]<=n)
		{
			cnt++;
			cur=pb[cur];
		}
		cout<<"Case #"<<ti<<": ";
		cout<<cnt;
		cout<<endl;
	}
	cout.close();
	cin.close();
	return 0;
}*/
/*#include <fstream>
#include <set>
#include <algorithm>
#include <string>
#include <map>
#define LL long long
using namespace std;
void parse(string &b,set<string> &a)
{
	string dir="";
	for(int i=1;i<b.size();i++)
	{
		if(b[i]=='/')
			a.insert(dir);
		dir+=b[i];
	}
	a.insert(dir);
}
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T=0;
	cin>>T;
	for(LL ti=1;ti<=T;ti++)
	{
		
		int n,k;
		cin>>n>>k;
		set<string> a;
		string temp;
		for(int i=0;i<k+n;i++)
		{
			cin>>temp;
			parse(temp,a);
		}
		int cnt=0;
		cnt=a.size()-n;
		if(cnt<0) cnt=0;
		cout<<"Case #"<<ti<<": ";
		cout<<cnt;
		cout<<endl;
	}
	cout.close();
	cin.close();
	return 0;
}
*/