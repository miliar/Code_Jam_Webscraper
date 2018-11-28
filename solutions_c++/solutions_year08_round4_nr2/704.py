#include <cstdio>
#include <cmath>
#include <memory>

int M, N, A;

int area(int x1, int y1, int x2, int y2){
	return abs(x1 * y2 - x2 * y1);
}

int main(){
	int nCase;
	scanf("%d", &nCase);
	for(int ca = 1; ca <= nCase; ++ca){
		scanf("%d %d %d", &N, &M, &A);
		bool flg = false;
		int x1, y1, x2, y2;
		for(x1 = 0; x1 <= N && !flg; ++x1)
			for(y1 = 0; y1 <= M && !flg; ++y1)
				for(x2 = 0; x2 <= N && !flg; ++x2)
					for(y2 = 0; y2 <= M && !flg; ++y2)
						if(area(x1, y1, x2, y2) == A) flg = true;
		printf("Case #%d: ", ca);
		if(flg) printf("0 0 %d %d %d %d\n", x1 - 1, y1 - 1, x2 - 1, y2 - 1);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}

