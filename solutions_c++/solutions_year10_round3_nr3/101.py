#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

int T, m, n, b[5000][5000], cnt[5000], s, mi;
char a[5000][5000], temp[100];

int main(){
	scanf("%d", &T);
	for (int tt = 1; tt<=T; tt++){
		int sum = 0;
		printf("Case #%d: ", tt);
		for (int i=0; i<5000; i++)
			cnt[i] = 0;
		scanf("%d%d", &m, &n);
		gets(temp);
		for (int i=0; i<m; i++){
			gets(a[i]);
			for (int j=0; j<n/4; j++)
				if (a[i][j]>='0' && a[i][j]<='9')
					a[i][j] = a[i][j] - '0';
				else a[i][j] = a[i][j] - 'A' + 10;
			for (int j=0; j<n/4; j++)
				if (i%2 == 0)
					a[i][j] = a[i][j]^10;
				else
					a[i][j] = a[i][j]^5;
		}
		for (int i=0; i<m; i++)
			for(int j=0; j<n/4; j++)
				for (int k=0; k<4; k++)
					b[i][j*4+k] = (a[i][j]>>3-k) & 1;
		if (m>n) mi = n; else mi = m;
		for (int i=mi; i>0; i--)
			for (int j=0; j<m; j++)
				for (int k=0; k<n; k++){
					if (b[j][k] == 1)
						s = 1;
					else s = 0;
					int ans = 0;
					if (((i+j)<=m) && i+k<=n){
					if (s==1)
						for (int q=j; q<i+j; q++){
							for(int w=k; w<i+k; w++)
								if (b[q][w] != 1){
									ans = -1;
									break;
								}
							if (ans == -1)
								break;
						}
					else 
						for (int q=j; q<i+j; q++){
							for(int w=k; w<i+k; w++)
								if (b[q][w] != 0){
									ans = -1;
									break;
								}
							if (ans == -1)
								break;
						}
					if (ans==0){
						for (int q=j; q<i+j; q++)
							for (int w=k; w<i+k; w++)
								b[q][w] = 2;
						cnt[i]++;
					}
					}
				}
		for (int i=1; i<=mi; i++)
			if (cnt[i]!=0)
				sum++;
		printf("%d\n", sum);
		for (int i=mi; i>=1; i--)
			if (cnt[i]!=0)
				printf("%d %d\n", i, cnt[i]);
//		for (int i=0; i<m; i++){
//			for (int j=0; j<n; j++)
//				printf("%d", b[i][j]);
//			printf("\n");
//		}
	}
	return 0;
}
