#include<iostream>
#include<cmath>
using namespace std;
int numDigits(int number){
	int i=0;
	while(number!=0)
	{
		number=number/10;
		i++;
	}
	return i;
}

int inarray(int *array,int num, int k){
	for(int i=0;i<k;i++){
		if(array[i]==num)
			return 1;
	}
	return 0;
}

int count(int small, int large)
{
	int cnt=0;
	for(int j=small;j<=large;j++){
		int num=j;
		int numD=numDigits(num);
		int newnums[numD-1];
		int lastnewnum=-1;
		int k=0;
		for(int i=0;i<numD-1;i++){
			int newNum=num/(int)pow(10,i+1)+(num%(int)pow(10,i+1))*(int)pow(10,numD-i-1);
			if(newNum>=small&&newNum<=large&&j!=newNum&&!inarray(newnums,newNum,k)){
				cnt++;
				newnums[k]=newNum;
				k++;

			}
			
		}
	}
	return cnt/2;
}

int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		int A,B;
		cin>>A;
		cin>>B;
		cout<<"Case #"<<i+1<<": "<<count(A,B)<<endl; 
	}
}

