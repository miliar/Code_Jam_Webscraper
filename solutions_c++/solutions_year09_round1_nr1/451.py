#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <sstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> pii; 

string C(int N, int B)
{
	//cout<<N<<' '<<B<<endl;
	string res = "0";
	if (N == 0)
		return "";
	else
	{
		res[0] += N % B;
		return C(N / B, B) + res;
	}
}

set<string> s;

int H(int N, int B)
{
	string p = C(N, B);
	s.clear();
	//return 0;
	while (1)
	{
	//cout<<N<<' '<<p<<endl;
		if (s.find(p) != s.end())
			return 0;
		s.insert(p);
		if (p == "1")
			return 1;
		int t = 0;
		REP(i, p.size())
			t += (p[i] - '0') * (p[i] - '0');
		p = C(t, B);
	}
}




int main()
{
	int cases;
	scanf("%d", &cases);
	string s;
	getline(cin, s);
	REP(caseIndex, cases)
	{
		getline(cin, s);
		istringstream sin(s);
		vector<int> v;
		int tmp;
		while (sin>>tmp)
			v.push_back(tmp);
		printf("Case #%d: ", caseIndex + 1);
		for (int i = 2; ; i++)
		{
			int suc = 1;
			for (int j = 0 ; j < v.size(); j++)
			{
				if (!H(i, v[j]))
				{
					suc = 0;
					break;
				}
			}
			if (suc)
			{
				printf("%d\n", i);
				break;
			}
		}
	}
}
