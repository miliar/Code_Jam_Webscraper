#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <sstream>
using namespace std;

void printVector(vector<int> d){
	for(int i=0;i<d.size();i++){	cout<<d[i]<<" ";}
	cout<<endl;
}

double mylog(int a,int b){
	return log((double)a)/log((double)b);
}

void convert(int a, int b, vector<int> &digit){
	digit.clear();
	while(a>0){
		int index=(int)floor(mylog(a,b));
		int fac=a/pow((double)b,(double)index);
		digit.push_back(fac);
		a-=fac*pow((double)b,(double)index);
	}
}

bool isHappy(int a,int b){
	vector<int> digit;
	convert(a,b,digit);
	//test;
	//printVector(digit);
	
	bool noOccur=true;
	bool happy=false;
	set<int> occur;
	while(noOccur){
		int sum=0;
		for(int i=0;i<digit.size();i++){	sum+=digit[i]*digit[i];}
		
		if(sum==1){	happy=true;	break;}
		if(occur.find(sum)!=occur.end()){	noOccur=false;	break;}
		occur.insert(sum);
		convert(sum,b,digit);
	}
	
	if(happy){	return true;}
	else{	return false;}
}

int main(){
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	
	int T;
	fin>>T;
	string str;
	getline(fin,str);
	vector<int> base;
	for(int r=1;r<=T;r++){
		base.clear();
		getline(fin,str);
		stringstream ss(str);
		int tmp;
		while(ss>>tmp){	base.push_back(tmp);}
		
		bool found=false;
		int ans=2;
		while(!found){
			//cout<<ans<<endl;
			bool ok=true;
			for(int i=0;i<base.size();i++){
				if(!isHappy(ans,base[i])){	ok=false;	break;}
			}
			if(ok){	found=true;	break;}
			else{	ans++;}
		}
		
		cout<<ans<<endl;
		fout<<"Case #"<<r<<": "<<ans<<endl;
	}
}