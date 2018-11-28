#include<stdio.h>
#include<iostream>

using namespace std;

int t[120];

int minimo(int a, int b){
	if(a<b) return a;
	else return b;
}

int main(){
	int T, i, N, S, p, k;
	scanf("%d ", &T);
	for(i=0; i<T; i++){
		scanf("%d %d %d ", &N, &S, &p);
		int cont =0; 
		int sur =0;
		for(k=0; k<N; k++){
			scanf("%d ", &t[k]);
			if(t[k] >=3*p-2)
				cont++;
			else if((t[k] >= 3*p-4) && (3*p>4))
				sur++;
		}	
		cout << "Case #" << i+1 << ": " << cont+minimo(S, sur) << endl;
	}
	return 0;
}
