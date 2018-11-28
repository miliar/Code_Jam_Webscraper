#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<iostream>
using namespace std;

int TC, n, i, j;
int po, pb, lo, lb;
int a[105], ans;
char s[105][1];
vector <int> vo, vb;

int main(void){
	scanf("%d", &TC);
	for (int t = 1; t <= TC; t++){
		scanf("%d", &n);
		vo.clear();
		vb.clear();
		for (i = 0; i < n; i++){
			scanf("%s %d", s[i], &a[i]);
			if (s[i][0] == 'O')
				vo.push_back(a[i]);
			else
				vb.push_back(a[i]);
		}
		vo.push_back(0);
		vb.push_back(0); //dummy
		
		po = pb = 1;
		lo = lb = 0;
		ans = 0;
		for (i = 0; i < n; i++){
			/*printf("posisi O = %d, B = %d\n", po, pb);
			printf("tujuan O -> %d, B -> %d\n", vo[lo], vb[lb]);
			printf("ans = %d\n", ans);*/
			int qo = vo[lo]-po;
			int qb = vb[lb]-pb;
			if (s[i][0]	== 'O'){
				//printf("giliran O~!\n");
				ans += abs(qo);
				po = vo[lo];
				lo++;
				if (abs(qb) > abs(qo)+1){
					if (qb < 0)
						qb = -1*(abs(qo)+1);
					else
						qb = (abs(qo)+1);
				}
				pb += qb;
			} else {
				//printf("giliran B~!\n");
				ans += abs(qb);
				pb = vb[lb];
				lb++;
				if (abs(qo) > abs(qb)+1){
					if (qo < 0)
						qo = -1*(abs(qb)+1);
					else
						qo = (abs(qb)+1);
				}
				po += qo;
			}
			ans++;
			//printf("ans jadi %d??\n\n", ans);
		}
		
		printf("Case #%d: %d\n", t, ans);	
	}
	
	return 0;
}
			

				
			
			
			
			
			
			
			
			
			
				
		