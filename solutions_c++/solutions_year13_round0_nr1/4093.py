#include<iostream>
#include<vector>
#include<fstream>
#include<queue>
#include<algorithm>
#include<list>
#include<cstdio>
#include<stack>
#include<cstring>
#include<cmath>
#include<string>
#include<map>
using namespace std;
#define     FOR(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     FIT(it,v)         for (typeof((v).begin())it=(v).begin(); it!=(v).end(); ++it)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     GSORT(x)          sort(ALL(x), greater<typeof(*((x).begin()))>())
#define     UNIQUE(v)         SORT(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
typedef long long ll;
typedef pair<int,int> pii;
int n;
string st;
int main(){
	int t, tc=1;
	freopen("a.in","r",stdin);
	ofstream cout("a.out");
	cin>>t;
	string s[4];
	while(t--)
	{
		cout<<"Case #"<<tc++<<": ";
		Rep(i,4) cin>>s[i];
		bool sw=0, dot=0;
		Rep(i,4)
		{
			int o=0,x=0;
			Rep(j,4)
			{
				if(s[i][j]=='O') o++;
				else if(s[i][j]=='X') x++;
				else if(s[i][j]=='T') o++,x++;
				else if(s[i][j]=='.') dot=1;
			}
			if(x==4)
			{
				cout<<"X won\n";
				sw=1;
				break;
			}
			else if(o==4)
			{
				cout<<"O won\n";
				sw=1;
				break;
			}
		}
		if(sw) continue;
		Rep(i,4)
		{
			int o=0,x=0;
			Rep(j,4)
			{
				if(s[j][i]=='O') o++;
				else if(s[j][i]=='X') x++;
				else if(s[j][i]=='T') o++,x++;
			}
			if(x==4)
			{
				cout<<"X won\n";
				sw=1;
				break;
			}
			else if(o==4)
			{
				cout<<"O won\n";
				sw=1;
				break;
			}
		}
		if(sw) continue;
		int o=0,x=0;
		Rep(i,4)
		{
			if(s[i][i]=='O') o++;
			else if(s[i][i]=='X') x++;
			else if(s[i][i]=='T') o++,x++;
		}
		if(x==4)
		{
			cout<<"X won\n";
			continue;
		}
		else if(o==4)
		{
			cout<<"O won\n";
			continue;
		}
		o=x=0;
		Rep(i,4)
		{
			if(s[i][3-i]=='O') o++;
			else if(s[i][3-i]=='X') x++;
			else if(s[i][3-i]=='T') o++,x++;
		}
		if(x==4)
		{
			cout<<"X won\n";
			continue;
		}
		else if(o==4)
		{
			cout<<"O won\n";
			continue;
		}
		if(dot==1) 
			cout<<"Game has not completed\n";
		else cout<<"Draw\n";
	}
	return 0;
}