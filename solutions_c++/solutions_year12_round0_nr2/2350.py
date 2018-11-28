#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
int max_count(int N, int p, int S, int *score){
	int count_1 = 0;
	int count_2 = 0;
	for(int i = 0 ;i<N; i++){

		if(score[i]>=3*p-2 ) count_1++;
		else {
			if(score[i]>=3*p-4 && 3*p-4>=0) count_2++;
		}
	}
	if(count_2<=S) count_1 += count_2;
	else		   count_1 += S;
	return count_1;

}

int main(){
	ifstream fin;
	fin.open("B.in");
	ofstream fout;
	fout.open("B.out");
	int case_num;
	fin>>case_num;
	int N;
	int S;
	int p;
	for(int t  = 0; t < case_num; t++){
		fin>>N>>S>>p;
		int * score;
		score = new int[N];
		for(int j = 0;j<N;j++)
			fin >> score[j] ;
		fout<<"Case #"<<t+1<<": "<<max_count(N,p,S,score)<<endl;
		cout<<t<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
