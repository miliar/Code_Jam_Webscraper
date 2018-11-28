#include<iostream>
#include<fstream>


using namespace std;

ifstream fin("a-small.in");
ofstream fout("a-small.out");


class snaper
{
public:
int rp,on,off,sp;
};

int snapping(int n, int k)
{

snaper s[90][1000];
int i,j;
for(i=1;i<=n;i++)
{
for(j=0;j<=k;j++)
{
s[i][j].rp=0;
s[i][j].on=0;
s[i][j].off=1;
s[i][j].sp=0;
}
}
for(j=0;j<=k;j++)
{
                 s[1][j].rp=1;
}


// snapping//
for(j=1;j<=k;j++)
{
s[1][j].on=!s[1][j-1].on;
s[1][j].off=!s[1][j-1].off;
s[1][j].sp=!s[1][j-1].sp;

for(i=2;i<=n;i++)
{
                 if(s[i-1][j].sp==1)
                 {
                 s[i][j].rp=1;
                 }
                 else
                 {
                 s[i][j].rp=0;
                 }

                 if(s[i][j-1].rp==1)
                 {
                 s[i][j].on=!s[i][j-1].on;
                 s[i][j].off=!s[i][j-1].off;
                 }
                 else{
                 s[i][j].on=s[i][j-1].on;
                 s[i][j].off=s[i][j-1].off;
                 }

                 s[i][j].sp=(s[i][j].rp*s[i][j].on);
}
}

if(s[n][k].sp==1)
{
return 1;
}
else { return 0;}
}

int main()
{
double noc,i;
int a,b;
int result;
fin>>noc;
for( i=1;i<=noc;i++)
{
fin>>a>>b;
result=snapping(a,b);
fout<<"Case #"<<i<<": ";
if(result==1)
{
fout<<"ON"<<endl;
}
else
fout<<"OFF"<<endl;
}

return 0;
}





