#include <iostream>
#include <string>
using namespace std;
//const string s = "abcdefghijklmnopqrstuvwxyz";
const string t = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
//	freopen("test.in","r",stdin);
//	freopen("test.out","w",stdout);
	int n;
	string ss, tt;
	cin>>n;
	getline(cin,ss);
	for(int i=0;i<n;i++)
	{
		getline(cin,ss);
		cout<<"Case #"<<i + 1<<": ";
		for(int j = 0; j < ss.size(); j++)
		{
			if(ss[j] == ' ')
			{
				cout<<' ';
			}
			else
			{
				cout<<t[ss[j]-'a'];
			}
		}
		cout<<endl;
	}
	return 0;
}