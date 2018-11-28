#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string.h>
#include <stdlib.h>
using namespace std;

short int g[6000][6000];


int main()
{
int tc;
cin>>tc;
char s[1000];

for(int t=1;t<=tc;++t)
{
int n,m;
cin>>n>>m;
int c=2;
map<string,int> mp;
mp.clear();
mp["//"]=1;

memset(g,-1,sizeof g);

for(int i=0;i<n;++i)
  {  
     cin>>s; int l = strlen(s);
	s[l] = '/';s[l+1]='\0';
     int par=1;
     string p;
     const char *tok = strtok(s,"/");
     while(tok!=NULL) {
      
         p+=string(tok)+"/";
    //     cout<<p<<endl;
	if (mp[p]==0)
		mp[p] = c++;
        int cur = mp[p];	
	g[par][cur]=1;
	par=cur;
        tok = strtok(NULL,"/");
     }	
  }
int ans=0;
for(int i=0;i<m;++i) {
  cin>>s; int l=strlen(s);
	s[l] = '/';s[l+1]='\0';
  int par=1;
  string p;
  const char *tok = strtok(s,"/");
   while(tok!=NULL) {
     p+=string(tok)+"/";
//	cout<<p<<endl;
     // cout<<tok<<' ';
      if (mp[p]==0) {
		mp[p] = c++;
      }
      int cur = mp[p];
      if (g[par][cur]==-1) ++ans;
      g[par][cur] = 1; 
      par = cur;
      tok = strtok(NULL,"/");
   }
}

cout<<"Case #"<<t<<": "<<ans<<endl;
}

}
