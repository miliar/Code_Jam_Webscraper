#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
using namespace std;
char c[100];
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	memset(c,0,sizeof c);
	string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	int n = a.length();
	for(int i=0;i<n;i++)
	{
		if(a[i] != ' ')
			c[a[i]-'a'] = b[i];
	}
	c['q' - 'a'] = 'z';
	c['z' - 'a'] = 'q';
	int t;
	scanf("%d\n",&t);
	int temp = t;
	while(t--)
	{
		string input;
		string output;
		output.clear();
		getline(cin,input,'\n');
		int len = input.length();
		for(int i=0;i<len;i++)
		{
			if(input[i] == ' ')
				output.insert(output.end(),1,' ');
			else
				output.insert(output.end(),1,c[input[i]-'a']);
		}
		cout<<"Case #"<<temp-t<<": "<<output<<endl;
	}
}
