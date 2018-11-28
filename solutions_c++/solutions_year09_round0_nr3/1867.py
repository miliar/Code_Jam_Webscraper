#include <iostream>
#include <vector>
#include <string>

using namespace std;

int cache[20][501];

string a="welcome to code jam";
string b;

int dp(int i, int j)
{
	if(j<0) return 0;
	if(i<0) return 0;
	if(i>18) return 0;
	if(j>=(int)b.length()) return 0;

	if(cache[i][j]!=-1)
		return cache[i][j];

	int &ret = cache[i][j] = 0;

	if(a[i]!=b[j])
	{
		for(int jj=j-1;jj>=0;jj--)
			if(a[i]==b[jj])
				ret=max(ret,dp(i,jj));
	}
	else
	{
		int cnt=dp(i-1,j-1);
		if(i==0) cnt=1;
		cnt += dp(i,j-1);
		ret = cnt % 10000;
	}

	return ret;
}

int main()
{

	int TestCase;
	cin >> TestCase;

	getline(cin, b);
	for(int ti=0;ti<TestCase;ti++)
	{
		for(int i=0;i<20;i++)
			for(int j=0;j<500;j++)
				cache[i][j]=-1;
		
		getline(cin, b);

		char strout[5];
		int ret=dp(18,(int)b.length()-1);
		ret %= 10000;
		sprintf(strout, "%04d",ret);

		cout << "Case #"<<ti+1<< ": "<<strout<<endl;
	}
	return 0;
}

