#include<iostream>
#include<string>
#include<cstring>
using namespace std;
main()
{
char reese[]="yhesocvxduiglbkrztnwjpfmaq";
string str;
int T;
cin>>T;
getline(cin,str);
string *output = new string[T];
string *out = new string[T];
for(int i=0;i<T;i++)
{
        getline(cin,str);
	out[i]=str;
        for(int j=0;j<str.length();j++)
                {
                if(str[j]>='a' && str[j]<='z')
                    output[i]+= reese[str[j]-'a'];
                else
                    output[i]+=str[j];
                }
}
for(int i=0;i<T;i++)
        {
        cout<<"Case #"<<i+1<<": "<<output[i]<<"\n";
        }
}
