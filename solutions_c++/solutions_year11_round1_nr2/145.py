#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

int tt;
int n,m,r,mm;
vector<string> len[11];
string a[10000];
string p[10000];
bool posi[10];

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d%d\n",&n,&m);
		for (int i=0;i<=10;++i) len[i].clear();
		for (int i=0;i<n;++i) {
			string s;
			getline(cin,s);
			a[i]=s;
			len[s.size()].push_back(s);
		}

		printf("Case #%d:",ii);
		for (int i=0;i<m;++i) {
			int best=-1; string ans;
			string s;
			getline(cin,s);
			for (int j=0;j<n;++j) {
				mm=a[j].size();
				r=len[mm].size();
				for (int k=0;k<r;++k)
					p[k]=len[mm][k];
				int cnt=0;
				for (int k=0;k<26;++k) {
					bool flag=false;
					for (int l=0;l<r;++l)
						if (p[l].find(s[k])!=p[l].npos) {
							flag=true;
							break;
						}
					if (!flag) continue;
					if (a[j].find(s[k])!=a[j].npos) {
						int tmp=0;
						memset(posi,false,sizeof(posi));
						for (int l=0;l<mm;++l)
							if (a[j][l]==s[k]) posi[l]=true;
						for (int l=0;l<r;++l) {
							bool flag=true;
							for (int t=0;t<mm;++t)
								if ((p[l][t]==s[k]) ^ (posi[t])) {
									flag=false;
									break;
								}
							if (flag) p[tmp++]=p[l];
						}
						r=tmp;
					} else {
						int tmp=0;
						cnt++;
						for (int l=0;l<r;++l)
							if (p[l].find(s[k])==p[l].npos) p[tmp++]=p[l];
						r=tmp;
					}
				}
				if (cnt>best) {
					best=cnt;
					ans=a[j];
				}
			}
			cout << " " << ans;
		}
		cout << endl;
	}
}
