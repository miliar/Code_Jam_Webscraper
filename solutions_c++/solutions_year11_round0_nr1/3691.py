
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <stdio.h>
#include <string.h>
#include <list>
#define FOR(i,a,b) for (int i=a; i<b; i++)
#define REP(i,n) for(int i=0;i<(int)n;++i)

using namespace std;

int main(){
	ifstream in("input.txt");
	FILE *out=fopen("answer.txt","w");
	int T,N;
	in>>T;
	REP(t,T){
		in>>N;
		int o=1,b=1;
		int time=0;
		int freeB=0,freeO=0;
		char c;
		REP(i,N){
			in>>c;
			int x;
			in>>x;
			if (c=='O'){
				//IF Orange is to go
				if (freeO>=abs(x-o)){
					//When freeO is enough
					//One second for pushing a button
					freeB+=1;
					time++;
				}
				else{
					//freeO is not enough
					freeB+=abs(x-o)+1-freeO;
					time+=abs(x-o)+1-freeO;
				}
				//Now Orange has no freeTime
				freeO=0;
				o=x;
			}
			else{
				//If Blue is to go
				if (freeB>=abs(x-b)){
					//When freeB is enough
					//One second for pushing a button
					freeO+=1;
					time++;
				}
				else{
					//freeB is not enough
					freeO+=abs(x-b)+1-freeB;
					time+=abs(x-b)+1-freeB;
				}
				//Now Blue has no freeTime
				freeB=0;
				b=x;
			}

		}
		fprintf(out,"Case #%d: %d\n",t+1,time);
	}
	return 0;
}

