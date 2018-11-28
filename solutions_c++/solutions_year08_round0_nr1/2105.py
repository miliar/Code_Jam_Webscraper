#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ifstream ifs=ifstream("in1.txt");
	ofstream ofs=ofstream("out1.txt");
	int N, S, Q;
	bool ses[110];
//	int changes=0;

	ifs>>N;

	for (int i=0; i<N; i++) {
		vector<string> SE;
		ofs<< "Case #" << i+1 << ": ";
		ifs>>S;
		int j;
		for (j=0; j<S; j++) {
			string se="";
			while (se.length()<=0)
				std::getline(ifs,se,'\n');
			SE.push_back(se);
		}
		ifs>>Q;
		int currentse=-1;
		memset(ses, false, sizeof(ses));
		int ava=S;
		j=0;
		int changes=0;
		bool output=false;

		while (j<Q) {
			string query="";
			while (query.length()<=0)
				std::getline(ifs,query,'\n');
			vector<string>::iterator it=find(SE.begin(), SE.end(), query);
			j++;
			if (it-SE.begin()<S) {
				if (!ses[it-SE.begin()]) {
					ava--;
					ses[it-SE.begin()]=true;
					while (ava==1) {
						int k;
						for (k=0; k<S; k++)
							if (!ses[k]) break;
						currentse=k;
						while (j<Q && it-SE.begin()!=currentse) {
							query="";
							while (query.length()<=0)
								std::getline(ifs,query,'\n');
							it=find(SE.begin(), SE.end(), query);
							j++;
						}
						if (j>=Q) {
							if (it-SE.begin()==currentse) changes++;
							ofs<<changes<<endl;
							output=true;
							break;
						}
						changes++;
						ava=S-1;
						memset(ses, false, sizeof(ses));
						ses[currentse]=true;
						currentse=-1;
					}
				}
			}
		}
		if (!output) {
			ofs<<changes<<endl;
		}
	}

	ifs.close();
	ofs.close();
	return 0;
}