#include <stdio.h>
#include <string.h>
#include <math.h>

const int maxn = 200;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int k = 1 ; k <= t; k++){
		int n;
		scanf("%d",&n);
		char col[maxn];
		int pos[maxn];
		for (int i = 0 ; i < n ; i++){
			scanf(" %c %d ",&col[i],&pos[i]);
		}
		int posO = 1, needO = -1;
		int posB = 1, needB = -1;
		int cnt = 0;
		int pressed = 0;
		while (pressed != n){
			
			if (needO == -1){
				for (int i = pressed ; i < n ; i++){
					if (col[i] == 'O'){
						needO = i;
						break;
					}
				}
			}
			if (needB == -1){
				for (int i = pressed ; i < n ; i++){
					if (col[i] == 'B'){
						needB = i;
						break;
					}
				}
			}
			bool Opress = pressed == needO;
			if (needO != -1)
			if (posO < pos[needO]){
				posO++;
			} else 
				if (posO > pos[needO]){
					posO--;
				} else
					if (Opress){
						pressed++;
						needO = -1;
					}
			if (needB != -1)
			if (posB < pos[needB]){
				posB++;
			} else 
				if (posB > pos[needB]){
					posB--;
				} else
					if (!Opress){
						pressed++;
						needB = -1;
					}
			cnt++;
		}
		printf("Case #%d: %d\n",k,cnt);
	}
	return 0;
}