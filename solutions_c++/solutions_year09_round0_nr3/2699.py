#include<iostream>
#include<string.h>
#include<ctype.h>
using namespace std;
int searc(char *line, int i, char a)
{
//cout<<"Searching: "<<a<<" in "<<i;
for(i;i<strlen(line);i++)
if(line[i]==a)
return i;
return -1;
}
int post[19];
main()
{
int i,j,k,l,n,cnt=0,len,ii,t=0;
char st[]="welcome to code jam";
char c;
char line[501];
cin>>n;
//cin>>c;
c=getchar();
string abc;
while(n--)
{
t++;
cnt=0;
ii=0;
//cin>>c;
//scanf("%s[^\n]",line);
getline(cin,abc);
for(ii=0;abc[ii]!='\0';ii++)
line[ii]=abc[ii];
line[ii]='\0';
//cin>>c
//cout<<c;
//c=getchar();
//while(c!='\n')
//{
//cout<<c<<endl;
//line[ii++]=c;
//cin>>c;
//}
//cout<<"Done";
//cin>>line;
//line[ii]='\0';
len=strlen(line);
//cout<<len;
//printf("\n%s",line);
//printf("\n%s\n",st);
//cin>>c;
k=0;
for(i=0;i<19;i++)
post[i]=len;
//cout<<"Lenght is len: "<<len<<endl;
for(i=0;i<len;i++)
{
i=searc(line,i,st[k]);
//cout<<" Found at: "<<i<<endl;
if(i==len-1)
{
if(k==18)
{
post[k]=i;
cnt++;
//cout<<endl;
//for(ii=0;ii<19;ii++)
//cout<<post[ii]<<" ";
//cout<<endl;
cnt%=10000;
}
if(k!=0)
{
i=post[k-1];
k--;
}
}
else if(i==-1)
{
if(post[k]!=len)
{
if(k!=0)
{
i=post[k-1];
k--;
}
else break;
}
else break;
}
else
{
post[k]=i;
if(k==18)
{
cnt++;
//for(ii=0;ii<19;ii++)
//cout<<post[ii]<<" ";
//cout<<endl;
cnt%=10000;
//cout<<"Here"<<k<<" "<<i;
//i=post[k-1];
//k--;
}
else k++;
}
}
printf("Case #%d: %04d\n",t,cnt);
}
}
