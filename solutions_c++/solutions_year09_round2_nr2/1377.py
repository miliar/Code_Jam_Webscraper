#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int nextno(int no){
	int next, n=no;
	vector<int> nos,arranged;
	while(no){
		nos.push_back(no%10);
		no /=10;
	}
	sort(nos.begin(),nos.end());
	next=0;
	for(int i=nos.size()-1;i>=0;i--){
		next = next * 10 + nos[i];
	}
	if(next <= n)
		nos.insert(nos.begin(),0);
	do{
		next=0;
		for(int i=nos.size()-1;i>=0;i--){
			next = next * 10 + nos[i];
		}
		arranged.push_back(next);
	}while(next_permutation(nos.begin(),nos.end()));
	sort(arranged.begin(),arranged.end());
	int pos = find(arranged.begin(),arranged.end(),n) - arranged.begin();
	return arranged[pos+1];
}

int main(){
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		int no;
		cin >> no;
		cout << "Case #"<<i+1<<": "<<nextno(no)<<endl;
	}
	return 0;
}
