#include <iostream>
#include <fstream>

using namespace std;

int main()
{int n,n1,k,m;

string s[5],s1[5],x,y,z,w,p,q;
   ofstream file1("output.txt");
   ifstream file("A-large.in");
   file>>n;
   for(int j=1;j<=n;j++)
    {k=0;m=0;string p,q;
    for(int a=0;a<=3;a++)
        {file>>s[a];}
for(int b=0;b<=3;b++)
    {x=s[0][b];
     y=s[1][b];
     z=s[2][b];
     w=s[3][b];
     s1[b]=x+y+z+w;
     p=p+s[b][b];
     q=q+s[b][3-b];
    }
   if((p=="XXXX")||(p=="XXXT")||(p=="XXTX")||(p=="XTXX")||(p=="TXXX")||(q=="XXXX")||(q=="XXXT")||(q=="XXTX")||(q=="XTXX")||(q=="TXXX"))
    {file1<<"Case #"<<j<<": X won"<<"\n";k=1;
    }
    else
    {if((p=="OOOO")||(p=="OOOT")||(p=="OOTO")||(p=="OTOO")||(p=="TOOO")||(q=="OOOO")||(q=="OOOT")||(q=="OOTO")||(q=="OTOO")||(q=="TOOO"))
    {file1<<"Case #"<<j<<": O won"<<"\n";k=1;
    }
else{for(int i=0;i<=3;i++)
{
    if((s[i]=="XXXX")||(s[i]=="XXXT")||(s[i]=="XXTX")||(s[i]=="XTXX")||(s[i]=="TXXX")||(s1[i]=="XXXX")||(s1[i]=="XXXT")||(s1[i]=="XXTX")||(s1[i]=="XTXX")||(s1[i]=="TXXX"))
    {file1<<"Case #"<<j<<": X won"<<"\n";k=1;break;
    }
    else
    {if((s[i]=="OOOO")||(s[i]=="OOOT")||(s[i]=="OOTO")||(s[i]=="OTOO")||(s[i]=="TOOO")||(s1[i]=="OOOO")||(s1[i]=="OOOT")||(s1[i]=="OOTO")||(s1[i]=="OTOO")||(s1[i]=="TOOO"))
    {file1<<"Case #"<<j<<": O won"<<"\n";k=1;break;
    }}
}
}
}
if(k!=1)
{for(int i=0;i<=3;i++)
 for(int j=0;j<=3;j++)
 {if(s[i][j]=='.')
 {m++;break;}}
 if(m==0)
 {file1<<"Case #"<<j<<": Draw"<<"\n";}
 else
 {file1<<"Case #"<<j<<": Game has not completed"<<"\n";}}
}
}
