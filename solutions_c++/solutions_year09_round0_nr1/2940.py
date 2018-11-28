#include<iostream>
#include<string.h>

using namespace std;


int isthere(char,int,int,char *);

int main()
{
int L,D,N,i,j,y,k,m;
cin>>L;
cin>>D;
cin>>N;
char word[D][L];
char msg[N][1000];
for(i=0;i<D;i++)
{
cin>>word[i];
}
for(i=0;i<N;i++)
{
cin>>msg[i];
}
for(y=0;y<N;y++)
{
int len=strlen(msg[y]);
int l=0;
int store[L][2];
for(i=0;i<len;i++)
{
if(msg[y][i]=='(')
{
j=i+1;
while(msg[y][j]!=')'){j++;}

store[l][0]=i+1;
store[l][1]=j-1;

l++;
i=j;
}
else
   {store[l][0]=i;store[l++][1]=i;}
}

int x,count=0;
for(i=0;i<D;i++)
{
for(j=0;j<L;j++)
{
x=isthere(word[i][j],store[j][0],store[j][1],msg[y]);
if(x==0) break;
}
if(x==1)
count++;
}

cout<<"Case #"<<y+1<<": "<<count<<endl;
}

return 0;
}


int isthere(char a,int p0,int p1,char msg[])
{
int i;
for(i=p0;i<=p1;i++)
{
if(msg[i]==a) return(1);
}
return(0);
}
