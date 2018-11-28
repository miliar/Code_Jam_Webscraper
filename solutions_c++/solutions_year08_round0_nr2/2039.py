#include <stdio.h>
#include <string.h>

#define size 150

int getReady(int h, const int &m, const int &t) {
	int temp = m+t;
	while (temp>60) {
		h++;
		temp-=60;
	}
	return (h*100+temp);
}

void merge(int a[], int low, int high, int mid) {
	int i, j, k, c[100];
	i=low;
	j=mid+1;
	k=low;
	while((i<=mid)&&(j<=high)) {
		if(a[i]<a[j]) {
			c[k]=a[i];
			k++;
			i++;
		}
		else {
			c[k]=a[j];
			k++;
			j++;
		}
	}
	while(i<=mid) {
		c[k]=a[i];
		k++;
		i++;
	}
	while(j<=high) {
		c[k]=a[j];
		k++;
		j++;
	}
	for(i=low;i<k;i++) {
		a[i]=c[i];
	}
} 

int mergesort(int a[], int low, int high) {
	int mid;
	if(low<high) {
		mid=(low+high)/2;
		mergesort(a,low,mid);
		mergesort(a,mid+1,high);
		merge(a,low,high,mid);
	}
	return 0;
}

int main() {
	int n, t, na, nb;
	int h1, m1, h2, m2;
	int a_d[size];
	int a_a[size];
	int b_d[size];
	int b_a[size];
	char buff[50];

	int cursA, cursB;
	int countA, countB;

//	gets(buff);
//	sscanf(buff, "%d", &n);
	scanf("%d", &n);
//	printf("n=%d\n", n);
	for (int i=1; i<=n; i++) {
		memset(a_d, 0, sizeof(a_d));
		memset(a_a, 0, sizeof(a_a));
		memset(b_d, 0, sizeof(b_d));
		memset(b_a, 0, sizeof(b_a));
		countA=0;
		countB=0;

//		gets(buff);
//		sscanf(buff, "%d", &t);
//		gets(buff);
//		sscanf(buff, "%d %d", &na, &nb);

		scanf("%d", &t);
//		printf("t=%d\n", t);
		scanf("%d %d", &na, &nb);
//		printf("na=%d, nb=%d\n", na, nb);
		for (int j=0; j<na; j++) {
//			gets(buff);
//			sscanf(buff, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			a_d[j] = h1*100+m1;
			a_a[j] = getReady(h2, m2, t);
		}
		for (int j=0; j<nb; j++) {
//			gets(buff);
//			sscanf(buff, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			b_d[j] = h1*100+m1;
			b_a[j] = getReady(h2, m2, t);
		}

//		for (int j=0; j<na; j++)
//			printf("a_d[%d]=%d; a_a[%d]=%d\n", j, a_d[j], j, a_a[j]);
//		for (int j=0; j<nb; j++)
//			printf("b_d[%d]=%d; b_a[%d]=%d\n", j, b_d[j], j, b_a[j]);

		mergesort(a_d, 0, na-1);
		mergesort(a_a, 0, na-1);
		mergesort(b_d, 0, nb-1);
		mergesort(b_a, 0, nb-1);
		
		cursA=0;
		cursB=0;
		while (cursA<na && cursB<nb) {
			if (b_a[cursB] > a_d[cursA]) {
				cursA++;
				countA++;
			}
			else {
				cursA++;
				cursB++;
			}
		}
		if (cursA<na)
			countA += na-cursA;

		cursA=0;
		cursB=0;
		while (cursA<na && cursB<nb) {
			if (a_a[cursA] > b_d[cursB]) {
				cursB++;
				countB++;
			}
			else {
				cursA++;
				cursB++;
			}
		}
		if (cursB<nb)
			countB += nb-cursB;

		printf("Case #%d: %d %d\n", i, countA, countB);	
	}
	return 0;
}
