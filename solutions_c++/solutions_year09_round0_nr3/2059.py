#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <map>
#include <list>
#include <string>
using namespace std;

char s[502];
char tgt[70]="welcome to code jam";
//char tgt[70]="com";
int dp[100][502]; 

int rec(int ind,int pos)
{
  if (ind==strlen(tgt)) {
	return 1;
  } 
  if (s[pos]=='\0')
	return 0;
  //cout<<ind<<' '<<pos<<endl;
  if (dp[ind][pos] != -1) {
		//cout<<"ret ==" <<dp[ind][pos]<<endl;				
		return dp[ind][pos];
	}
  while (s[pos]!='\0' && tgt[ind]!=s[pos]) {++pos;}
   if (s[pos]=='\0') return 0;
  int ret=0;
  ret = rec(ind+1,pos+1)%10000;
  ret +=rec(ind,pos+1)%10000;
  dp[ind][pos]=ret;
  return ret;
}

int main()
{
int T,tc;
cin.getline(s,502);
sscanf(s,"%d",&T);
bool b = false;
 for(int tc=1;tc<=T;++tc)
  {
	cin.getline(s,502);
	memset(dp,-1,sizeof dp);
	rec(0,0);
	b=false;
	for(int i=0;i<strlen(s);++i)
		{			
		if (s[i]=='w') {
			char str[7];
			sprintf(str,"%d",dp[0][i]);
			string s1=str;
			while (s1.size()<4) s1="0"+s1;			
			cout<<"Case #"<<tc<<": "<<s1<<endl;
			b=true;
		 	break;		
		}
	}
	if (!b) cout<<"Case #"<<tc<<": "<<"0000"<<endl;
  }
}


