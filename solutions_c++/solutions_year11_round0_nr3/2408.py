#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
#include <algorithm>

using namespace std;

vector<int> binary(int i){
	vector<int> ans;
	while(i>=2){
		ans.push_back(i%2);
		i/=2;
	}
	if (i) ans.push_back(i);
	return ans;
} 

int add(int a, int b){
	vector<int> ba=binary(a);
	vector<int> bb=binary(b);
	int len;
	vector<int> bans,bsmall;
	if (bb.size()>ba.size()) {
		len=ba.size();
		bans=bb;
		bsmall=ba;
	}
	else{
		len=bb.size();
		bans=ba;
		bsmall=bb;
	}
	for(int i=0;i<len;i++){
		if(bans[i]==bsmall[i]) bans[i]=0;
		else bans[i]=1;
	}
	int ans=0;
	for(int i=0;i<(int)bans.size();i++){
		ans+=pow(2.0,i)*bans[i];
	}
	//cout<<a<<" "<<b<<" "<<ans<<endl;
	return ans;
}

string solve(string str1,int N){
	stringstream s(str1);
	vector<int> c;
	for(int i=0;i<N;i++){	
		int candy;
		s>>candy;
		c.push_back(candy);
	}
	int total=0;
	for(int i=0;i<N;i++){
		total=add(total,c[i]);
		//cout<<total<<endl;
	}
	if (total!=0) return "NO";
	else {
		sort(c.begin(),c.end());
		int ans=0;
		for(int i=1;i<N;i++){
			ans+=c[i];
		}
		stringstream s1;
		s1<<ans;
		return s1.str();
	}
}	

int main(){
	int T;
	fstream ps("statement.txt");
	fstream output("output.txt",fstream::trunc | fstream::out);
	ps>>T;
	int i=1;
	while(i!=T+1){
		int N;
		ps>>N;
		string str;
		do {
			getline(ps,str);
		}while(str=="");
		output<<"Case #"<<i<<": "<<solve(str,N)<<endl;
		//cout<<"Case #"<<i<<": "<<solve(str,N)<<endl;
		i++;	
	}		
	return 0;
}	
