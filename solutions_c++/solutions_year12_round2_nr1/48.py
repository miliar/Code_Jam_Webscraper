#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 205;
int Tc;
int n;
int a[N];

int main(){
	cin >> Tc;
	for (int i=1;i<=Tc;i++){
		cin >> n;
		for (int i=0;i<n;i++) cin >> a[i];
		int sum = 0;
		for (int i=0;i<n;i++) sum += a[i];
		printf("Case #%d:",i);
		for (int i=0;i<n;i++){
			double l = 0 , r = 1;
			for (int t=0;t<200;t++){
				double mid = (l + r) / 2;
				double now = a[i] + sum * mid;
				double need = 0;
				for (int j=0;j<n;j++)
					if (i != j){
						if (a[j] >= now) continue;
						need += (now - a[j]) / sum;
					}
				if (need >= 1 - mid) {
					r = mid;
				} else {
					l = mid;
				}
			}
			printf(" %.12lf",l * 100);
		}
		printf("\n");
	}
}
