#include <iostream>
using namespace std;

int main()
{
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	string s="yhesocvxduiglbkrztnwjpfmaq";
	string t;
	int cases=1;
	char ch;
	int repeat,i,j,k;
	cin>>repeat;
	while(ch=getchar())
		{
			if(ch=='\n')
			break;
		}
	while(repeat--)
	{
		
		getline(cin,t);
		cout<<"Case #"<<cases++<<": ";
		for(i=0;i<t.size();i++)
		{
			if(t[i]==' ')
			cout<<t[i];
			else
			cout<<s[t[i]-'a'];
		}
		cout<<endl;
		
	}
	
	
	


	return 0;
	
	
}