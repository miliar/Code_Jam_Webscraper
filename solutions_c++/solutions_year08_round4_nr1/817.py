#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
using namespace std;
int main()
{
	int tc,i,j,k,l,n;
	int d;
	vector<int> g,c;
	vector<long long> ans;
	vector<vector<bool> > vis;
	vector<vector<int> > stp;
	cin>>tc;
	for(i=0;i<tc;i++)
	  {
	    cin>>n>>d;
	    for(j=0;j<n;j++)
	      {
		if(j<(n-1)/2)
		  {
		    cin>>k>>l;
		    c.push_back(l);
		  }
		else
		  cin>>k;
		g.push_back(k);
		vector<int> st;
		st.push_back(100000);
		st.push_back(100000);
		stp.push_back(st);
	      }
	    for(j=(n-1)/2;j<n;j++)
	      {
		if(g[j]==1)
		  stp[j][1]=0;
		if(g[j]==0)
		  stp[j][0]=0;
	      }
	    for(j=((n-1)/2)-1;j>=0;j--)
	      {
		if(g[j]==1)
		  {
		    if(stp[2*(j+1)-1][0]<10000 && stp[2*(j+1)][0]<10000)
		      if(stp[j][0]>stp[2*(j+1)-1][0]+stp[2*(j+1)][0])
			  stp[j][0]=stp[2*(j+1)-1][0]+stp[2*(j+1)][0];
		    if(stp[2*(j+1)-1][1]<10000 && stp[2*(j+1)][0]<10000)
			if(stp[j][0]>stp[2*(j+1)-1][1]+stp[2*(j+1)][0])
			  stp[j][0]=stp[2*(j+1)-1][1]+stp[2*(j+1)][0];				    if(stp[2*(j+1)-1][0]<10000 && stp[2*(j+1)][1]<10000)
			if(stp[j][0]>stp[2*(j+1)-1][0]+stp[2*(j+1)][1])
			  stp[j][0]=stp[2*(j+1)-1][0]+stp[2*(j+1)][1];
		    if(stp[2*(j+1)-1][1]<10000 && stp[2*(j+1)][1]<10000)
			if(stp[j][1]>stp[2*(j+1)-1][1]+stp[2*(j+1)][1])
			  stp[j][1]=stp[2*(j+1)-1][1]+stp[2*(j+1)][1];
		  }
		if(g[j]==0)
		  {
		    if(stp[2*(j+1)-1][0]<10000 && stp[2*(j+1)][0]<10000)
			if(stp[j][0]>stp[2*(j+1)-1][0]+stp[2*(j+1)][0])
			  stp[j][0]=stp[2*(j+1)-1][0]+stp[2*(j+1)][0];
		    if(stp[2*(j+1)-1][1]<10000 && stp[2*(j+1)][0]<10000)
			if(stp[j][1]>stp[2*(j+1)-1][1]+stp[2*(j+1)][0])
			  stp[j][1]=stp[2*(j+1)-1][1]+stp[2*(j+1)][0];				    if(stp[2*(j+1)-1][0]<10000 && stp[2*(j+1)][1]<10000)
			if(stp[j][1]>stp[2*(j+1)-1][0]+stp[2*(j+1)][1])
			  stp[j][1]=stp[2*(j+1)-1][0]+stp[2*(j+1)][1];
		    if(stp[2*(j+1)-1][1]<10000 && stp[2*(j+1)][1]<10000)
			if(stp[j][1]>stp[2*(j+1)-1][1]+stp[2*(j+1)][1])
			  stp[j][1]=stp[2*(j+1)-1][1]+stp[2*(j+1)][1];
		  }
		if(c[j]==1 && g[j]==1)
		  {
		    if(stp[2*(j+1)-1][0]<10000 && stp[2*(j+1)][0]<10000)
		      if(stp[j][0]>stp[2*(j+1)-1][0]+stp[2*(j+1)][0])
			  stp[j][0]=stp[2*(j+1)-1][0]+stp[2*(j+1)][0];
		    if(stp[2*(j+1)-1][1]<10000 && stp[2*(j+1)][0]<10000)
			if(stp[j][0]>stp[2*(j+1)-1][1]+stp[2*(j+1)][0])
			  stp[j][0]=stp[2*(j+1)-1][1]+stp[2*(j+1)][0];  			    if(stp[2*(j+1)-1][0]<10000 && stp[2*(j+1)][1]<10000)
			if(stp[j][0]>stp[2*(j+1)-1][0]+stp[2*(j+1)][1])
			  stp[j][0]=stp[2*(j+1)-1][0]+stp[2*(j+1)][1];
		    if(stp[2*(j+1)-1][1]<10000 && stp[2*(j+1)][0]<10000)
			if(stp[j][1]>stp[2*(j+1)-1][1]+stp[2*(j+1)][0]+1)
			  stp[j][1]=stp[2*(j+1)-1][1]+stp[2*(j+1)][0]+1;			    if(stp[2*(j+1)-1][0]<10000 && stp[2*(j+1)][1]<10000)
			if(stp[j][1]>stp[2*(j+1)-1][0]+stp[2*(j+1)][1]+1)
			  stp[j][1]=stp[2*(j+1)-1][0]+stp[2*(j+1)][1]+1;
		    if(stp[2*(j+1)-1][1]<10000 && stp[2*(j+1)][1]<10000)
			if(stp[j][1]>stp[2*(j+1)-1][1]+stp[2*(j+1)][1])
			  stp[j][1]=stp[2*(j+1)-1][1]+stp[2*(j+1)][1];
		  }
		if(c[j]==1 && g[j]==0)
		  {
		    if(stp[2*(j+1)-1][0]<10000 && stp[2*(j+1)][0]<10000)
		      if(stp[j][0]>stp[2*(j+1)-1][0]+stp[2*(j+1)][0])
			  stp[j][0]=stp[2*(j+1)-1][0]+stp[2*(j+1)][0];
		    if(stp[2*(j+1)-1][1]<10000 && stp[2*(j+1)][0]<10000)
			if(stp[j][0]>stp[2*(j+1)-1][1]+stp[2*(j+1)][0]+1)
			  stp[j][0]=stp[2*(j+1)-1][1]+stp[2*(j+1)][0]+1;			    if(stp[2*(j+1)-1][0]<10000 && stp[2*(j+1)][1]<10000)
			if(stp[j][0]>stp[2*(j+1)-1][0]+stp[2*(j+1)][1]+1)
			  stp[j][0]=stp[2*(j+1)-1][0]+stp[2*(j+1)][1]+1;
		    if(stp[2*(j+1)-1][1]<10000 && stp[2*(j+1)][0]<10000)
			if(stp[j][1]>stp[2*(j+1)-1][1]+stp[2*(j+1)][0])
			  stp[j][1]=stp[2*(j+1)-1][1]+stp[2*(j+1)][0];        		    if(stp[2*(j+1)-1][0]<10000 && stp[2*(j+1)][1]<10000)
			if(stp[j][1]>stp[2*(j+1)-1][0]+stp[2*(j+1)][1])
			  stp[j][1]=stp[2*(j+1)-1][0]+stp[2*(j+1)][1];
		    if(stp[2*(j+1)-1][1]<10000 && stp[2*(j+1)][1]<10000)
			if(stp[j][1]>stp[2*(j+1)-1][1]+stp[2*(j+1)][1])
			  stp[j][1]=stp[2*(j+1)-1][1]+stp[2*(j+1)][1];
		  }
	      }
	    if(stp[0][d]<10000)
	      ans.push_back(stp[0][d]);
	    else
	      ans.push_back(-1);
	    stp.erase(stp.begin(),stp.end());
	    g.erase(g.begin(),g.end());
	    c.erase(c.begin(),c.end());
	  }
	for(i=0;i<ans.size();i++)
	  {
	    if(ans[i]==-1)
		cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
	    else
		cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
	  }
	return 0;
}
