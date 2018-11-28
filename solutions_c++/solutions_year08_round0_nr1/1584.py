#include <iostream>
#include <vector>
#include <set>
#include <sstream>
#include <map>
using namespace std;

#define OO (1<<30)

int dp[1010][110];
int s,q;

vector<string> queries;
vector<string> engines;

int f ( int qu , int en )
{
	if ( qu == q ) return 0;
	if ( en == s ) return OO;

	if ( dp [qu][en] != -1 )
		return dp [qu][en];

	int r1 = OO , r2 = OO , rt = OO;

	if ( queries[qu] != engines [en] )  
		r1 = f(qu+1,en);
	else 
	for ( int i = 0 ; i < s ; i ++ )
	{
		if ( i == en ) continue;
		rt = f(qu,i)+1;
		r2 = rt<r2? rt : r2 ; 
	}
	return dp [qu][en] = r1<r2 ? r1 :r2 ;
}
int main ()
{
	freopen("al.txt","rt",stdin);
	freopen("alo.txt","wt",stdout);
	int i,j,ncase,c=1;
	cin >> ncase;

	while (ncase>0)
	{
		memset(dp,-1,sizeof(dp));
		engines.clear();
		queries.clear();

		cin >> s;
		string temp;
		getline(cin,temp);

		for ( i = 0 ; i < s ; i ++ )
		{
			getline(cin,temp);
			//cout<<temp<<endl;
			engines.push_back(temp);
		}
		cin >> q;

		//cout << endl << endl;
		getline(cin,temp);

		for ( i = 0 ; i < q ; i ++ )
		{
			getline(cin,temp);
			//cout<<temp<<endl;
			queries.push_back(temp);
		}

		int ans = OO , tt = OO;
		for ( i = 0 ; i < s ; i ++ )
		{
			tt = f(0,i);
			ans = tt<ans ? tt : ans;
		}

		//Case #X: Y
		cout <<"Case #"<<c<<": "<<ans<<endl;
		c++;
		ncase--;
	}
	return 0;
}