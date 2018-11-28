#include <iostream>
#include <string>
#include <map>
#include <string.h>

using namespace std;
int L,D,n;
map<string,int> mp;
string st[510][20];
bool v[510][20][30];
string d[5010];
int num[5010];
int tot,ans=0;


int main()
{
    //freopen("p1.in","r",stdin);  
    freopen("A-large.in","r",stdin);
    freopen("p1.out","w",stdout);
    int kase,i,j,k;
    string s;
    //cin>>kase;
    //while(kase--) {
    memset(v,false,sizeof(v));
       tot=0;
       cin>>L>>D>>n;
       for(i=1;i<=D;i++) {
          cin>>d[i];
       }
       k=0;
       for(j=1;j<=n;j++) {
          k++;
          cin>>s;  string ts;  tot=0;
          for(i=0;i<s.length();i++) {
             if(s[i]=='(') {
                i++;  ts="";
                while(s[i]!=')') ts=ts+s[i],i++;
                st[j][tot++]=ts;
             }else st[j][tot++]=s[i];
          }//for         
       }
       for(i=1;i<=n;i++) 
          for(j=0;j<L;j++)
             for(k=0;k<st[i][j].length();k++) 
                v[i][j][st[i][j][k]-'a' ]=true;
       memset(num,0,sizeof(num));
       bool f;
       for(i=1;i<=D;i++) {
          for(j=1;j<=n;j++) {
             f=false;
             for(k=0;k<L;k++) {
                if(v[j][k][d[i][k]-'a']==false) {
                   f=true;
                   break;
                }
             }
             if(!f) num[j]++;
          }
       }
       for(i=1;i<=n;i++)
         cout<<"Case #"<<i<<": "<<num[i]<<endl;
    //}
    return 0;
}
