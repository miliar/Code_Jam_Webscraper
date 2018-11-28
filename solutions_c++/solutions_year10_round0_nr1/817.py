#include <fstream>
#include <stack>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#define LL long long
using namespace std;
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	LL T=0;
	cin>>T;
	for(LL ti=1;ti<=T;ti++)
	{
		LL N,K;
		cin>>K>>N;
		vector<LL> res;
		if(N==0) res.push_back(0);
		while(N!=0)
		{
			res.insert(res.begin(),N%2);
			N/=2;
		}
		reverse(res.begin(),res.end());
		LL mx=-1;
		res.resize(K+5);
		for(LL i=0;i<res.size() && res[i];i++)
			mx=i;
		cout<<"Case #"<<ti<<": ";
		if((K-1)<=mx)cout<<"ON"<<endl; else cout<<"OFF"<<endl;
	}
	cout.close();
	cin.close();
	return 0;
}