#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
using namespace std;

struct node {
	string s;
	int t[101];
};

node a[10001];

int n,m,i,j,l,x,p,nn,ans,testcase,test;
string str,s,sn[101],sm[101];

int exist(int p,string s) {
	for (int k=1; k<=a[p].t[0]; ++k)
		if (a[a[p].t[k]].s==s) return k;
	return -1;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>testcase;
	for (test=1; test<=testcase; ++test) {
		cin>>n>>m;
		for (i=1; i<=n; ++i) cin>>sn[i];
		for (i=1; i<=m; ++i) cin>>sm[i];
		sort(sn+1,sn+n+1);
		sort(sm+1,sm+m+1);
		a[0].t[0]=0;
		nn=0;
		for (i=1; i<=n; ++i) {
		    str=sn[i];
			p=0; s="";
			for (j=1; j<str.length(); ++j)
			    if (str[j]!='/') s+=str[j];
				else {
					if ((x=exist(p,s))!=-1) p=a[p].t[x];
					else {
						a[p].t[++a[p].t[0]]=++nn;
						p=nn;
						a[p].s=s;
						a[p].t[0]=0;
					}
					s="";
				}
			if ((x=exist(p,s))!=-1) p=a[p].t[x];
			else {
				a[p].t[++a[p].t[0]]=++nn;
				p=nn;
				a[p].s=s;
				a[p].t[0]=0;
			}
		}
		ans=0;
		for (i=1; i<=m; ++i) {
			str=sm[i];
			p=0; s="";
			for (j=1; j<str.length(); ++j)
				if (str[j]!='/') s+=str[j];
			    else {
					if ((x=exist(p,s))!=-1) p=a[p].t[x];
					else {
						++ans;
						a[p].t[++a[p].t[0]]=++nn;
						p=nn;
						a[p].s=s;
						a[p].t[0]=0;						
					}
					s="";
				}
			if ((x=exist(p,s))!=-1) p=a[p].t[x];
			else {
				++ans;
				a[p].t[++a[p].t[0]]=++nn;
				p=nn;
				a[p].s=s;
				a[p].t[0]=0;						
			}
		}
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
	return 0;
}