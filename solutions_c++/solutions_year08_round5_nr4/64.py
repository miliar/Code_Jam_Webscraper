
#include <iostream>
#include <vector>

#define MOD 10007

long long data[200][200];


using namespace std;
int main(void){
	int cases;
	cin >> cases;
	for(int case_no=1; case_no<=cases; case_no++){
		long long H,W,R;
		cin >> H >> W >> R;
		vector<pair<int,int> > rocks(R);
		memset(data, 0x00, sizeof(data));
		for(int i=0; i<R; i++){
			cin >> rocks[i].first >> rocks[i].second;
			data[rocks[i].first][rocks[i].second] = -1;
		}
		data[1][1] = 1;
		for(int y=1; y<=100; y++)
			for(int x=1; x<=100; x++){
				if(data[y][x] == -1) continue;
				if(data[y+2][x+1] != -1)
					data[y+2][x+1] =(data[y+2][x+1]+data[y][x])%MOD;
				if(data[y+1][x+2] != -1)
					data[y+1][x+2] =(data[y+1][x+2]+data[y][x])%MOD;
			}
		long long ans = data[H][W];
		cout << "Case #"<<case_no<<": " << ans << endl;
	}
	return 0;
}
