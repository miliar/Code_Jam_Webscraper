#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
using namespace std;
int main(){
	string ifile="A-large.in";
	string ofile="A-large.out";
	ifstream infile(ifile.c_str());
	ofstream outfile(ofile.c_str());
	string s;
    getline(infile,s);
    stringstream ss(s);
    int L,D,N;
    ss>>L;ss>>D;ss>>N;
	vector<string> d;d.resize(D);
	vector<string> n;n.resize(N);
	for(int i=0;i<D;i++){
		getline(infile,d[i]);
	}
	for(int j=0;j<N;j++){
		getline(infile,n[j]);
		vector<int> flag;flag.resize(D);
		int nj=0;
		for(int k=0;k<L;k++){
			if (n[j][nj]=='('){
				while(n[j][nj]!=')'){
					for (int i1=0;i1<D;i1++){
					if (n[j][nj]==d[i1][k])
						flag[i1]++;
					}
					nj++;
				}
				nj++;
			}
			else {
				for (int i1=0;i1<D;i1++){
					if (n[j][nj]==d[i1][k])
						flag[i1]++;
				}
				nj++;
			}
		}
		int count=0;
		for(int m=0;m<D;m++){
			if (flag[m]==L){
				count++;
			}			
		}
		outfile<<"Case #"<<j+1<<": "<<count<<endl;
	}
	infile.close();
    outfile.close();
   
	return 0;
}

Input    
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc

Output 
Case #1: 2
Case #2: 1
Case #3: 3
Case #4: 0
 
