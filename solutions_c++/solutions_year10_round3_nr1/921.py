#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#define mp make_pair
using namespace std;

pair<int , int> X[1001];

int main(){
	int runs,n;
	int cont = 1;
	int a , b , c , d;
	int res = 0;
	cin >> runs;
	while(runs--){
		cin >> n;
		res = 0;
		for(int i = 0 ; i < n ; i++){
			scanf("%d%d",&a,&b);
			X[i] = mp(a,b);
		}
		sort(X,X+n);
		for(int i = 0 ; i < n ; i++){
			for(int j = i+1 ; j < n ; j++){
				if(X[i].second > X[j].second) res++;
			}
		}
		printf("Case #%d: %d\n",cont++,res);
	}
	return 0;
}