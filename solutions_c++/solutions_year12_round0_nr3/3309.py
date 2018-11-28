#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int howmany(long num,long limit){
	vector<long> res;
	//Converting
	string num_c, num_new;
	stringstream cvr;
	cvr<<num;
	cvr>>num_c;
	//
	int num_ln=num_c.size();
	for(int i=1;i<num_ln;i++){
		num_new=num_c.substr(num_ln-i,i)+num_c.substr(0,num_ln-i);
		long num_new_l=atoi(num_new.c_str());
		if(num_new_l>num && num_new_l<=limit){
			//cout<<num<<"  "<<num_new_l<<endl;	
			if(find(res.begin(),res.end(),num_new_l)==res.end())
				res.push_back(num_new_l);
		}
	}
	return res.size();
}

int main(){
	ifstream input;
	ofstream output;
	input.open("d:/input.in");
	output.open("d:/output.in");
	int N;
	input>>N;
	for(int i=1;i<=N;i++){
		long A,B,res=0;
		input>>A>>B;
		for(int i=A;i<=B;i++)
			res+=howmany(i,B);
		output<<"Case #"<<i<<": "<<res<<"\n";
		cout<<"Case #"<<i<<": "<<res<<"\n";
	}
	system("pause");
	return 0;
}