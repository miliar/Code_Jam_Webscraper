#include <iostream>
#include <fstream>
#include <queue>
#include <utility>

using namespace std;

int main(){
	ofstream fout ("g11r1ac.out");
	ifstream fin ("g11r1ac.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int c[80], s[80], t[80], start, total;
		fin>>start;
		for(int n=0; n<start; n++)
			fin>>c[n]>>s[n]>>t[n];
		fin>>total;
		total+=start;
		for(int n=start; n<total; n++)
			fin>>c[n]>>s[n]>>t[n];
		int best=0;
		for(int goal=start; goal<=total; goal++){
			int turns=1, score=0, hand=start;
			priority_queue<int> cards[2];
			for(int n=0; n<hand && n<goal; n++){
				if(t[n]>0){
					turns+=t[n]-1;
					score+=s[n];
					hand+=c[n];
				}
				else
					cards[c[n]].push(s[n]);
			}
			while(hand<goal){
				if(turns==0 || cards[1].empty())
					break;
				turns--;
				score+=cards[1].top();
				cards[1].pop();
				hand++;
				if(turns==0)
					break;
				for(int n=hand-1; n<hand && n<goal; n++){
					if(t[n]>0){
						turns+=t[n]-1;
						score+=s[n];
						hand+=c[n];
					}
					else
						cards[c[n]].push(s[n]);
				}
			}
			while(turns>0){
				turns--;
				if(!cards[0].empty() && (cards[1].empty() || cards[0].top()>cards[1].top())){
					score+=cards[0].top();
					cards[0].pop();
				}
				else if(!cards[1].empty()){
					score+=cards[1].top();
					cards[1].pop();
				}
				else
					break;
			}
			if(score>best)
				best=score;
		}
		fout<<"Case #"<<caseNum+1<<": "<<best<<endl;
	}
	return 0;
}
