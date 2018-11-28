#include<iostream>
#include<fstream>
using namespace std;
int T;
int R;
int K;
int N;
int *g;

int main(){
	ifstream fin;
	fin.open("C-small-attempt0.in");
	

	ofstream fout;
	fout.open("out3.small");
	if(!fin || !fout)
		cout<<"Error!"<<endl;
	
	
	fin>>T;
	int income=0;
	for(int i=0; i<T; i++){
		income = 0;
		fin>>R;
		fin>>K;
		fin>>N;
		g = new int[N];
		for(int j=0; j<N; j++)
			fin>>g[j];
		
		int cur = 0;
		while(R>0){
			
			int inc = 0;
			int total = 0;
			while(inc < K && inc+g[cur] <= K && total <N ){
				inc+=g[cur];
				cur=(cur+1)%N;
				total++;
			}
			income+=inc;
			R--;
		}
		
		fout<<"Case #"<<i+1<<":	"<<income<<endl;


	}
}