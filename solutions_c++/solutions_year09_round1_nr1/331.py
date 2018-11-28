#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <ctime>
 
using namespace std;

//int arr[10000000];
int bases[11];

char nos[]="0123456789";
int dp[10000000][11];

int main()
{
  int n,T;
  char str[100000];
  cin.getline(str,100);
  sscanf(str,"%d",&T);
  for(int tc=1;tc<=T;++tc)
  {
    cin.getline(str,100);
    stringstream ss;
    ss << str;
    int b,ind=0;
    while(ss>>b) {
	bases[ind++]=b;	
    }

int j;
   memset(dp,-1,sizeof dp);
    for(long long i=2;;++i)
    {
	bool ok=false;
	for(j=ind-1;j>=0;--j)
	{
		if (i<10000000) {
			if (dp[i][bases[j]]==0) break;
			else if (dp[i][bases[j]]==1) continue;
		}
		long long k=i;
		int x=0;
		map<long long,int> mp;	
	        b=bases[j];
		
		while(1)
		{
		//	cout<<"i=="<<i<<" k=="<<k<<" b=="<<b<<endl;
			x=0;
			while(k!=0)
			{
		   	    int p=k%b;
			    k/=b;
			   str[x++]=nos[p];	
			}
		      str[x]='\0';
		  //   cout<<"str=="<<str<<endl;
		      for(int m=x-1;m>=0;--m)
			 k+=(str[m]-'0')*(str[m]-'0');
		
		    // cout<<"k=="<<k<<endl;
		    				
		       if (k==1 || (k<10000000 && dp[k][b]==0)) break;
		       if(mp[k]==1) break;
		       else mp[k]=1;
		}
		//cout<<"BREAK\n";
		if (i<10000000)
		{
		if (k==1) {
			dp[i][b]=1;
			for(map<long long,int>::iterator it=mp.begin();it!=mp.end();++it)
				if (it->first < 10000000) dp[it->first][b]=1;
		}
		else {ok=false;
			for(map<long long,int>::iterator it=mp.begin();it!=mp.end();++it)
				if (it->first < 10000000)  dp[it->first][b]=0;
			dp[i][b]=0;break;}
		} else {

			if (k!=1) break;
		}
		mp.clear();	
	}
       if(j!=-1) continue;
       else {	//cout<<"DONE "<<i<<endl;
		cout<<"Case #"<<tc<<": "<<i<<endl;
		break;}
    }

  }
}
