#include<iostream>
#include<cstdio>
using namespace std;

static int intcmp(const void *a,const void *b){
	return *((const int*)b) - *((const int*)a) ; 
}

int long long solve( int n, int k, int l ){
	long long int keystrokes=0;
	int a[1001];
	for(int i=0;i<l;i++){
		cin >> a[i];
	}
	qsort((int*)a,l,sizeof(int),intcmp);
	int numkeys=1;
	for(int i=0;i<l;i++){
		keystrokes += a[i]*((int)i/k+1);
	}
	return keystrokes;


}

int main(){
	int n,k,l;
	int cases;
	cin >> cases;
	for(int i=0; i< cases;i++ ){
		cin >> n >> k >>l;
	cout << "Case #"<<i+1<<": "<<solve(n,k,l)<<endl;
	}
	return 0;
}


