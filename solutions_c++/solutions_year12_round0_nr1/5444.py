
 //in the name of ALLAH 
#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<fstream>
using namespace std;

string a="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	 freopen ("A.in","r",stdin);
	  freopen ("A.out","w",stdout);
	string ins,outs;
	int t;
	cin>>t;
	cin.ignore();
	for(int tc=1;tc<=t;tc++)
	{
		
		getline(cin,ins);

		printf("Case #%d: ",tc);
		for(int i=0;i<ins.length();i++)
		{
			if(!isspace(ins[i]) )
				cout<<a[ins[i]-'a'];
			else cout<<" ";
		}
		cout<<endl;
	}
	return 0;
}
//AmzMohammad


