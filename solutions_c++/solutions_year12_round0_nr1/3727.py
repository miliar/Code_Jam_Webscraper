#include <iostream>
#include <string>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	char arr[]="yhesocvxduiglbkrztnwjpfmaq";
	/*
	for(int i=0;i<26;i++)
		arr[i] = '-';

	string str1,str2;
	


	getline(cin,str1);
	getline(cin,str2);

	for(char i = 'a';i<='z';i++)
		cout<<i;
	cout<<endl;

	for(int i=0;i<str1.size();i++)
		if(str1[i] != ' ')
			arr[str1[i]-'a'] = str2[i];


	cout<<arr<<endl;
	*/

	int n;
	cin>>n;
	cin.ignore(1);
	for(int i=0;i<n;i++)
	{
		string str;
		getline(cin, str);
		
		cout<<"Case #"<<i+1<<": ";

		for(int j=0;j<str.size();j++)
		{
			if(str[j] == ' ')
				cout<<" ";
			else
				cout<<arr[str[j]-'a'];
		}
		cout<<endl;

	}
	

	return 0;
}