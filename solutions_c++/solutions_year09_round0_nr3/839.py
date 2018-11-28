#include<iostream>
#include<map>
#include<string>
#include<sstream>
#include<vector>
using namespace std;

string patt="welcome to code jam";
string text; // "something. :)
int m=10000;
int memo[510][510];

int recur(int pi,int ti)
{
	if(pi==patt.size()) return 1;
	if(ti==text.size()) return 0;
	if(memo[pi][ti]!=-1) return memo[pi][ti];
	int rv=0;
	if(patt[pi]==text[ti])
	{
		rv+=recur(pi+1,ti+1);
		rv%=m;
	}
	rv=rv+recur(pi,ti+1);
	rv=rv%m;
	return memo[pi][ti]=rv;

}

int main()
{
	int n; cin>>n;
	cin.ignore();
	int cn=0;
	while(n--)
	{
		cn++;
		memset(memo,-1,sizeof(memo));
		getline(cin,text);
		int rv=recur(0,0);
		ostringstream os;
		os<<rv;
		string temp=os.str();
		while(temp.size()<4) temp.insert(temp.begin(),'0');
		cout<<"Case #"<<cn<<": ";
		cout<<temp<<endl;
	}

}
