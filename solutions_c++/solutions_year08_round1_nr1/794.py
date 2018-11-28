#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
int cmpncase(const void * a, const void * b){
	return ( *(int*)a ) - ( *(int*)b ) ;
}
int cmpncase2(const void * a, const void * b){
	return ( *(int*)b ) - ( *(int*)a ) ;
}
int main(){
	int T, n, v1[1000], v2[1000];
	long long sum;
	cin >> T;
	for(int i = 0 ; i < T ; i++){
		cin >> n;
		for(int j = 0 ; j < n ; j++)
			cin >> v1[j] ;
		for(int j = 0 ; j < n ; j++)
			cin >> v2[j] ;
		qsort(v1, n, sizeof(v1[0]), cmpncase);
		qsort(v2, n, sizeof(v2[0]), cmpncase2);
		sum = 0;
		for(int j = 0 ; j < n ; j++)
			sum += v1[j] * v2[j];

		cout << "Case #" << i+1 << ": " << sum << endl;
	}
}
