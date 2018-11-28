#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
main()
{
  int t;
  cin>>t;
  for(int x=0;x<t;x++)
  {
    int n;
    char r;
    int p;
    vector<int> R;
    vector<vector<int> > P(2,vector<int>());
    cin>>n;
    for(int i=0;i<n;i++)
    {
	cin>>r>>p;
	r=='O'?R.push_back(0):R.push_back(1);
	r=='O'?P[0].push_back(p):P[1].push_back(p);
    }
    int cur[]={1,1};
    int a,b;
    int sum=0;
    for(int i=0;i<R.size();i++)
    {
	R[i]==0?(a=0,b=1):(a=1,b=0);
	int step=int(abs(float(P[a][0]-cur[a])))+1;
	int need=(P[b].size()==0?0:P[b][0]-cur[b]);
        cur[a]=P[a][0];
	if(int(abs(float(need)))<=step)
	{     if(P[b].size())cur[b]=P[b][0];}
	else if(need>0)
	     cur[b]+=step;
	else
	     cur[b]-=step;
	sum+=step;
	P[a].erase(P[a].begin());
    }
    cout<<"Case #"<<x+1<<": "<<sum<<endl;
  }
}
