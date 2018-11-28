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

int a[100][100];
int b[100][100];
int m=26;
char s0[1010];
int res[1010];
int resc=0;
int has[100];
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tt=0;tt<t;tt++){
		for(int i=0;i<m;i++) for(int j=0;j<m;j++) a[i][j]=0;
		for(int i=0;i<m;i++) for(int j=0;j<m;j++) b[i][j]=0;
		for(int i=0;i<m;i++) has[i]=0;
		resc=0;
		int c;
		scanf("%d", &c);
		char s[10];
		for(int i=0;i<c;i++){
			scanf("%s", s);
			int x=s[0]-'A';
			int y=s[1]-'A';
			int z=s[2]-'A';
			a[x][y]=z;
			a[y][x]=z;
			if(z==0) cerr<<"Fail!\n";
		}
		int d;
		scanf("%d", &d);
		for(int i=0;i<d;i++){
			scanf("%s", s);
			int x=s[0]-'A';
			int y=s[1]-'A';
			b[x][y]=1;
			b[y][x]=1;
		}
		int n;
		scanf("%d%s", &n, s0);
		for(int i=0;i<n;i++){
			if(resc==0){
				res[resc++]=s0[i]-'A';
				has[s0[i]-'A']++;
			}else{
				int x=s0[i]-'A';
				if(a[res[resc-1]][x]>0){
					has[res[resc-1]]--;
					res[resc-1]=a[res[resc-1]][x];
				}else{
					bool op=false;
					for(int i=0;i<m && !op;i++) if(has[i]>0 && b[i][x]==1) op=true;
					if(op){
						resc=0;
						for(int i=0;i<m;i++) has[i]=0;
					}else{
						res[resc++]=x;
						has[x]++;
					}
				}
			}
		}
		printf("Case #%d: ", tt+1);
		if(resc==0) printf("[]\n");
		else{
			printf("[%c", (char)res[0]+'A');
			for(int i=1;i<resc;i++) printf(", %c", (char)res[i]+'A');
			printf("]\n");
		}
	}		
	return 0;
}
