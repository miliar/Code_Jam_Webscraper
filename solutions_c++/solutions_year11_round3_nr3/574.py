
//Problem A. Square Tiles

#include <iostream>

using namespace std;

int n,l,h;
int freq[100];

int GCD(int a, int b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

int compute(){
	int i,j,k;
	if (l==1) return 1;
	for (i=l;i<=h;i++){
		for (j=0;j<n;j++){
			//printf("gcd %d %d %d\n",i,freq[j],GCD(i,freq[j]));
			if (freq[j]==1) continue;
			//if (GCD(i,freq[j])>1){
			if (i%freq[j]==0 || freq[j]%i ==0){
				
			}else {
				j=999999;
			}
		}
		if (j<999999) return i;
	}
	return 0;
}

int main(){
	int t;
	int i,j,k;
	int result;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>n>>l>>h;
		for (j=0;j<n;j++){
			cin>>freq[j];
		}
		//printf("input: %d %d %d\n",n,l,h);

		result=compute();
		cout<<"Case #"<<(i+1)<<": ";
		if (result){
			cout<<result<<endl;
		}else {
			cout<<"NO"<<endl;
		}
	}
}
