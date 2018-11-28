#include<iostream>
#include<cstring>
using namespace std;

char str[27]="yhesocvxduiglbkrztnwjpfmaq";
char upstr[27]="YHESOCVXDUIGLBKRZTNWJPFMAQ";

int main ()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int T;
	cin>>T;
	int Case=0;
	getchar();
	while(T--)
	{	Case++;
		char str1[101];
		gets(str1);

		int len=strlen(str1);
		for(int i=0;i<len;i++)
		{
			if(str1[i]>='a'&&str1[i]<='z')
				str1[i]=str[str1[i]-'a'];
		}
		cout<<"Case #"<<Case<<": ";
		for(int i=0;i<len;i++)
		{
			cout<<str1[i];
		}
		cout<<endl;
	}
	//system("pause");
	return 0;
}