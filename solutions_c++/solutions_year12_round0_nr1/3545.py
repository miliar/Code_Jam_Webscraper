#include<iostream>
#include<cstdio>
#include<string>
#include<cctype>
#include<map>

using namespace std;

int main()
{
    string c;int i;
string a="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string b="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
map<char,char>m;
for(i=0;i<a.length();i++)
{
m[a[i]]=b[i];
}
m['q']='z';
m['z']='q';
int t,ch=0;
cin>>t;
getchar();
while(t--)
{
          ch++;
getline(cin,c);
printf("Case #%d: ",ch);
for(i=0;i<c.length();i++)
{
printf("%c",m[c[i]]);
}
printf("\n");
}
return 0;
}

