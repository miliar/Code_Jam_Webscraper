#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <cassert>
#include <string.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int digit(int n){
	int d = 1;
	while(n>=10){
		n = n/10;
		d ++;
	}
	return d;
}

int isPaired(int val,int array[],int a,int b){
	int d = digit(val);
	int count = 0;
	int tmp = pow(10,d-1)* (val%10) + val/10;
	while (tmp != val){
		if(tmp >= a && tmp <=b && array[tmp] != -99){
			count++;
			array[tmp]=-99;
		}
		tmp = pow(10,d-1)* (tmp%10) + tmp/10;
	}
	int result = (count+1)*count/2;
	return result;
}

void makeArray(int array[],int a,int b){
	for(int i=0;i<a;i++){
		array[i]=-99;
	}
	for(int k=a;k<b+1;k++){
		array[k]=k;
	}
}

int check(int array[],int a, int b){
	int count =0;
	for(int i=a;i<=b;i++){
		count += isPaired(i,array,i,b);
	}
	return count;
}

int part(int array[],int a,int b){
	int d = digit(b)-digit(a);
	int count =0;
	if(d == 0){
		count = check(array,a,b);
	}
	else{
		count = check(array,a,pow(10,digit(a)-1)-1);
		int foo = digit(a);
		while(foo<digit(b)){
			count += check(array,pow(10,foo -1),pow(10,foo)-1);
			foo++;
		}
		count += check(array,pow(10,digit(b)-1),b);
	}
	return count;
}

int main(){
	int num;
	cin>>num;

	int round = 1;
    while(round <= num){
		cout << "Case #" <<round <<": ";
		int a,b;
		cin >> a >> b;
//		cout << digit(10)<<" "<<digit(151)<<endl;
		int array[b+1];
		makeArray(array,a,b);
//		cout << array[0]<<" " << array[a]<<" "<<array[b];
//		cout << isPaired(125,array,100,300);

//		cout << check(array,a,b);
		int result = part(array,a,b);
        cout << result;
		cout<<endl;
		round++;
	}
}	




