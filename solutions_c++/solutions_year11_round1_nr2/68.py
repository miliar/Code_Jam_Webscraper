#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <ctime>
#include <climits>
#include <cassert>
//#pragma comment(linker, "/STACK:640000000")
#ifdef _Win32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define next ksdjgsd
#define prev lsfnasd
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pi;
const ld E=1e-8;
const int inf=(int)1e9;

int mask[10010][26];
string s1[10010];
string s2[10010];
string res[10010];
int num[10010];
int can[10010];
vector<int> vi[1000010];
int may[1000010];
//int color[10010];
int p[10010];
int pc=0;
int ch;

inline bool comp(const int &x, const int &y){
	return mask[x][ch]<mask[y][ch];
}
inline bool comp2(const int &x, const int &y){
	return ((int)s1[x].size())<((int)s1[y].size());
}	 
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tn;
	scanf("%d", &tn);
	for(int tt=1;tt<=tn;tt++){
		cerr<<"new test "<<tt<<endl;
		int n, m;
		scanf("%d%d", &n, &m);
		for(int i=0;i<n;i++) cin>>s1[i];
		for(int i=0;i<m;i++) cin>>s2[i];
		for(int i=0;i<n;i++){
			for(int j=0;j<26;j++) mask[i][j]=0;
			for(int j=0;j<(int)s1[i].size();j++) mask[i][s1[i][j]-'a']|=1<<j;
		}
		for(int i=0;i<m;i++){
			cerr<<"new m "<<i<<endl;
			for(int j=0;j<n;j++) num[j]=0;
			int vic=0;
			int cc=0;
			for(int j=0;j<n;j++) p[j]=j;
			sort(p, p+n, comp2);
			vi[0].pb(p[0]);
			for(int j=1;j<n;j++){
				if(s1[p[j-1]].size()!=s1[p[j]].size()) cc++;
				vi[cc].pb(p[j]);
			}
			vic=cc+1;
            int st=0, en;
            for(int j=0;j<26;j++){
				ch=s2[i][j]-'a';
				en=vic;
				for(int i0=st;i0<en;i0++){
					if(vi[i0].size()==0) continue;
					pc=0;
					for(int j0=0;j0<(int)vi[i0].size();j0++) p[pc++]=vi[i0][j0];
					vi[i0].clear();
					int t=0;
					for(int j0=0;j0<pc && t==0;j0++) t|=mask[p[j0]][ch];
					if(t==0){
						for(int j0=0;j0<pc;j0++) vi[vic].pb(p[j0]);
						vic++;
						continue;
					}
					sort(p, p+pc, comp);
					for(int j0=0;j0<pc;j0++) if(mask[p[j0]][ch]==0) num[p[j0]]++;
					int cc=0;
					vi[vic].pb(p[0]);
					for(int j0=1;j0<pc;j0++){
						if(mask[p[j0-1]][ch]!=mask[p[j0]][ch]){
							cc++;
							if(vi[vic+cc].size()!=0){
								cerr<<"FAIL "<<vic<<endl;
								vi[vic+cc].clear();
							}
							if(vi[vic+cc].size()!=0){
								cerr<<"FAIL "<<vic<<endl;
								vi[vic+cc].clear();
							}
						}
						vi[vic+cc].pb(p[j0]);
					}
					vic+=cc+1;
				}
				st=en;
			}
			for(int j=0;j<vic;j++) if(vi[j].size()!=0){
				vi[j].clear();
				//cerr<<j<<" "<<vic<<endl;
			}
			//for(int j=0;j<n;j++) cerr<<num[j]<<" ";
			//cerr<<endl;
			cc=0;
			for(int j=1;j<n;j++) if(num[j]>num[cc]) cc=j;
			res[i]=s1[cc];
		}
		/*for(int i=0;i<m;i++){
			for(int k0=0;k0<n;k0++){
				for(int k=0;k<n;k++){
					if(s1[k0].size()==s1[k].size()) can[k]=1;
					else can[k]=0;
				}
				int pp=0;
				for(int j=0;j<26;j++){
				    int t=0;
					for(int k=0;k<n && t==0;k++) if(can[k]) t|=mask[k][s2[i][j]-'a'];
					if(t>0){
						if(mask[k0][s2[i][j]-'a']==0) pp++;
						for(int k=0;k<n;k++) if(mask[k][s2[i][j]-'a']!=mask[k0][s2[i][j]-'a']) can[k]=false;
					}
				}
				num[k0]=pp;
			}
			//for(int j=0;j<n;j++) cerr<<num[j]<<" ";
			//cerr<<endl;
			int cc=0;
			for(int k=1;k<n;k++) if(num[k]>num[cc]) cc=k;
			res[i]=s1[cc];
		}*/
		printf("Case #%d:", tt);
		for(int i=0;i<m;i++) cout<<" "<<res[i];
		cout<<endl;
	}
	return 0;
}
