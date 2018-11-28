#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

#define forV(va,ve) for(int va=0;va < ve.size();++va)
#define V(t) vector< t >
#define Vall(t) t.begin(),t.end()
vector<string> es;
vector<string> q;

int memo[1000][1000];

int dp(int at,int se)
{
	if(at == q.size()){return 0;}
	int &ret = memo[at][se];
	if(ret != -1){return ret;}
	if(q[at] == es[se]){return 100000;}
	ret = 1000000;
	for(int i=0;i<es.size();++i)
	{
		ret <?= dp(at+1,i) + ((i == se)?(0):(1));
	}
	return ret;
}

int main(void)
{
	int N;
	cin >> N;
	for(int cn=1;cn <= N;++cn)
	{
		int S,Q;
		memset(memo,-1,sizeof(memo));
		cin >> S;
		es.clear();
		q.clear();
		string ss;
		getline(cin,ss);
		for(int i=0;i<S;++i)
		{
			getline(cin,ss);
			es.push_back(ss);
		}
		//read case
		cin >> Q;
		getline(cin,ss);
		for(int i=0;i<Q;++i)
		{
			getline(cin,ss);
			q.push_back(ss);
		}
		int out = 1000000;
		for(int i=0;i<S;++i)
		{
			out <?= dp(0,i);
		}
		cout << "Case #" << cn << ": " << out << endl;

	}
	return 0;
}
