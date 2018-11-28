#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

#define size 1005

void merge(int a[], int low, int high, int mid) {
	int i, j, k, c[600];
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
	int n, p, k, l;
	int alpha[size];
	int press;
	int key;
	int answer;

	scanf("%d", &n);
	for (int i=1; i<=n; i++) {
		memset(alpha, 0, sizeof(alpha));
		scanf("%d %d %d", &p, &k, &l);
		for (int j=0; j<l; j++) {
			scanf("%d", &alpha[j]);
		}

		mergesort(alpha, 0, l-1);

//		for (int j=0; j<l; j++)
//			printf("%d ", alpha[j]);
//		printf("\n");

		press = 1;
		key = 0;
		answer = 0;
		for (int j=(l-1); j>=0; j--) {
			answer += press*alpha[j];
//			cout << "alpha[j] = " << alpha[j] << " ";
			
			key++;
			if (key == k) {
				key = 0;
				press++;
			}
//			cout << "key = " << key << " ";
		}

		printf("Case #%d: %d\n", i, answer);
	}
	return 0;
}