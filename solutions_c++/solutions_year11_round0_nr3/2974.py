#include <iostream>
using namespace std;

long solveEachCase();
long stupidAdd(long, long);
void main(){
	int caseNum;
	cin >> caseNum;
	for(int i = 0; i< caseNum;i++){
		long caseResult = solveEachCase();
		if(caseResult >= long(0))
			cout<< "Case #" <<i+1<<": "<<caseResult;
		else
			cout<< "Case #" <<i+1<<": NO";
		if(i<caseNum-1)
			cout<<endl;
	}

}

long solveEachCase(){
	int candyNum;
	cin >>candyNum;

	long* candyVal =(long*) malloc(candyNum*sizeof(long));
	for(int i=0;i<candyNum;i++){
		cin>>candyVal[i];
	}
	
	long sum = long(0);
	for(int i=0;i<candyNum;i++){
		sum = stupidAdd(sum,candyVal[i]);
	}

	if(sum != long(0))
		return long(-1);

	long min = 1000001;
	long total = 0;
	for(int i =0;i < candyNum;i++){
		total +=candyVal[i];
		if(candyVal[i] < min)
			min = candyVal[i];
	}
	return total -min;
}

long stupidAdd(long a, long b){
	if(a==long(0))
		return b;
	if(b==long(0))
		return a;
	long result = 0;
	long r_A = a%2;
	long d_A = a/2;
	long r_B = b%2;
	long d_B = b/2;
	if(r_A==r_B)
		return stupidAdd(d_A,d_B)*2;
	else
		return stupidAdd(d_A,d_B)*2 + 1;
	
}