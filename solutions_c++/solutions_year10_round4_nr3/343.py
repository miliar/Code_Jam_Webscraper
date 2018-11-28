#include <iostream>

using namespace std;

int main(){
	int TEST; cin >> TEST;
	for(int test=1;test<=TEST;test++){
		bool mp[2][251][251];
		memset(mp, false, sizeof(mp));
		int N; cin >> N;
		for(int i=0;i<N;i++){
			int x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
			for(int x=x1;x<=x2;x++)
				for(int y=y1;y<=y2;y++)
					mp[0][x][y] = true;
		}
		int ans = 0;
		for(ans=1; ;ans++){
			memset(mp[ans%2], false, sizeof(mp[0]));
			bool flag = true;
			for(int i=0;i<210;i++){
				for(int j=0;j<210;j++){
					if(mp[1-ans%2][i][j]){
						if((i!=0&&mp[1-ans%2][i-1][j])||(j!=0&&mp[1-ans%2][i][j-1])){
							mp[ans%2][i][j] = true;
							flag = false;
						}
					} else {
						if((i!=0&&mp[1-ans%2][i-1][j])&&(j!=0&&mp[1-ans%2][i][j-1])){
							mp[ans%2][i][j] = true;
							flag = false;
						}
					}
				}
			}
			if(flag) break;
		}
		printf("Case #%d: %d\n", test, ans);
	}
}
