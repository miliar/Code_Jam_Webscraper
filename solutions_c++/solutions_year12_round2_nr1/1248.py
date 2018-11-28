#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <functional>
#include <map>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
using namespace std;
const double PI = 3.14159265358979323846;

int s[200],s2[200];

int main(){
	int T;
	scanf("%d",&T);
	for(int X = 1; X <= T; X++){
		int n;
		scanf("%d",&n);
		for(int i = 0; i < n; i++)scanf("%d",s+i);
		for(int i = 0; i < n; i++)s2[i]=s[i];
		int sum = 0,rest = 0;
		for(int i = 0; i < n; i++)sum += s[i];
		rest = sum;
		int r = 0,k;
		
		while(1){
			k = 0;
			for(int i = 0; i < n; i++){
				if(s2[i]<r){
					rest--;
					s2[i]++;
				}
				k += s2[i]==r;
			}
			if(k>rest)break;
			r++;
		}
		
		printf("Case #%d:",X);
		for(int i = 0; i < n; i++){
			double ans = (s2[i]-s[i]+(s2[i]==r?(double)rest/(double)k:0))*100.0/sum;
			printf(" %0.6f",ans);
		}
		printf("\n");
	}
	return 0;
}
