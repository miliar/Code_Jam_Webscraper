#include<stdio.h>
#include<queue>
using namespace std;
int t,n,o, posO,posB,tmp;
char turn;
int main(){
	scanf("%d",&t);
	for(int I = 1; I <= t; ++I){
		o = 0;
		queue<int> qO,qB,qTurn;
		posO = 1; posB = 1;
		
		scanf("%d ",&n);
		
		for(int i=0;i<n;++i){
			scanf("%c%d ", &turn, &tmp);
			
			qTurn.push(turn);
			if(turn == 'O') qO.push(tmp);
			else qB.push(tmp);
		}
		
		for(o = 0; !qTurn.empty() ; ++o){
			bool pushed = 0;
			if(!qO.empty()){
				if(qO.front() > posO) ++posO;
				else if(qO.front() < posO) --posO;
				else if(qTurn.front() == 'O') {
					pushed = 1;
					qO.pop();
					qTurn.pop();
				}
			}
			
			if(!qB.empty()){
				if(qB.front() > posB) ++posB;
				else if(qB.front() < posB ) -- posB;
				else if(qTurn.front() == 'B' && !pushed){
					qB.pop();
					qTurn.pop();
				}
			}
		}
		printf("Case #%d: %d\n",I,o);
	}
}
