#include <fstream>
#include <iostream>

using namespace std;

int main () {
	
	ifstream fin("B.in");
	ofstream fout("B.out");
	
	int T, C, D, N;
	char word[150], rta[150];
	char opposite[100][3], combine[100][4];
	
	fin>>T;
	
	for(int i=0;i<T;i++) {
		fin>>C;
		for(int j=0;j<C;j++) {
			fin>>combine[j];
		}
		fin>>D;
		for(int j=0;j<D;j++) {
			fin>>opposite[j];
		}
		fin>>N;
		fin>>word;
		
		// Process:
		//cout<<C<<" "<<D<<" "<<N<<" "<<endl;
		int current = 0;
		//cout<<"Word: "<<word<<endl;
		for(int j=0;j<N;j++) {
			//cout<<"letra: "<<word[j]<<endl;
			if(current!=0) {
				// Check Combine:
				bool comb = false;
				char a = word[j];
				char b = rta[current-1];
				for(int k=0;k<C&&!comb;k++) {
					if((combine[k][0]==a && combine[k][1]==b) || (combine[k][0]==b && combine[k][1]==a)) {
						comb = true;
						rta[current-1] = combine[k][2];
						rta[current] = '\0';
						//cout<<"Comb: "<<combine[k]<<endl;
					}
				}
				if(!comb) {
					// Check Opposite:
					bool opp = false;
					for(int k=0;k<current&&!opp;k++) {
						for(int h=0;h<D&&!opp;h++) {
							if((opposite[h][0]==rta[k] && opposite[h][1]==word[j]) ||
							   (opposite[h][1]==rta[k] && opposite[h][0]==word[j])) {
								current = 0;
								opp = true;
								//cout<<"Opposite: "<<opposite[h]<<endl;
							}
						}
					}
					if(!opp) {
						rta[current] = word[j];
						current++;
					}
				}
			} else {
				rta[current] = word[j];
				current++;
			}
		}
		rta[current] = '\0';
		fout<<"Case #"<<i+1<<": ";
		if(current==0) fout<<"[]"<<endl;
		else {
			fout<<"[";
			for(int j=0;j<current-1;j++) { fout<<rta[j]<<", ";}
			fout<<rta[current-1]<<"]"<<endl;
		}
	}
	
	return 0;
}
