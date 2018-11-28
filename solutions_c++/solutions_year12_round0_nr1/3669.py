#include<iostream>
using namespace std;

char s[1000],map[30]="yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	//freopen("11.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int T,tc;
	cin>>T;
	gets(s);
	for(tc=1;tc<=T;tc++)
	{
		gets(s);
		for(int i=0;s[i];i++)
			if(s[i]!=' ')
			{
				s[i]=map[s[i]-'a'];
			}
		cout<<"Case #"<<tc<<": "<<s<<endl;
	}
	return 0;
}