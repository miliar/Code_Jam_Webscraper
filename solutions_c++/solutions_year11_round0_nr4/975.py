#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){

	ifstream fin("d.in", ios::in);
	ofstream fout("d.out",ios::out);

	int T;
	fin>>T;
	int i;
	for (i=0;i<T;i++){
		int N;
		fin>>N;
		vector<int> num;//,sorted;
		num.resize(N);
		int j;
		double lagad = 0;
		int count = 0;
		for (j=0;j<N;j++){
			fin>>num[j];
			num[j]--;
			if (num[j]!=j)
				lagad++;
		}
		/*vector<int> loops;
		for (j=0;j<N;j++){
			if (num[j]>=0){
				int temp;
				int loopsize=1;
				int pos = num[j];
				temp = pos;
				while (pos!=j){
					pos = num[pos];
					num[temp] = -1;
					temp=pos;
					loopsize++;
				}
				loops.push_back(loopsize);
			}
		}
		int Nloop = loops.size();
		double lagad = 0;
		for (j=0;j<Nloop;j++){
			lagad += 2*(loops[j]-1);
		}*/
		fout.precision(6);
		fout<<"Case #"<<i+1<<": "<<fixed<<lagad<<endl;


	}
	fout.close();

	return 0;
}
