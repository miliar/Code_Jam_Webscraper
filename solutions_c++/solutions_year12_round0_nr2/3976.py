#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAXN 2000
int score[MAXN];

int main() {
	int T;
	int i,j,k;
	int n,s,p;
	int NumOfPeople;
	int surprise;
	int a[3];
	int tmp;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(k=1;k<=T;k++) {
		scanf("%d%d%d",&n,&s,&p);
		NumOfPeople=0;
		tmp = surprise=0;
		for(i=0;i<n;i++)	scanf("%d",&score[i]);
		for(j=0;j<n;j++) {
			if(p==0) {
				NumOfPeople++;
				continue;
			}
			else if(p==1) {
				if(score[j]==0) {
					continue;
				}
				else if(score[j]>=1) {
					NumOfPeople++;
					continue;
				}
			}
			else if(score[j]<3*p-4) {
				continue;
			}
			else {
				switch(3*p-score[j]) {
				case 4:surprise++;NumOfPeople++;break;
				case 3:surprise++;NumOfPeople++;break;
				case 2:tmp++;NumOfPeople++;break;
				case 1:tmp++;NumOfPeople++;break;
				default:tmp++;NumOfPeople++;break;
				}
			}
		}
		if(surprise>s) {
			NumOfPeople-=(surprise-s);
		}
		printf("Case #%d: %d\n",k,NumOfPeople);
	}
	return 0;
}