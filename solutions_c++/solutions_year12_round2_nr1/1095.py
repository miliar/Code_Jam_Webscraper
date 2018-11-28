#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
int t;
int n;
float a[500];
float ans[500];
cin >> t;

for(int j = 0; j < t; j++){
	cin >> n;
	float total = 0;
	for(int i = 0; i < n; i++){
		cin >> a[i];
		total = total + a[i];
		ans[i] = -1;
	}
	cout << "Case #" << j+1 << ": " ;
	int n1 = n;
	float total1 = total;
	for(int l = 0; l < n; l++){
		if((2*total - n*a[l]) < 0){
			ans[l] = 0.000000;
			n1--;
			total1 = total1 - a[l]; 
		}
	}
	for(int l = 0; l < n; l++){
		if(ans[l] == 0.000000){
		printf("0.000000 ");
		}
		else { printf("%.6f ",100*((total1+total) - n1*a[l])/(n1*total));}
	}
	cout << endl;	
}

return 0;
}
