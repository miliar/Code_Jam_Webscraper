#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int howmany(long num,long limit){
	vector<long> res;
	char *num_c=new char[7],*num_new=new char[7];
	itoa(num,num_c,10);
	int num_ln=strlen(num_c);
	for(int i=1;i<num_ln;i++){
		for(int j=num_ln-i;j<num_ln;j++)
			num_new[j-(num_ln-i)]=num_c[j];
		for(int j=0;j<num_ln-i;j++)
			num_new[j+i]=num_c[j];
		long num_new_l=atoi(num_new);
		if(num_new_l>num && num_new_l<=limit){
			//cout<<num<<"  "<<num_new_l<<endl;	
			if(find(res.begin(),res.end(),num_new_l)==res.end())
				res.push_back(num_new_l);
		}
	}
	return res.size();
	return 0;
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
		for(long j=A;j<=B;j++)
			res+=howmany(j,B);
		output<<"Case #"<<i<<": "<<res<<"\n";
		cout<<"Case #"<<i<<": "<<res<<"\n";
	}
	system("pause");
	return 0;
}