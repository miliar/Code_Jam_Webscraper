#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <utility>
#include <cstdio>
using namespace std;

int main(){
	FILE* f = fopen("B-large.in", "r");
	ofstream out("output.txt");
	int N;
	fscanf(f,"%d ",&N);
	for(int t = 0; t<N; ++t){
		int T;
		int NA,NB;
		fscanf(f, "%d %d %d ",&T,&NA, &NB);
		multiset<pair<int, int> > AS,BS;
		for(int i = 0; i<NA; ++i){
			int sh,sm,fh,fm;
			fscanf(f,"%d:%d %d:%d",&sh,&sm,&fh,&fm);
			AS.insert(make_pair(sh*60+sm,fh*60+fm));
		}
		for(int i = 0; i<NB; ++i){
			int sh,sm,fh,fm;
			fscanf(f,"%d:%d %d:%d",&sh,&sm,&fh,&fm);
			BS.insert(make_pair(sh*60+sm,fh*60+fm));
		}
		multiset<int> AT, BT;
		int rA = 0, rB = 0;
		while (!AS.empty() || !BS.empty()){
			if (!AS.empty() && (BS.empty() || AS.begin()->first <= BS.begin()->first)){
				if (AT.empty() || *AT.begin() > AS.begin()->first){
					++rA;
				}
				else{
					AT.erase(AT.begin());
				}
				BT.insert(AS.begin()->second+T);
				AS.erase(AS.begin());
			}
			else{
				if (BT.empty() || *BT.begin() > BS.begin()->first){
					++rB;
				}
				else{
					
					BT.erase(BT.begin());
				}
				AT.insert(BS.begin()->second+T);
				BS.erase(BS.begin());
			}
		}
		 
		out<<"Case #"<<t+1<<": "<<rA<<" "<<rB<<endl;
	}
	fclose(f);
	return 0;
}