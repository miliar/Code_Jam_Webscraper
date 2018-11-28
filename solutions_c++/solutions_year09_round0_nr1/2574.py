#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<algorithm>
#include<functional>
#include<utility>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdio>
#include<ctime>
#include<string>
using namespace std;
vector<string>rs;
map<string,int>my;
int p[20];
int re=0;
int L,D,N;
map<string,int>::iterator q;
void back(int t)
{
	int i;
	if(t>L-1)
	{
		string tt;
      for(i=0;i<L;i++)
           tt+=rs[i][p[i]];
	  if(my[tt])
		  re++;
	  return;
	}
	for(i=0;i<rs[t].size();i++)
	{
		p[t]=i;
		string s;
		int j;
		for(j=0;j<=t;j++)
	     s+=rs[j][p[j]];
		for(q=my.begin();q!=my.end();q++)
		{	
			if(q->first.substr(0,t+1)==s)
				break;
		}
		if(q!=my.end())
		  back(t+1);
	}
}
int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
    cin>>L>>D>>N;
    int i,j,kth=1;
	string str;
	my.clear();
	for(i=0;i<D;i++)
	{
		cin>>str;
		my[str]=1;
	}
	for(i=0;i<N;i++)
	{
		re=0;
		cin>>str;
		string t;
		int len=str.length();
		int biao=0,b=0;
		rs.clear();
	    rs.resize(20);
		for(j=0;j<len;j++)
		{
			if(biao==1&&str[j]!=')')
			{
             t+=str[j];
			}
            else if(str[j]=='(')
		    {
			  biao=1;
			  continue;
		    }
		    else if(str[j]==')')
		    {
               biao=0;
               rs[b]=t;
			   t="";
			   b++;
		    }
			else
			{
               t+=str[j];
			   rs[b]=t;
			   t="";
			   b++;
			}
		}
      memset(p,0,sizeof(p));
	  back(0);
      printf("Case #%d: %d\n",i+1,re);

	} 
	return 0;
}

