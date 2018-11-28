#include <iostream>
#include <string>
#include <sstream>
#include <map>
using namespace std;

int T;
int A, B;
int sz;
int recp;

const int mx=200001;
int d[mx];

string str(int x)
{
	stringstream ss;
	ss<<x;
	return ss.str();
}

int solve(int x)
{
	map<string, bool> used;
	string sx=str(x);
	string sB=str(B);
	string ts;
	string t=sx+sx;
	int ret=0;

	for(int i=0; i<sz; ++i)
	{
		ts=t.substr(i, sz);
		if(ts>sx && ts<=sB && !used[ts] && t.find(ts)!=string::npos) 
		{
			ret++;
			used[ts]=1;
		}
	}
	
	return ret;
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	cin>>T;
	for(int i=0; i<T; i++)
	{
		printf("Case #%d: ", i+1);
		cin>>A>>B;
		sz=str(A).size();
		recp=0;
		for(int i=A; i<B; ++i)
		{
			recp+=solve(i);
		}
		cout<<recp<<endl;
	}

	fclose(stdout);
}