#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int ans( ifstream & in){
	int N, limit,  p;
	in >> N >> limit >> p;
	int *tt = new int[N];
	for(int i=0;i!=N;++i){
		in >> tt[i];
	}

	int count=0;
	for(int i=0;i<N;++i){
 		int r=tt[i]%3;
		int low,hi;
 		switch(r){
   			case 0: low = tt[i]/3; hi = ( tt[i] >=3 ? (tt[i]+3)/3 : 0);
    				break;
   			case 1: low = hi = ( tt[i] >=  4 ? (tt[i]+2)/3 : 1);
    				break;
   			case 2: low = (tt[i]+1)/3; hi = (tt[i]+4)/3;
    				break;
  		}
		if(low >= p) ++count;
		else if(hi >= p && limit >0) {
                	++count; --limit;
                }
	}
        return count;
}

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("inout/B-large.in");
	fout.open("inout/B.out");

	int T;
	fin >> T;
	for(int i=0;i != T ;++i)
	{
		int a = ans(fin);
		fout << "Case #" << i+1 << ": " << a << endl;
	}

	fout.close();
	fin.close();
	return 0;
}
