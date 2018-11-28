#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

bool mat[2][110][110];

int main(){
	int tc, i, j, r, x1, x2, y1, y2, cnt, ans, k;
	cin>>tc;
	for(k=1; k<=tc; k++){
		cin>>r;
		memset(mat, false, sizeof(mat));
		cnt = 0;
		while(r--){
			cin>>x1>>y1>>x2>>y2;
			if(x1>x2)swap(x1, x2);
			if(y1>y2)swap(y1, y2);
			for(i=x1; i<=x2; i++){
				for(j=y1; j<=y2; j++){
					mat[0][i][j] = true;
				}
			}
		}
		for(i=1; i<110; i++){
			for(j=1; j<110; j++){
				if(mat[0][i][j])
					cnt++;
			}
		}
		//cout<<cnt<<endl;
		ans = 0;
		while(cnt){
			for(i=1; i<110; i++){
				for(j=1; j<110; j++){
					if(mat[ans%2][i][j]){
						if(!mat[ans%2][i-1][j] && !mat[ans%2][i][j-1]){
							mat[(ans+1)%2][i][j] = false;
							cnt--;
						} else{
							mat[(ans+1)%2][i][j] = true;
						}
					} else {
						if(mat[ans%2][i-1][j] && mat[ans%2][i][j-1]){
							mat[(ans+1)%2][i][j] = true;
							cnt++;
						} else {
							mat[(ans+1)%2][i][j] = false;
						}
					}
				}
			}
			ans++;
			//cout<<ans<<endl;
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}

