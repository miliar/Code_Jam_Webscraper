#include <cstdio>
#include <iostream>

using namespace std;

int t, n, m, q;
int ar[1000];
int x[100][100];
int y[100][100];
char s[1000];

int main () {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tc = 0;
	int k;
    scanf("%d", &t);
	while(t--){
		k = 0;
		memset(x, 0, sizeof(x));
		memset(y, 0, sizeof(y));
		
		scanf("%d", &n);
		for(int i = 0; i < n; i++){
			char ca, cb, cc;
			int a, b, c;
			scanf(" %c%c%c", &ca, &cb, &cc);
			a = (ca - 'A') + 1;
			b = (cb - 'A') + 1;
			c = (cc - 'A') + 1;
			x[a][b] = x[b][a] = c;
		}
		scanf(" %d", &m);
		for(int i = 0; i < m; i++){
			char ca, cb;
			int a, b;
			scanf(" %c%c", &ca, &cb);
			a = (ca - 'A') + 1;
			b = (cb - 'A') + 1;
			y[a][b] = 1;	
		}
		
		char ch;
		scanf(" %d ", &q);
		gets(s);
		for(int i = 0; i < q; i++){
			char ch = s[i];
			int num;
			num = (ch - 'A') + 1;
			
			if(k > 0){
				int last = ar[k-1];
				int res = x[last][num];
				if(res){
					ar[k-1] = res;
				}
				else{
					bool ok = true;
					for(int j = 0; j < k; j++){
						if(y[ar[j]][num] || y[num][ar[j]]){
							k = 0;
							ok = false;
						}
					}
					
					if (ok) {
						ar[k++] = num;
					}
				}
			}
			else {
				ar[k++] = num;
			}

//			for(int i = 0; i < k; i++){
//				if(i > 0){
//					printf(", ");
//				}
//				printf("%c", ar[i] + 64);
//			}
//			printf("\n");
		}
		
		printf("Case #%d: [", ++tc);
		for(int i = 0; i < k; i++){
			if(i > 0){
				printf(", ");
			}
			printf("%c", ar[i] + 64);
		}
		printf("]\n");
	}
    return 0;
}
