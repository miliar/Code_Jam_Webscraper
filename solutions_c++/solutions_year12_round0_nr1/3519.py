#include<iostream>
#include<string>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long cases,count=1;
	
	string dics = "yhesocvxduiglbkrztnwjpfmaq";
	
	string str,out;
	scanf("%ld\n",&cases);
	while(cases--)
	{
		getline(cin,str);
		
		out = "";
		for(int i=0;i<str.length();i++)
		{
			if(str[i]>='a'&&str[i]<='z')
				out+=dics[str[i]-'a'];
			else out+=str[i];
		}
		cout<<"Case #"<<count<<": "<<out<<endl;
		count++;
	}


	return 0;
}