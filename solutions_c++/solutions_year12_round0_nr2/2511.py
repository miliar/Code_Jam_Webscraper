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

class Dancer{
	public:
		int total,sNum,nNum,diff;
		bool special;
		Dancer();
};

Dancer :: Dancer()
		:total(0),sNum(0),nNum(0),diff(0),special(false){}

int checkS(int total,int p){
	int a1,a2,a3,t=0;
	if(total == 0 && p!=0){return 0;}
	if(total%3==0){ // 9 8 7 || 8 8 8
		a1 = a2 = a3 = total/3;
		t=1;
	}
	else if((total-4)%3==0){ //7 9 9 
		 a1= (total-4)/3;
		 a2 = a3 = (total -a1)/2;
		if(abs(a3-a1)>2){
			a1 = a2 =(total+2)/3;
		a3 = total -a1- a2;
		}

		t=2;
	}
	else if((total-2)%3==0){//7 7 9
		 a1=a2= (total-2)/3;
		 a3 = total -a1 -a2;
		if(abs(a3-a1)>2){
			a1 = (total+4)/3;
		a3 = a2 = (total -a1)/2;
		}

		t=3;
	}
	else{
		a1=a2=a3=t=0;
		return 0;
	}

	if(abs(a3-a1)>2){
		return 0;
	}

	if(3*p <=total && p<=a1 && p<=a3){
		return 1;
	}
	else if(2*p + (p-2) <= total){
			return 1;
	}
	else if(p+2*(p-2) <= total){
			return 1;
	}
	else{
		return 0;
	}
}
	
int checkN(int total,int p){
	int a1,a2,a3,t=0;
	if((total-2)%3==0){ // 9 9 8
		a1= a2 = (total-2)/3;
		a3 = total -a1- a2;
		
		if(abs(a3-a1)>1){
			a1 = a2 =(total+1)/3;
		}
		a3 = total -a1- a2;
		t=1;
	}
	else if((total-1)%3==0){ //8 8 9
		 a1= a2 = (total-1)/3;
		 a3 = total -a1- a2;
		if(abs(a3-a1)>1){
			a1 = a2 =(total-2)/3;
		}
		a3 = total -a1- a2;

		t=2;
	}
	else if(total%3 ==0){
		a1 = a2 = a3= total/3;
		t=3;
	}
	else{
		return 0;
	}

	if(abs(a3-a1)>1){
		return 0;
	}

	if(3*p <=total && p<=a1 && p<=a3){
		return 1;
	}
	else if(2*p + (p-1) <= total){
		if(t==2||t==1){
			return 1;
		}
		return 0;
	}
	else if(p+2*(p-1) <= total){
		if(t==2||t==1){
			return 1;
		}
		return 0;
	}
	else{
		return 0;
	}
}

void set(Dancer array[],int n){
	for(int k=0;k<n;k++){
		if(!array[k].special && array[k].sNum >array[k].nNum){
			array[k].special = true;
			return;
		}
	}
	for(int m=0;m<n;m++){
		if(!array[m].special && array[m].sNum == array[m].nNum){
			array[m].special = true;
			return;
		}
	}
	for(int i=0;i<n;i++){
		if(!array[i].special && array[i].sNum < array[i].nNum){
			array[i].special = true;
			return;
		}
	}
}

int main(){
	int num;
	cin>>num;
	
	int round = 1;
    while(round <= num){
		cout << "Case #" <<round <<": ";
		int n,s,p;
		cin >> n >> s >> p;
		Dancer array[n];
		for(int i =0;i<n;i++){
			cin >> array[i].total;
			array[i].sNum = checkS(array[i].total,p);
			array[i].nNum = checkN(array[i].total,p);
		}
		
		while(s != 0){
			set(array,n);
			s--;
		}
		int result = 0;

		for(int b=0;b<n;b++){
			if(array[b].special){
				result += array[b].sNum;
	//			cout << array[b].total <<" "<<array[b].sNum<<endl;
			}
			else{
				result += array[b].nNum;
//			//	cout << array[b].total <<" n "<<array[b].nNum<<" "<<array[b].sNum<<endl;
			}
		//	cout<<result<<" ";
		}
        cout << result;
		cout<<endl;
		round++;
	}
}	
