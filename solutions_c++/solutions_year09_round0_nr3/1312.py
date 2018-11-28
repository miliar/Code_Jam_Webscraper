#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<iomanip>

using namespace std;

int main()
{
char input[502];
long long int wel[20];
int i,j,testcases,testcount;
char c;

scanf("%d",&testcases);
getchar();
for(testcount=1;testcount<=testcases;testcount++)
{
for(i=0;i<20;i++)
wel[i]=0;

i=0;
while(scanf("%c",&c)!=EOF)
{
if(c==10)
break;
input[i++]=c;
}
input[i]=0;
//cout<<input;

int len=strlen(input);
wel[0]=1;
for(i=0;i<len;i++)
{
if(input[i]=='w')
{
wel[1]+=wel[0];

wel[1]=wel[1]%10000;
}
if(input[i]=='e')
{
wel[2]+=wel[1];
wel[7]+=wel[6];
wel[15]+=wel[14];

wel[2]=wel[2]%10000;
wel[7]=wel[7]%10000;
wel[15]=wel[15]%10000;
}
if(input[i]=='l')
{
wel[3]+=wel[2];

wel[3]=wel[3]%10000;
}
if(input[i]=='c')
{
wel[4]+=wel[3];
wel[12]+=wel[11];

wel[4]=wel[4]%10000;
wel[12]=wel[12]%10000;
}
if(input[i]=='o')
{
wel[5]+=wel[4];
wel[10]+=wel[9];
wel[13]+=wel[12];

wel[5]=wel[5]%10000;
wel[10]=wel[10]%10000;
wel[13]=wel[13]%10000;
}

if(input[i]=='m')
{
wel[6]+=wel[5];
wel[19]+=wel[18];

wel[6]=wel[6]%10000;
wel[19]=wel[19]%10000;}
if(input[i]==' ')
{
wel[8]+=wel[7];
wel[11]+=wel[10];
wel[16]+=wel[15];

wel[8]=wel[8]%10000;
wel[11]=wel[11]%10000;
wel[16]=wel[16]%10000;}
if(input[i]=='t')
{
wel[9]+=wel[8];
wel[9]=wel[9]%10000;
}
if(input[i]=='d')
{
wel[14]+=wel[13];
wel[14]=wel[14]%10000;
}
if(input[i]=='j')
{
wel[17]+=wel[16];
wel[17]=wel[17]%10000;
}
if(input[i]=='a')
{
wel[18]+=wel[17];
wel[18]=wel[18]%10000;
}

}

cout<<"Case #"<<testcount<<": ";
cout<<setw(4)<<setfill('0')<<wel[19]<<endl;
}
return 0;
}
