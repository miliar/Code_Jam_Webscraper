#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cassert>
using namespace std;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int main() {
	int t,c;
	cin>>t;
	for (c=1;c<=t;++c) {
		int m,n;
		cin>>m>>n;
		VVB f(m,VB(n));
		for (int i=0;i<m;++i) {
			string s;
			cin>>s;
			for (int j=0;j<n/4;++j) {
				char buf[2];
				buf[0]=s[j];
				buf[1]=0;
				int x;
				sscanf(buf,"%x",&x);
				for (int k=0;k<4;++k)
					f[i][j*4+k]=(x>>(3-k))&1;
			}
		}
		
		VVI right(m,VI(n));
		VVI down(m,VI(n));
		VVI g(m,VI(n));
		VVB v(m,VB(n,false));
		VPII sol;
		
		int mm=0;
		int s=m*n;
		while(1) {
			for (int i=0;i<m;++i) {
				int s=1;
				right[i][n-1]=1;
				if (v[i][n-1])
					right[i][n-1]=0;
				for (int j=n-2;j>=0;--j) {
					if ((f[i][j]!=f[i][j+1])&&!v[i][j+1])
						++s;
					else
						s=1;
					right[i][j]=s;
					if (v[i][j])
						right[i][j]=0;
				}
			}
			
			for (int j=0;j<n;++j) {
				int s=1;
				down[m-1][j]=1;
				if (v[m-1][j])
					down[m-1][j]=0;
				for (int i=m-2;i>=0;--i) {
					if ((f[i][j]!=f[i+1][j])&&!v[i+1][j])
						++s;
					else
						s=1;
					down[i][j]=s;
					if (v[i][j])
						down[i][j]=0;
				}
			}
			
			for (int i=0;i<m;++i)
				g[i][n-1]=1;
			for (int j=0;j<n;++j)
				g[m-1][j]=1;
			
			mm=0;
			for (int i=m-2;i>=0;--i) {
				for (int j=n-2;j>=0;--j) {
					if (v[i][j])
						continue;
					int x;
					if ((f[i+1][j+1]==f[i][j])&&!v[i+1][j+1])
						x=min(g[i+1][j+1]+1,min(down[i][j],right[i][j]));
					else
						x=1;
					g[i][j]=x;
					if (x>mm)
						mm=x;
				}
			}
			
			if (mm<=0)
				break;
			
			int kk=0;
			VVB vv(m,VB(n,false));
			for (int i=0;i<m;++i) {
				for (int j=0;j<n;++j) {
					if (v[i][j]||vv[i][j])
						continue;
					if (g[i][j]==mm) {
						for (int ii=0;ii<mm;++ii) {
							for (int jj=0;jj<mm;++jj) {
								assert(!v[i+ii][j+jj]);
								v[i+ii][j+jj]=true;
								if (j-jj>=0)
									vv[i+ii][j-jj]=true;
							}
						}
						s-=mm*mm;
						kk++;
					}
				}
			}
			
			sol.push_back(PII(mm,kk));
		}
		
		if (s)
			sol.push_back(PII(1,s));
		
		int x=-1;
		int y=0;
		VPII soll;
		for (int i=0;i<sol.size();++i) {
			if (sol[i].first==x) {
				y+=sol[i].second;
			} else {
				if (x>=0)
					soll.push_back(PII(x,y));
				x=sol[i].first;
				y=sol[i].second;
			}
		}
		soll.push_back(PII(x,y));
		
		cout<<"Case #"<<c<<": "<<soll.size()<<endl;
		for (int i=0;i<soll.size();++i) {
			cout<<soll[i].first<<' '<<soll[i].second<<endl;
		}
		
	}
	return 0;
}
