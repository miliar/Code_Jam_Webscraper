#include<vector>
#include<iostream>
#include<string.h>
using namespace std;
vector<char> src;
vector<int> pit;
vector<int>result;
int trainS(int k){
	int i,size;
	int count=1;
	char tempC;
	char T1;
	size=src.size();
	tempC=src[pit[0]];
	for(i=1;i<size;++i){
		T1=src[pit[i%k]+i-(i%k)];
		if(tempC!=T1){
			count++;
			tempC=T1;
		}
	}
	return count;
}
void perm(int s,int m,int k){
	int i,res;
	if(s==(m-1)){
	    res=trainS(k);
		result.push_back(res);
	}
	else{
		for(i=s;i<m;++i){
			swap(pit[s],pit[i]);
			perm(s+1,m,k);
			swap(pit[s],pit[i]);
		}
	}
}
void deal(int cases){
	int k,i;
	int out;
	char temp;
	cin>>k;
	temp=getchar();
	for(i=0;i<k;++i){
		pit.push_back(i);
	}
	while('\n'!=(temp=getchar()))
	{
		src.push_back(temp);
	}
	perm(0,i,k);
	out=result[0];
	for(i=1;i<result.size();++i){
		if(out>result[i]){
			out=result[i];
		}
	}
	src.erase(src.begin(),src.end());
	pit.erase(pit.begin(),pit.end());
	result.erase(result.begin(),result.end());
	cout<<"Case #"<<cases<<": "<<out;
}
void main(){
	int i,N;
	cin>>N;
	for(i=0;i<N;++i){
		if(i!=0)cout<<"\n";
		deal(i+1);
	}
}