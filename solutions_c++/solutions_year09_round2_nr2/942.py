#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;
int main()
{
int nooftest,testc;
cin>>nooftest;
getchar();
for(testc=1;testc<=nooftest;testc++)
{
char c;
char d[23];
int m,n,i,j;
m=n=i=j=0;
c=11;


while(scanf("%c",&c)!=EOF)
{
if(c==10)
break;
d[i++]=c;
}

n=i;


for(i=n-1;i>=0;i--)
{
if(d[i]>d[i-1])
break;
}

m=i;


int swap,pos;
//now find min m->n
if(m>0)
{
pos=m;
swap=d[m];

for(i=m;i<n;i++)
if(swap>d[i]&&d[i]>d[m-1])
{
pos=i;swap=d[i];
}
d[pos]=d[m-1];
d[m-1]=swap;
for(i=m;i<n;i++)
for(j=m;j<n-1;j++)
if(d[j]>d[j+1])
{
swap=d[j];
d[j]=d[j+1];
d[j+1]=swap;
}
}
else
{

d[n]='0';
n++;
for(i=0;i<n;i++)
for(j=0;j<n-1;j++)
if(d[j]>d[j+1])
{
swap=d[j];
d[j]=d[j+1];
d[j+1]=swap;
}



}

for(i=0;i<n;i++)
{
if(d[i]!='0')
break;
}

swap=d[i];
d[i]='0';
d[0]=swap;

d[n]=0;
char answer[23];
strcpy(answer,d);
cout<<"Case #"<<testc<<": "<<answer<<endl;
}
return 0;

}
