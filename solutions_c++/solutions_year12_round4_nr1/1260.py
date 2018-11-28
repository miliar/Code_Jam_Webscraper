#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>

using namespace std;
const int MAX = 10100;

int n, casos, D, pos;
int d[MAX], l[MAX];
bool ans;

int main(){
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
	scanf(" %d", &n);
	for(int i=0;i<n;i++) scanf(" %d %d", &d[i], &l[i]);
	scanf(" %d", &D);

	ans = false;
	pos = 1;
	l[0] = d[0];
	for(int i=0;i<min(pos, n);i++){
		if(d[i]+l[i] >= D) ans = true;
		for(int j=pos;j<n;j++){
			if(d[i]+l[i] >= d[j]){
				l[j] = min(d[j]-d[i], l[j]);
				pos++;
			}
		}
	}
	printf("Case #%d: %s\n", inst, ans ? "YES" : "NO");
	}
	return 0;
}

