#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <fstream>

using namespace std;

long long nextstep(vector <long long> &groupsizes, long long index, long long buscapacity, long long &newindex, long long &money){
	long long sum=0;
	newindex=index;
	long long i = 0;
	while((sum+groupsizes[newindex]<=buscapacity)&&(i<groupsizes.size())){
		sum = sum+groupsizes[newindex];
		i++;
		newindex=(newindex + 1 + groupsizes.size())%groupsizes.size();
	}
	money = sum;
	//cout << "money = " << money << endl;
	return 0;
}
void getperiod(vector <long long> &groupsizes, long long buscapacity,long long &periodlength, 
			   long long &periodstartround, long long &periodstartindex, long long &periodmoney,long long &totmoney){
	vector <long long> moneyatindex;
	vector <long long> roundatindex;
	moneyatindex.assign(groupsizes.size(),-1);
	roundatindex.assign(groupsizes.size(),-1);
	totmoney = 0;
	long long i =1;
	bool repetition = false;
	long long index = 0;
	long long newindex;
	long long money;
	long long tot=0;
	//invariants:
	//at the beginning of the loop:
	//1-roundatindex[index] = -1
	//2-moneyatindex[index] = -1
	//3-tot contains the money of all rounds prior to round i;
	//4-roundatindex has a non-negative value at every index that has been visited prior to round i;
	
	
	while(repetition==false){		
		nextstep(groupsizes,index,buscapacity,newindex,money);
		if(roundatindex[index]!=-1){
			periodmoney = tot + money - moneyatindex[index]; 
			periodstartround = i; 
			totmoney = tot;
			periodlength = i-roundatindex[index];
			periodstartindex = index;
			
			repetition = true;
		}
		else{
			roundatindex[index] = i;
			moneyatindex[index] = tot+money;
			tot = tot+money;
			index = newindex;
			i++;
		}
	}
}
long long simplesolve( vector <long long> &groupsizes,long long nrounds, long long buscapacity,long long startindex ){
	long long tot = 0;
	long long index = startindex;
	long long newindex = 0;
	long long money = 0;
	for(long long i=0;i<nrounds;i++){
		nextstep(groupsizes,index,buscapacity,newindex,money);
		tot+=money;
		index = newindex;
	}
	return tot;

}
long long solveinstance( vector <long long> &groupsizes,long long nrounds, long long buscapacity ){
	long long periodlength,periodstartround,periodstartindex,periodmoney,totmoney;
	getperiod(groupsizes,buscapacity,periodlength,periodstartround,periodstartindex,periodmoney,totmoney);
	if(nrounds<=periodstartround+3){
		return simplesolve(groupsizes,nrounds,buscapacity,0);
	}
	else{
		//cout <<"we're here" << endl;
		long long steady = periodmoney*((nrounds-periodstartround+1)/periodlength);
		long long remaining = (nrounds-periodstartround+1)%periodlength;
		long long ret  = simplesolve(groupsizes,remaining,buscapacity,periodstartindex);
		totmoney = totmoney + steady + ret;
		return totmoney;
	}
}
void testsolveinstance(){
	long long r;
	cout << "please enter the number of rounds" << endl;
	cin >> r;
	cout << "please enter the bus capacity" << endl;
	long long cap;
	cin >> cap;
	cout << "please say how many groups" << endl;
	long long n;
	cin >> n;
	cout << "please enter the group sizes" << endl;
	long long z;

	vector <long long> vi;
	for (long long i=0;i<n;i++){
		cin >> z;
		vi.push_back(z);
	}
	long long m1 = simplesolve(vi,r,cap,0);
	long long m2 = solveinstance(vi,r,cap);
	cout << "m1 = " << m1 << endl;
	cout << "m2 = " << m2 << endl;
	
}
void testnextstep(){
	long long r;
	cout << "please enter the number of rounds" << endl;
	cin >> r;
	cout << "please enter the bus capacity" << endl;
	long long cap;
	cin >> cap;
	cout << "please say how many groups" << endl;
	long long n;
	cin >> n;
	cout << "please enter the group sizes" << endl;
	long long z;

	vector <long long> vi;
	for (long long i=0;i<n;i++){
		cin >> z;
		vi.push_back(z);
	}
	long long tot = 0;
	long long index = 0;
	long long newindex = 0;
	long long money = 0;
	for(long long i=0;i<r;i++){
		nextstep(vi,index,cap,newindex,money);
		tot+=money;
		index = newindex;
	}
	cout << "the total is " << tot << endl;
}
void solveproblem(){
	ofstream outfile;
	ifstream infile;
	infile.open("C-Large.in");
	outfile.open("C-Large.out");
	long long N;
	infile >> N;
	for(long long i=0;i<N;i++){
		long long R,k,n;
		infile >> R >> k >> n;
		vector <long long> groupsizes;
		for(long long j=0;j<n;j++){
			long long z;
			infile >> z;			
			groupsizes.push_back(z);
		}
		long long m = solveinstance(groupsizes,R,k);
		outfile << "Case #" << i+1 <<": " << m << endl; 
	}

}
int  main(){
	solveproblem();
	return 0;
}