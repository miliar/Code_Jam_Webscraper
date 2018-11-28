#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>

int time, na, nb;
int tba[100][2], tbb[100][2];
void read(int tb[][2], int n) {
	for(int i=0;i<n;i++) {
		int a,b;
		scanf("%d:%d",&a,&b);
		tb[i][0] = a*60+b;
		scanf("%d:%d",&a,&b);
		tb[i][1]= a*60+b;
	}
}

void sort(int tb[][2], int sindex,int size) {
	/*
	for(int i=0;i<size;i++) {
		printf("%d:%d %d:%d\n",tb[i][0]/60,tb[i][0]%60,tb[i][1]/60,tb[i][1]%60);
	}*/

	for(int i=0;i<size-1;i++) {
		int k = i;
		for(int j=i+1;j<size;j++) {
			if (tb[j][sindex]<tb[k][sindex]) k=j;
		}
		if (k!=i) {
			int swap = tb[k][0];
			tb[k][0] = tb[i][0];
			tb[i][0] = swap;
			swap=tb[k][1];
			tb[k][1]=tb[i][1];
			tb[i][1]=swap;
		}
	}
	/*
	printf("---%d %d\n",sindex, size);
	for(int i=0;i<size;i++) {
		printf("%d:%d %d:%d\n",tb[i][0]/60,tb[i][0]%60,tb[i][1]/60,tb[i][1]%60);
	}*/
}
int work(int tba[][2], int na, int tbb[][2], int nb) {
	sort(tba, 0, na);
	sort(tbb, 1, nb);
	// int used[100]; for(int i=0;i<nb;i++) used[i]=0;
	int j=0; 
	int touse = 0;
	for(int i=0;i<na;i++) {
		// check if a train from b could be used
		if (j==nb) {
//			printf("for train %d:%d, use another\n", tba[i][0]/60, tba[i][0]%60);
			touse++;
		}
		else if (tba[i][0] >= tbb[j][1]+time) {
//			printf("%d:%d by %d:%d\n",tba[i][0] / 60,tba[i][0]%60,tbb[j][1] / 60,tbb[j][1]%60);
			j++;
		} else {
//			printf("for train %d:%d, use another 2\n", tba[i][0]/60, tba[i][0]%60);
			touse++;
		}
	}
	return touse;

}
int main() {
	int n;
	scanf("%d", &n);
	for(int i=1;i<=n;i++) {
		scanf("%d %d %d ",&time, &na, &nb);
		read(tba,na);
		read(tbb,nb);
		printf("Case #%d: %d %d\n",i,work(tba,na,tbb,nb),work(tbb,nb,tba,na));
	}
//	scanf("%d",&n);
	return 0;
}