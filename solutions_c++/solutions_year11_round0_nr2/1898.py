#include<iostream>
#include<cmath>
#include<string>
using namespace std;

char com[30][30];
char opp[30][30];

int c2i(char c)
{
	return c-'A'+1;
}

bool canCom(string& s, char c)
{
	int len = s.length();
	if(len>0 && com[ c2i(s[len-1]) ][ c2i(c) ] ) return true;
	else return false;
}

bool canOpp(string& s, char c)
{
	int len = s.length();
	for(int i=0;i<len;i++)
	{
		if(opp[ c2i(s[i]) ][ c2i(c) ]) return true;
	}
	return false;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
//	freopen("1.txt","r",stdin);
	int T,C,D,N;
	cin>>T;
	string tmp,s;
	for(int cas=1;cas<=T;cas++)
	{
		cin>>C;
		memset(com,0,sizeof(com));
		for(int i=0;i<C;i++)
		{
			cin>>tmp;
			com[ c2i(tmp[0]) ][ c2i(tmp[1]) ] = c2i(tmp[2]);
			com[ c2i(tmp[1]) ][ c2i(tmp[0]) ] = c2i(tmp[2]);
		}

		cin>>D;
		memset(opp,0,sizeof(opp));
		for(int i=0;i<D;i++)
		{
			cin>>tmp;
			opp[ c2i(tmp[0]) ][ c2i(tmp[1]) ] = 1;
			opp[ c2i(tmp[1]) ][ c2i(tmp[0]) ] = 1;
		}

		cin>>N>>s;
		string res = "";
		for(int i=0;i<N;i++)
		{
			int idx = res.length();
			if(canCom(res,s[i]))
			{
				res[idx-1] = com[ c2i(res[idx-1]) ][ c2i(s[i]) ]+'A'-1;
			}
			else if(canOpp(res,s[i]))
			{
				res = "";
			}
			else
			{
				res += s[i];
			}
		}

		cout<<"Case #"<<cas<<": [";
		for(int i=0;i+1<res.length();i++)
		{
			cout<<res[i]<<", ";
		}
		if(res.length()>0) cout<<res[res.length()-1];
		cout<<"]\n";

	}
	return 0;
}