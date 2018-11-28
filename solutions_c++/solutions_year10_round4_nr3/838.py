#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>

using namespace std;

char tab[123][123];

typedef pair<int, int> pii;

int main(void){
	int N;
	cin >> N;
	for(int cas=1; cas <= N; cas++){
		memset(tab,0,sizeof(tab));
		int n;
		cin >> n;
		for(int i = 0; i < n; i++){
			int x1,y1,x2,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for(int x = x1; x <= x2; x++){
				for(int y = y1; y <= y2; y++){
					tab[y][x] = 1;
				}
			}
		}
		int res = 0;
		bool alive=true;

		while(alive){
			res++;
			alive = false;
			for(int x = 1; x < 110; x++){
				for(int y = 1; y < 110; y++){
					if(tab[y][x] == 1){
						if(!tab[y-1][x] && !tab[y][x-1]){
							tab[y][x] = 2;
						} else {
							alive = true;
						}
					}
				}
			}

			for(int x = 1; x < 110; x++){
				for(int y = 1; y < 110; y++){
					if(tab[y][x] == 0){
						if((tab[y-1][x] == 1 || tab[y-1][x] == 2)  && 
							(tab[y][x-1] == 1 || tab[y][x-1] == 2)){
							tab[y][x] = 3;
							alive = true;
						}
					}
				}
			}

			for(int x = 1; x < 110; x++){
				for(int y = 1; y < 110; y++){
					if(tab[y][x] == 2) tab[y][x] = 0;
					if(tab[y][x] == 3) tab[y][x] = 1;
				}
			}
		}

		printf("Case #%d: %d\n",cas, res);

	}

	return 0;

}



