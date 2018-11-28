#include <vector>
#include <cstdio>
#include <map>
#include <queue>
#include <iostream>
#include <string>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)

using namespace std;

int main(){
	int T;scanf("%d",&T);
	for(int tt=1 ; tt<=T ; tt++){
		int C;scanf("%d",&C);
		vector<string> combine;
		REP(i,C){
			string s;cin>>s;
			combine.push_back(s);
		}
		int D;scanf("%d",&D);
		vector<string> oppose;
		REP(i,D){
			string s;cin>>s;
			oppose.push_back(s);
		}
		int N;scanf("%d",&N);
		string invoke;cin>>invoke;
		vector<char> res;

		REP(i,invoke.size()){
			res.push_back(invoke[i]);
			if(res.size()>=2){
				char a = res[res.size()-1];
				char b = res[res.size()-2];
				REP(j,C){
					if(	(a==combine[j][0] && b==combine[j][1]) ||
						(a==combine[j][1] && b==combine[j][0])){
							res.pop_back();
							res.pop_back();
							res.push_back(combine[j][2]);
							break;
					}
				}
			}

			vector<int> cnt(256,0);
			REP(j,res.size())cnt[res[j]]++;
			REP(j,D){
				if(cnt[oppose[j][0]]>0 && cnt[oppose[j][1]]>0){
					res.clear();
					break;
				}
			}
		}
		printf("Case #%d: [",tt);
		REP(i,res.size()){
			printf("%c",res[i]);
			if(i!=res.size()-1)printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
