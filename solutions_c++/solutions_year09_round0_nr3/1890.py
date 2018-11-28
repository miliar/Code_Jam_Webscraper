#include<iostream>
using namespace std;

int n,i,j,ile,wsk,res;
string s,pattern;
char c;

void rec(int ile, int poz)
{
int i;
if(ile==19) {++res; goto m;}
for(i=poz; i<s.length(); ++i)
     if(s[i]==pattern[ile]) rec(ile+1,i+1);
m:;
}

int main()
{
cin >> n;
getchar();
pattern="welcome to code jam";

for(i=1; i<=n; ++i)
     {
     s="";
     res=0;
     while(1){c=getchar(); if(c=='\n' || c==EOF) break; s+=c;}
     printf("Case #%d: ",i);
     if(s.length()<19) {printf("0000\n"); continue;}
     rec(0,0);
     if(res<10) {printf("000"); printf("%d\n",res); continue;}
     if(res<100) {printf("00"); printf("%d\n",res); continue;}
     if(res<1000) {printf("0"); printf("%d\n",res); continue;}
     printf("%d\n",res);
     }

return 0;
}
