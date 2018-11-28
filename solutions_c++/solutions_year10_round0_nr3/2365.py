#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int T,R,k,N;

int g[1000];

int calc(){
	int idx=0;
	int tmpE=0;
	for (int i=0;i<R;i++){
		int tmpK=0;
		for (int tmpN=0;tmpK+g[idx]<=k && tmpN<N;tmpN++){
			tmpK+=g[idx];

			idx++;
			while(idx>=N) idx -= N;
		}
		tmpE+=tmpK;
	}
	return tmpE;
}


int main(int argc,char **argv)
{
	ifstream fin(argv[1]);
	
	fin>>T;

	for(int t=0;t<T;t++){
		fin>>R>>k>>N;
		for(int i=0;i<N; i++){
			fin>>g[i];
		}
		
		int e = calc();
		cout<<"Case #"<<t+1<<": "<<e<<endl;
	}

}
