#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
using namespace std;
void deal(int cases){
	vector<int> lettfrency;
	int i,temp,count=0;
	int length;
	__int64 result=0;
	int P,K,L;
	cin>>P>>K>>L;
	for(i=0;i<L;++i){
		cin>>temp;
		lettfrency.push_back(temp);
	}
	sort(lettfrency.begin(),lettfrency.end());
	length=lettfrency.size();
	int c=1;
	int pit;
	while(1){
		for(i=0;i<K;++i){
			if(count==L)break;
			pit=length-count-1;
			result+=lettfrency[length-count-1]*c;
			++count;
		}
		if(count==L)break;
		++c;
	}
	//cout<<"Case #"<<cases<<": "<<result;
	printf("Case #%d: %I64d",cases,result);
}
void main(){
	int cases;
	cin>>cases;
	for(int i=0;i<cases;++i){
		if(i!=0) cout<<"\n";
		deal(i+1);
	}

}