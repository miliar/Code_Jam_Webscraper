#include <iostream>
#include <vector>

#define SZ(x) ((int)(x).size())

#define MAXN 100002

using namespace std;

int cor[MAXN][2];

int main(){
	int tcc, tc;
	tcc = 0;
	for (scanf("%d", &tc); tc; --tc){
		long long n, a, b, c, d, x, y, m;

		cin >> n >> a >> b >> c >> d >> x >> y >> m;

		cor[0][0] = x;
		cor[0][1] = y;

		for (int i = 1; i < n; i++){
			x = (a * x + b) % m;
			y = (c * y + d) % m;
			cor[i][0] = x;
			cor[i][1] = y;
		}

		long long sol = 0;


		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				for (int k = j + 1; k < n; k++)
					if ( ( cor[i][0] + cor[j][0] + cor[k][0] ) % 3 == 0 )
						if ( ( cor[i][1] + cor[j][1] + cor[k][1] ) % 3 == 0 )
							++sol;
				

		printf("Case #%d: %d\n", ++tcc, sol);
	}
	return 0;
}
