#include <cstdio>

struct scores{
	int s1, s2, s3;
};

int n, s, p, t;
int vals[100];
scores info[100];

int main(){
	freopen("dance.in", "r", stdin);
	freopen("dance.txt", "w", stdout);
	scanf("%d", &t);
	for(int imaretard = 1; imaretard <= t; imaretard++){
		int count = 0;
		scanf("%d %d %d", &n, &s, &p);
		for(int i = 0; i < n; i++){
			scanf("%d", &vals[i]);
			info[i].s1 = vals[i]/3;
			info[i].s2 = vals[i]/3;
			info[i].s3 = vals[i]/3;
			if(vals[i] % 3 == 1){
				info[i].s3++;
			}
			else if(vals[i] % 3 == 2){
				info[i].s2++;
				info[i].s3++;
			}
		}
		//printf("\nNeeds %d %d %d\n", n, s, p);
		for(int i = 0; i < n; i++){
			//printf("%d %d %d\n", info[i].s1, info[i].s2, info[i].s3);
			if(info[i].s3 >= p) count++;
			else if(info[i].s1 == info[i].s2 && info[i].s2 == info[i].s3 && info[i].s3 + 1 >= p && s > 0 && info[i].s1 - 1 >= 0){
				//printf("HERE");
				count++;
				s--;
			}
			else if(info[i].s2 > info[i].s1 && info[i].s2 == info[i].s3 && info[i].s3 + 1 >= p && s > 0 && info[i].s2 - 1 >= 0){
				count++;
				s--;
			}
		}
		printf("Case #%d: %d\n", imaretard, count);
	}
	return 0;
}