#define maxn 220
#include <iostream>
using namespace std;

int mp[maxn][maxn], sp[maxn][maxn];
int r, x1, y1, x2, y2, cnt;
int init(){
	memset(mp, 0, sizeof mp);
	scanf("%d", &r);
	cnt = 0;
	while (r--){
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int i=x1; i<=x2; i++)
			for (int j=y1; j<=y2; j++){
				if (!mp[j][i]) cnt++;
				mp[j][i] = 1;
			}
	}
}

int solve(int cas){
	int ans = 0;
	while (cnt>0){
//		cout<<"cnt:"<<cnt<<endl;
//		for (int i=1; i<=10; i++){
//			for (int j=1; j<=10; j++) cout<<mp[i][j]<<" ";
//			cout<<endl;
//		}
//		getchar();
		for (int i=1; i<=200; i++) {
			sp[1][i] = mp[1][i];
			sp[i][1] = mp[i][1];
		}
		for (int i=2; i<=200; i++)
			for (int j=2; j<=200; j++){
				sp[i][j] = mp[i][j];
				if (mp[i-1][j] && mp[i][j-1]) {
					if (!mp[i][j]) cnt++;
					sp[i][j] = 1;
				}
			}
		
//		for (int i=1; i<=10; i++){
//			for (int j=1; j<=10; j++) cout<<sp[i][j]<<" ";
//			cout<<endl;
//		}
//		cout<<"cnt1:"<<cnt<<endl;
		for (int i=1; i<=200; i++)
			for (int j=1; j<=200; j++)
				if (!(mp[i-1][j] || mp[i][j-1])){
					if (mp[i][j]) cnt--;
					sp[i][j]=0;
				}
//		cout<<"cnt2:"<<cnt<<endl;
		memcpy(mp, sp, sizeof sp);
		ans++;
	}
	printf("Case #%d: %d\n", cas, ans);
}		

int main(){
	int test; scanf("%d", &test);
	for (int cas=1; cas<=test; cas++){
		init();
		solve(cas);
	}
	return 0;
}
