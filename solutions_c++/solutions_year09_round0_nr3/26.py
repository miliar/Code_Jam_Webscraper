#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string tar="welcome to code jam", data;
int dynamic[500][19];

int getDynamic(int, int);

int main(void)
{
	int t;
	cin>>t;
	string dummy;
	getline(cin, dummy);

	for(int caseN=1;caseN<=t;caseN++)
	{
		memset(dynamic, -1, sizeof(dynamic));
		getline(cin, data);

		int ans=getDynamic((int)data.size()-1, 18);
		string res;
		for(int i=0;i<4;i++) { res+=(char)(ans%10+'0'); ans/=10; }
		reverse(res.begin(), res.end());

		cout<<"Case #"<<caseN<<": "<<res<<endl;
	}

	return 0;
}

int getDynamic(int nth, int lev)
{
	if(nth<0) return 0;
	int &ret=dynamic[nth][lev];
	if(ret!=-1) return ret;

	ret=getDynamic(nth-1, lev);
	if(data[nth]==tar[lev]) 
	{
		if(lev!=0) ret+=getDynamic(nth-1, lev-1);
		else ret++;
	}

	ret%=10000;
	return ret;
}
