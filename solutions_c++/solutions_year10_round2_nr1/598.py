#include <fstream>
#include <set>
#include <algorithm>
#include <string>
#include <map>
#define LL long long
using namespace std;
void parse(string &b,set<string> &a)
{
	string dir="";
	for(int i=1;i<b.size();i++)
	{
		if(b[i]=='/')
			a.insert(dir);
		dir+=b[i];
	}
	a.insert(dir);
}
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T=0;
	cin>>T;
	for(LL ti=1;ti<=T;ti++)
	{
		
		int n,k;
		cin>>n>>k;
		set<string> a;
		string temp;
		for(int i=0;i<k+n;i++)
		{
			cin>>temp;
			parse(temp,a);
		}
		int cnt=0;
		cnt=a.size()-n;
		if(cnt<0) cnt=0;
		cout<<"Case #"<<ti<<": ";
		cout<<cnt;
		cout<<endl;
	}
	cout.close();
	cin.close();
	return 0;
}