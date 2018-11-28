#include<iostream>
#include<cassert>
using namespace std;

const int maxl = 1000001;
int tn;
int p,l,k;
int fre[maxl];

int cmp(const void*va, const void *vb){
	return *(int*)vb - *(int*)va;
}

void init(){
	cin>>p>>k>>l;
	assert(l <= p*k);
	for(int i=0; i<l; i++){
		cin>>fre[i];
	}
	qsort(fre, l, sizeof(int), cmp);
}

int getnum(){
	int sum = 0;
	for(int i=1; (i-1)*k<l; i++){
		for(int j=(i-1)*k; j<i*k && j<l; j++){
			sum += fre[j]*i;
		}
	}
	return sum;
}

int main(){
	cin>>tn;
	for(int i=1; i<=tn; i++){
		init();
		cout<<"Case #"<<i<<": "<<getnum()<<endl;
	}	
	return 0;
}
