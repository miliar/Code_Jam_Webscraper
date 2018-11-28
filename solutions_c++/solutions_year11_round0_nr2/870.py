#include <iostream>
using namespace std;
int comb[256][256];
int kcomb[256][256];
char str[200];
char xout[200];
int destructive[256];
void idestr(int k,int f=1)
{
for(int i='A';i<='Z';i++)
if(kcomb[k][i]=='+')destructive[i]+=f;
}
int main()
{
ios_base::sync_with_stdio(0);
int t;
cin >> t;
for(int cn=1;cn<=t;cn++)
{
int c,i,j;
for(i=0;i<255;i++)for(j=0;j<255;j++)comb[i][j]=kcomb[i][j]=0;
cin >> c;
for(i=0;i<c;i++){cin>>str;comb[str[0]][str[1]]=str[2];comb[str[1]][str[0]]=str[2];}
int d;
cin >> d;
for(i=0;i<d;i++){cin>>str;kcomb[str[0]][str[1]]='+';kcomb[str[1]][str[0]]='+';}
int n;
cin >> n;
cin >> str;
int xptr=0;
for(j=0;j<256;j++)destructive[j]=0;
for(i=0;i<n;i++)
{
if(xptr==0)
{
xout[xptr++] = str[i];
idestr(str[i]);
continue;
}
int q = comb[xout[xptr-1]][str[i]];
if(!q && destructive[str[i]])
{
xptr=0;
for(j=0;j<256;j++)destructive[j]=0;
continue;
}
if(q)
{
idestr(xout[xptr-1],-1);
xout[xptr-1] = q;
idestr(q);
}
else
{
xout[xptr++] = str[i];
idestr(str[i]);
}
xout[xptr]=0;
}
cout << "Case #"<<cn << ": [";
for(i=0;i<xptr;i++)cout<<xout[i]<<(i==xptr-1?"":", ");
cout<<"]"<<endl;
}
return 0;
}
