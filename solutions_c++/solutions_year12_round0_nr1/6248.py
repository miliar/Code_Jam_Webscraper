#include<iostream>
#include<stdio.h>
#define SIZE 500
using namespace std;
void convert(char *strr,char *cvt)
{
int i;
char ref[30] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};//array
for(i=0;strr[i]!='\0';i++)
if(strr[i] == ' ') cvt[i] = ' ';
else cvt[i] = ref[(strr[i] - 97)];
cvt[i] = '\0';
}
int main()
{
int t;
char strr[SIZE],cvt[SIZE];
cin>>t;
cin.getline(strr,SIZE);
for(int tc=0;tc<t;tc++)
{
cin.getline(strr,SIZE);
convert(strr,cvt);
cout<<"Case #"<<tc+1<<':'<<' '<<cvt<<'\n';
}
return 0;
}
