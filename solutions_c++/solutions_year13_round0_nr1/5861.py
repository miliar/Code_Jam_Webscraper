#include <cstdio>
#include <string>
using namespace std;
int n = 4;
char a[11][11];
int ans = 0;
string c[4] = {"Game has not completed","O won","X won","Draw",};
bool oo(char t1, char t2, char t3, char t4) {
	if (t1=='.' || t2=='.' || t3=='.' || t4=='.') return false;
	if (t1=='X' || t2=='X' || t3=='X' || t4=='X') return false;
	return true;
}
bool xx(char t1, char t2, char t3, char t4) {
	if (t1=='.' || t2=='.' || t3=='.' || t4=='.') return false;
	if (t1=='O' || t2=='O' || t3=='O' || t4=='O') return false;
	return true;
}
int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int tc=1; tc<=t; tc++) {
		for (int i=0; i<n; i++) {
			scanf("%s",a[i]);
		}
		int x=0;
		int o=0;
		for (int i=0; i<n; i++) {
			if (oo(a[i][0],a[i][1],a[i][2],a[i][3]))
				o=1;
			if (xx(a[i][0],a[i][1],a[i][2],a[i][3]))
				x=1;
			if (oo(a[0][i],a[1][i],a[2][i],a[3][i]))
				o=1;
			if (xx(a[0][i],a[1][i],a[2][i],a[3][i]))
				x=1;
		}
		if (oo(a[0][0],a[1][1],a[2][2],a[3][3])) o=1;
		if (xx(a[0][0],a[1][1],a[2][2],a[3][3])) x=1;
		if (oo(a[0][3],a[1][2],a[2][1],a[3][0])) o=1;
		if (xx(a[0][3],a[1][2],a[2][1],a[3][0])) x=1;
		ans=2*x+o;
		if (ans == 0 || ans == 3) {
			bool cc=false;
			for (int i=0; i<n; i++) {
				for (int j=0; j<n; j++) {
					if (a[i][j] == '.') cc=true;
				}
			}
			if (cc) ans = 0;
			else ans = 3;
		}
		printf("Case #%d: %s\n",tc,c[ans].c_str());
	}
	return 0;
}