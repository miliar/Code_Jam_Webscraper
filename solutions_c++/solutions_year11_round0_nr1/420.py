#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
using namespace std;
int C[2];
int T[2];
int main(){
	int n, t;
	char c;
	int d;
	int ans;
	scanf("%d", &t);
	for (int it=1; it<=t; it++){
		C[0] = C[1] = 1;
		T[0] = T[1] = 0;
		cin>>n;
		while (n--){
			cin>>c>>d;
			int p;
			if (c=='O')
				p = 0;
			else
				p = 1;
			T[p] = T[p] + labs(C[p] - d) + 1;
			if (T[p] < T[1-p] + 1)
			   T[p] = T[1-p] + 1;
			C[p] = d;
		}
		if (T[0]<T[1])
			T[0] = T[1];
		printf("Case #%d: %d\n", it, T[0]);
	}
	return 0;
}
