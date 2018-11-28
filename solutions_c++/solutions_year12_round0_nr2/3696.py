#include <iostream>
#include <fstream>
using namespace std;




bool usedSuprice=false;


bool calcMax(int num,int toAchive,bool canUseSuprice){
	if(num==0){
		return 0==toAchive;
	}
	int close = num/3;

	if(num%3!=0){
		toAchive--;
	}
	if(close>=toAchive){
		return true;//dont need to use suprice.
	}else if(canUseSuprice&&num%3!=1){
		toAchive--;
		if(close>=toAchive){
			usedSuprice=true;
			return true;
		}
	}
	return false;
}


int solve(int n, int s, int p, int * arr){
	int count =0;
	int supriceLeft = s;
	for(int i=0;i<n;i++){
		bool temp = calcMax(arr[i],p,(s>0));
		if(temp){ //count it ?
			count++;
			if(usedSuprice){ //i use a greedy algorithm
				s--;
				usedSuprice=false;
			}
		}
	}
	return count;
}



void readIn(){
	ifstream in ("in.txt");
	int numOftests=0;
	in>> numOftests ;
	FILE * f = fopen("out.txt","w");
	for(int i=0;i<numOftests;i++){
		int n =0,s=0, p=0;
		in  >> n;
		in >> s;
		in >> p;

		int *arr  = new int[n];
		for (int j = 0; j < n; j++)
		{
			in >> arr[j]; 
		}
		//solve here..
		int result =solve(n,s,p,arr);
		fprintf(f,"Case #%i: %i",i+1,result);
		fprintf(f,"\n");
	}
	fclose(f);
}


int main(){
	readIn();
	printf("\r\n---done---");
	cin.get();
}