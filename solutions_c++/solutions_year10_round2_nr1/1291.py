#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
int T,t;
int n,m,i,ans,maxl,mj,w,j,nn;
string ns[10000],ms[100],ts,tt;
bool r;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			cin>>ns[i];
		nn=n;
		for(i=0;i<n;i++)
		{
			ts=ns[i];
			r=false;
			while (ts.length()>0)
			{
				if (r==false) tt="/";
				else tt=ns[nn-1]+"/";
				r=true;
				ts.erase(0,1);
				w=ts.find("/");
				if (w==-1) break;
				tt=tt+ts.substr(0,w);
				ts.erase(0,w);
				ns[nn++]=tt;
			}
		}
		n=nn;
		ns[n++]="";
		sort(ns,ns+n);
		ans=0;
		for(i=0;i<m;i++)
		{
			cin>>ms[i];
			r=false;
			for(j=0;j<n;j++)
				if (ns[j]==ms[i]||ns[j].find(ms[i])==0&&ns[j][ms[i].length()]=='/') 
				{
					r=true;
					break;
				}
			if (r) continue;
			for(maxl=0,mj=0,j=0;j<n;j++)
				if (ms[i]==ns[j]||(ms[i].find(ns[j])==0&&ms[i][ns[j].length()]=='/')&&ns[j].length()>maxl)
					maxl=ns[j].length(),mj=j;
			ts=ms[i];
			ts.erase(0,maxl);
			r=false;
			while (ts.length()>0)
			{
				ts.erase(0,1);
				w=ts.find("/");
				if (w==-1) w=ts.length();
				if (r) mj=n-1;
				r=true;
				tt=ns[mj]+"/"+ts.substr(0,w);
				ts.erase(0,w);
				ns[n++]=tt;
				ans++;
			}
			sort(ns,ns+n);
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}