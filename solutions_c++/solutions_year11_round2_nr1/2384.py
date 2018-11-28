#include<vector>
using namespace std;
main()
{
int te,n,i,j,cn=0,op;
double sum;
vector<string>s(100); 
cin>>te;
while(te--)
{
cn++;
cin>>n;
vector<double>avg(100);
vector<double>avg1(100);
vector<double>avg2(100);
vector<double>rpi(100);
vector<double>wint(100);
vector<double>play(100);
for(i=0;i<n;i++)
{
cin>>s[i];
}
for(i=0;i<n;i++)
{
int gam=0,win=0;
for(j=0;j<n;j++)
{
if(s[i][j]!='.')
gam++;
if(s[i][j]=='1')
win++;
}
wint[i]=win;
play[i]=gam;
avg[i]=(double)win/(double)gam;
}
//for(i=0;i<n;i++)
//cout<<avg[i]<<" ";
for(i=0;i<n;i++)
{
sum=0.0;
op=0;
for(j=0;j<n;j++)
{
if(s[i][j]!='.' && i!=j)
{
if(s[j][i]=='1')
{
sum+=((wint[j]-1)/(play[j]-1));
op++;
}
else if(s[j][i]=='0')
{
sum+=((wint[j])/(play[j]-1));
op++;
}
}
}
avg1[i]=sum/(double)op;
}
for(i=0;i<n;i++)
{
sum=0.0;
op=0;
for(j=0;j<n;j++)
{
if(s[i][j]!='.' && i!=j)
{
sum+=avg1[j];
op++;
}
}
avg2[i]=sum/(double)op;
}
for(i=0;i<n;i++)
rpi[i]=0.25 * avg[i] + 0.50 * avg1[i] + 0.25 * avg2[i];
cout<<"Case #"<<cn<<":"<<"\n";
for(i=0;i<n;i++)
cout<<rpi[i]<<"\n";
}
}