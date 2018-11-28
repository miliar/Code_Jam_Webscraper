#include<iostream>
#include<math.h>
using namespace std;
int main()
 { int t,tn=0,c,i,r[26][26],d,g[26][26],n,p[101],o[101],y,pr,fl,j;
   char ch,c1,c2,c3,cc,s[101];cin>>t;
   while(t--)
    {tn++;
     cin>>c;
     for(i=0;i<26;i++)for(j=0;j<26;j++){r[i][j]=0;g[i][j]=0;}
     for(i=0;i<c;i++) {cin>>s;c1=s[0]%65;c2=s[1]%65;c3=s[2]%65;r[c1][c2]=c3;r[c2][c1]=c3;}
     cin>>d;
     for(i=0;i<d;i++) {cin>>s;c1=s[0]%65;c2=s[1]%65;g[c1][c2]=1;g[c2][c1]=1;}
     cin>>n;cin>>s;
     for(i=0;i<n;i++){p[i]=s[i]%65;}
     o[0]=p[0];y=0; 
     for(i=1;i<n;i++) 
       { if(y<0){y=0;o[y]=p[i];continue;}
         c=p[i];pr=o[y];fl=0;
         if(r[c][pr]!=0){o[y]=r[c][pr];continue;}
         else if(d!=0){for(j=0;j<=y;j++)if(g[o[j]][c]){y=-1;fl=1;break;} }
         if(fl==0){y++;o[y]=c;}
       }
     cout<<"Case #"<<tn<<": [";for(i=0;i<y;i++){ch=o[i]+65;cout<<ch<<", ";}
     if(y>=0){ch=o[y]+65;cout<<ch;}cout<<"]"<<endl;
   }
    return 0;
 }
     
