#include <stdio.h>
#include <string.h>
#define MAX 100010
#define MAXN 110
#define MAXM 1010
#define MAXLEN 110

int main(){
	int t_case,t,i,j,k,d,n,m;
	int map[MAX][3] = {{0}},map_num,min[MAXN][MAXM];
	char engine[MAXN][MAXLEN],query[MAXM][MAXLEN];
	bool find,fail;
	scanf("%d",&t_case);
	for (t = 1;t <= t_case;t++){
		scanf("%d",&n);
		getchar();
		for (i = 0;i < n;i++)
			gets(engine[i]);
		scanf("%d",&m);
		m++;
		getchar();
		for (i = 1;i < m;i++)
			gets(query[i]);
		printf("Case #%d: ",t);
		find = false;
		for (i = 0;i < n;i++){
			map[i][0] = i,map[i][1] = 0,map[i][2] = 0;
			j = map[i][1]+1;
			while (j < m && strcmp(query[j],engine[map[i][0]])){
				min[i][j] = 0,j++;
			}
			j--;
			if (j+1 == m){
				printf("%d\n",map[i][2]);
				find = true;
				break;
			}
			map[i][1] = j;
			for (k = j;k < m;k++)
				min[i][k] = k;
		}
		map_num = i;
		i = 0;
		while (i < map_num && !find){
			for (k = 0;k < n;k++)
				if (k != map[i][0]){
					j = map[i][1]+1,d = map[i][2]+1;
					fail = false;
					while (j < m && strcmp(query[j],engine[k])){
						if (d < min[k][j])
							min[k][j] = d;
						else{
							fail = true;
							break;
						}
						j++;
					}
					j--;
					if (!fail && d <= min[map[i][0]][j]){
						map[map_num][0] = k,map[map_num][1] = j;
						map[map_num++][2] = d;
					}
					if (j+1 == m){
						printf("%d\n",d);
						find = true;
						break;
					}
				}
			i++;
		}
	}
}
