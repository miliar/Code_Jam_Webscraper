#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    char replace[]="yhesocvxduiglbkrztnwjpfmaq";

	int cases;
	cin>>cases;
	char str[110];
	int length;
	gets(str);
	for(int count = 1;count<=cases;count++)
	{
		/*cin.getline(str,110);*/
		gets(str);
		length = strlen(str);
		for(int i = 0;i<length;i++)
		{
			if(str[i]-'a'>=0)
				str[i] = replace[str[i]-'a'];
		}
		cout<<"Case #"<<count<<": "<<str<<endl;		
	}

	return 0;
}