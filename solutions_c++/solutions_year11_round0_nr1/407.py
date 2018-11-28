#include <vector>
#include <cstdio>
#include <map>
#include <queue>
#include <iostream>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)

using namespace std;

int main(){
	int T;scanf("%d",&T);
	for(int tt=1 ; tt<=T ; tt++){
		int N;scanf("%d",&N);
		queue<pair<int,int> > blue;
		queue<pair<int,int> > orange;
		REP(i,N){
			int p;
			char r;
			scanf(" %c %d",&r,&p);
			//cout << p << "," << r << endl;
			if(r=='B')blue.push(make_pair(i,p));
			else orange.push(make_pair(i,p));
		}
		int res = 0;
		int cnt = 0;
		int bpos = 1;
		int opos = 1;
		while(cnt<N){
			bool pushed = false;
			if(!blue.empty()){
				if(blue.front().second==bpos){
					if(blue.front().first==cnt){
						blue.pop();
						pushed = true;
					}
				}
				else if(blue.front().second>bpos)bpos++;
				else if(blue.front().second<bpos)bpos--;
			}
			if(!orange.empty()){
				if(orange.front().second==opos){
					if(orange.front().first==cnt){
						orange.pop();
						pushed = true;
					}
				}
				else if(orange.front().second>opos)opos++;
				else if(orange.front().second<opos)opos--;
			}
			if(pushed)cnt++;
			res++;
		}
		printf("Case #%d: %d\n",tt,res);
	}
	return 0;
}
