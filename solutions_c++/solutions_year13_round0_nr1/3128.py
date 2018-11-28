#include<iostream>
#include<fstream>
using namespace std;
int main()
{
ifstream fin("A-large.in");
ofstream fout("output.txt");
char ch[4][4];
int ar[100],i,t,j,flag,p=0;
for(i=0;i<100;i++)
ar[i]=0;
fin>>t;
while(t--)
{
for(i=0;i<4;i++)
for(j=0;j<4;j++)
fin>>ch[i][j];
flag=0;
ar['.']=0;
for(i=0;i<4;i++)
{
    ar['X']=0;
    ar['O']=0;
    ar['T']=0;

    for(j=0;j<4;j++)
        ar[ch[i][j]]++;

    if((ar['X']+ar['T'])==4)
    {
     flag=1;
     break;
    }
    else if((ar['O']+ar['T'])==4)
    {
     flag=2;
     break;
    }

    ar['X']=0;
    ar['O']=0;
    ar['T']=0;

    for(j=0;j<4;j++)
        ar[ch[j][i]]++;

    if((ar['X']+ar['T'])==4)
    {
     flag=1;
     break;
    }
    else if((ar['O']+ar['T'])==4)
    {
     flag=2;
     break;
    }

    ar['X']=0;
    ar['O']=0;
    ar['T']=0;

    for(j=0;j<4;j++)
        ar[ch[j][j]]++;

    if((ar['X']+ar['T'])==4)
    {
     flag=1;
     break;
    }
    else if((ar['O']+ar['T'])==4)
    {
     flag=2;
     break;
    }

    ar['X']=0;
    ar['O']=0;
    ar['T']=0;

    for(j=0;j<4;j++)
        ar[ch[j][3-j]]++;

    if((ar['X']+ar['T'])==4)
    {
     flag=1;
     break;
    }
    else if((ar['O']+ar['T'])==4)
    {
     flag=2;
     break;
    }


}
p++;
if(flag==1)
fout<<"Case #"<<p<<": "<<"X won"<<endl;
else if(flag==2)
fout<<"Case #"<<p<<": "<<"O won"<<endl;
else if((flag==0)&&(ar['.']!=0))
fout<<"Case #"<<p<<": "<<"Game has not completed"<<endl;
else
fout<<"Case #"<<p<<": "<<"Draw"<<endl;


}
return 0;

}
