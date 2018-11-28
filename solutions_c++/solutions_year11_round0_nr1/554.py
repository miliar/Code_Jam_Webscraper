/*	GCJ - Qualification Round 2011
	Problema A
*/

#include<cstdio>
#include<vector>

#define pb push_back

using namespace std;

int main(){
	int T,n;
	char in[4];
	int mv,resp;
	vector<char>	moves;
	vector<int>	moveO,moveB;

	scanf("%d",&T);
	for(int i=0; i<T; i++){
		resp=0;
		moves.clear();
		moveO.clear();
		moveB.clear();
		scanf("%d",&n);
		for(int j=0; j<n; j++){
			scanf("%s %d",in,&mv);
			if(in[0] == 'O')
				moveO.pb(mv),moves.pb('O');
			else
				moveB.pb(mv),moves.pb('B');
		}
		for(int j=0,lO=1,lB=1,pO=0,pB=0; j<moves.size(); j++){
			switch(moves[j]){
				case 'O':
					while(lO!=moveO[pO]){
						if(lO<moveO[pO])	lO++;
						else				lO--;
						if(lB<moveB[pB])	lB++;
						if(lB>moveB[pB])	lB--;
						resp++;
					}
					pO++;
					resp++;
					if(lB<moveB[pB]) lB++;
					if(lB>moveB[pB]) lB--;
					break;
				case 'B':
					while(lB!=moveB[pB]){
						if(lB<moveB[pB])	lB++;
						else				lB--;
						if(lO<moveO[pO])	lO++;
						if(lO>moveO[pO])	lO--;
						resp++;
					}
					pB++;
					resp++;
					if(lO<moveO[pO])	lO++;
					if(lO>moveO[pO])	lO--;
				default:
					break;
			}
		}
		printf("Case #%d: %d\n",i+1,resp);
	}
	return 0;
}
