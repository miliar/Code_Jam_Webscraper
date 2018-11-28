#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

#define forV(va,ve) for(int va=0;va < ve.size();++va)
#define V(t) vector< t >
#define Vall(t) t.begin(),t.end()

int N;
vector<string> v;
vector<int> vv;
vector<int> valpha;

int memo[100][100];

int dp(int at,int use)
{
	if(at == N){return 0;}
	int &ret = memo[at][use+1];
	if(ret != -1)
	{
		return ret;
	}
	ret = dp(at+1,use);
	if(use == -1 || vv[at] > vv[use])
	{
		ret >?= 1 + dp(at+1,at);
	}
	return ret;
}


int main(void)
{
	int N;
	cin >> N;
	string s;
	for(int cn=1;cn <= N;++cn)
	{
		int T;
		cin >> T;
		vector<long long> a(T,0),b(T,0);
		for(int i=0;i<T;++i)
		{
			cin >> a[i];
		}
		for(int i=0;i<T;++i)
		{
			cin >> b[i];
		}
		sort(Vall(a));
		sort(Vall(b));
		reverse(Vall(b));

		long long out = 0;
		for(int i=0;i<T;++i)
		{
			out += a[i]*b[i];
		}
		reverse(Vall(b));
		reverse(Vall(a));
		long long oout = 0;
		for(int i=0;i<T;++i)
		{
			oout += a[i]*b[i];
		}
		out <?= oout;
		cout << "Case #" << cn << ": " << out << endl;
	}
	return 0;
}
