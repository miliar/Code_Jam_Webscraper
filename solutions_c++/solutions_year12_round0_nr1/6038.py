#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char map[27]="yhesocvxduiglbkrztnwjpfmaq";
char str[5000];

int main()
{
	int n,cases,i,len;
	cin>>n;
	getchar();
	for(cases=1;cases<=n;cases++)
	{
		gets(str);
		len=strlen(str);
		for(i=0;i<len;i++)
			if('a'<=str[i] && str[i]<='z')
				str[i]=map[(int)(str[i]-'a')];
		cout<<"Case #"<<cases<<": "<<str<<endl;
	}
return 0;
}