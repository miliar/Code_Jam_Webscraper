#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
using namespace std;
int main (int argc, char * const argv[]) {
	ofstream outFile;
	ifstream inFile;
	outFile.open("A-large.out");
	inFile.open("A-large.in.txt");
	int T,N;
	int rows[40];
	inFile>>T;
	string instring;
	char charSearch;
	int temp;
	int count;
	int wswitch;
	for(int c=0; c<T; c++){
		count=0;
		inFile>>N;
		for(int i=0; i<N;i++){
			inFile>>instring;
			rows[i]=instring.find_last_of('1');
		}
		
		for(int i=0; i<N; i++){
			if(rows[i]>i){
				for(int j=i+1; j<N; j++){
					if(rows[j]<=i){
						wswitch=j;
						break;
					}
				}
				temp=rows[wswitch];
				for(int j=wswitch; j>i; j--){
					rows[j]=rows[j-1];
				}
				rows[i]=temp;
				count+=wswitch-i;
			}
		}
		outFile<<"Case #"<<c+1<<": "<<count<<endl;
	}
	outFile.close();
	inFile.close();
    return 0;
}
