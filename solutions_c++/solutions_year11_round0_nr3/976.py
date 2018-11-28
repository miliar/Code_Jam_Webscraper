#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){

	ifstream fin("c.in", ios::in);
	ofstream fout("c.out",ios::out);

	int T;
	fin>>T;
	int i;
	for (i=0;i<T;i++){
		int N;
		fin>>N;
		vector<int> num;//,sorted;
		num.resize(N);
		int j;
		int sumXor = 0;
		int sum=0;
		for (j=0;j<N;j++){
			fin>>num[j];
			sumXor ^= num[j];
			sum += num[j];
		}
		fout<<"Case #"<<i+1<<": ";
		if (sumXor!=0){
			fout<<"NO"<<endl;
		}else{
			sort(num.begin(),num.end());
			fout<<sum-num[0]<<endl;
		}
	}
	fout.close();

	return 0;
}
