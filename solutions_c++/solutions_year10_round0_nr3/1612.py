#include <vector>
#include <iostream>
using namespace std;
__int64 R,k,N;
__int64 S[1000];
__int64 eval(__int64 start, __int64 &total){
	__int64 end=start;
	bool finished=false;
	total=0;
	while(((total+S[end])<=k) && !finished){
		total+=S[end];
		end=(end+1)%N;
		if(end==start){
			finished=true;
		}
	}
	return end;
}

__int64 solve(){
	cin>>R>>k>>N;
	for(__int64 i=0;i<N;++i){
		cin>>S[i];
	}
	__int64 gain;
	__int64 a=eval(0,gain);
	__int64 b=eval(a,gain);
	//===find precycle===
	while(a!=b){
		a=eval(a,gain);
		b=eval(b,gain);
		b=eval(b,gain);
	}
	//===accumulate precycle===
	__int64 total=0;
	a=0;
	while((a!=b)&&(R>0)){
		a=eval(a, gain);
		total+=gain;
		--R;
	}
	if(R==0){
		return total;
	}
	//===find cycle len===
	__int64 cycleLen=0;
	__int64 cycleGain=0;
	do{
		a=eval(a,gain);
		cycleGain+=gain;
		++cycleLen;
	}while(a!=b);
	//===compute total===
	total+=(R/cycleLen)*cycleGain;
	__int64 remaining=R%cycleLen;
	for(__int64 i=0;i<remaining;++i){
		a=eval(a,gain);
		total+=gain;
	}
	return total;
}

int main(){
	__int64 numCases;
	cin>>numCases;
	for(__int64 i=1;i<=numCases;++i){
		__int64 sol=solve();
		cout<<"Case #"<<i<<": "<<sol<<endl;
	}
	return 0;
}