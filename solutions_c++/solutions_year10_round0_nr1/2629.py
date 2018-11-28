#include<iostream>

#include<fstream>
#include<Cstring>
using namespace std;

const char infile[] = "E://A-large.in";
const char outfile[] = "E://bigrobey1.out";


int main(){
	ofstream o_file;
    ifstream i_file;

	i_file.open(infile);
	o_file.open(outfile);
	int T;
	i_file>>T;
	for(int i=1;i<=T;i++){
		int N,K;
		i_file>>N>>K;
		int qwe=(1<<N);
		int t=K%qwe;
		if(t==qwe-1)
			o_file<<"Case #"<<i<<": "<<"ON"<<endl;
		else
			o_file<<"Case #"<<i<<": "<<"OFF"<<endl;
	}
	i_file.close();
	o_file.close();
	return 0;
}