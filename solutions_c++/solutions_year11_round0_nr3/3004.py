#include <iostream>
#include <set>
using namespace std;

multiset<int> candy;
int sum;

int think(multiset<int>::const_reverse_iterator max_iter,int val,int xor){
	int next,next_max=val;
	if(max_iter==candy.rend())return xor?0:val;
	// cerr<<"("<<*max_iter<<","<<val<<","<<xor<<"){";
	for(multiset<int>::const_reverse_iterator iter=max_iter;iter!=candy.rend();iter++){
		next=think((++iter)--,val+*iter,xor^*iter);
		if(next_max<next&&next<sum){
			next_max=next;
		}
	}
	// cerr<<next_max<<"}";
	return next_max;
}

int main(){
	int t;
	cin>>t;
	for(int case_num=1; case_num<=t; case_num++){
		// cerr<<"-- #"<<case_num<<" --"<<endl;
		candy.clear();
		int n;
		cin>>n;
		int val,xor=0;
		sum=0;
		for(int i=0;i<n;i++){
			cin>>val;
			candy.insert(val);
			xor^=val;
			sum+=val;
		}
		if(xor){
			cout<<"Case #"<<case_num<<": NO"<<endl;
			continue;
		}

		int result=think(candy.rbegin(),0,0);

		if(result){cout<<"Case #"<<case_num<<": "<<result<<endl;}
		else{cout<<"Case #"<<case_num<<": NO"<<endl;}
		// cerr<<endl;
	}
	return 0;
}