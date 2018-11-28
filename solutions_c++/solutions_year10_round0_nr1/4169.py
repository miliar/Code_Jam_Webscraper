#include<iostream>
#include<fstream>
using namespace std;
pair<int,int> L[31];
int main() {
	ifstream in("i.txt");
	int N,K,T;
	in >> T;
	ofstream out("a.txt");
	for(int z = 0; z < T; z++) {
	    in >> N >> K;
	if(K%(1<<N) == (1 << N) - 1) out<<"Case #"<<z+1<<": "<<"ON"<<endl;
	else out<<"Case #"<<z+1<<": "<<"OFF"<<endl;
  }
	system("pause");
}
