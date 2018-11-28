#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int main(){
	ofstream fout ("g11r1ab.out");
	ifstream fin ("g11r1ab.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int numWords, numLists, lengths[100];
		char words[100][11], lists[10][27];
		fin>>numWords>>numLists;
		fin.get();
		for(int n=0; n<numWords; n++){
			fin.getline(words[n], 11);
			lengths[n]=fin.gcount();
		}
		for(int n=0; n<numLists; n++)
			fin.getline(lists[n], 27);
		fout<<"Case #"<<caseNum+1<<":";
		for(int i=0; i<numLists; i++){
			int best=-1, bestWord=-1;
			for(int n=0; n<numWords; n++){
				int score=0;
				list<int> guesses;
				for(int m=0; m<numWords; m++)
					if(lengths[m]==lengths[n] && n!=m)
						guesses.push_back(m);
				for(int j=0; j<26; j++){
					if(guesses.empty())
						break;
					char c=lists[i][j];
					bool has=false, lose=false;
					for(int k=0; k<lengths[n]; k++)
						if(words[n][k]==c)
							has=true;
					for(list<int>::iterator it=guesses.begin(); it!=guesses.end(); ){
						bool match=true;
						for(int k=0; k<lengths[*it]; k++)
							if((words[*it][k]==c) xor (words[n][k]==c))
								match=false;
						if(!match){
							it=guesses.erase(it);
							if(!has)
								lose=true;
						}
						else
							it++;
					}
					if(lose)
						score++;
				}
				if(score>best){
					best=score;
					bestWord=n;
				}
			}
			fout<<" "<<words[bestWord];
		}
		fout<<endl;
	}
	return 0;
}
