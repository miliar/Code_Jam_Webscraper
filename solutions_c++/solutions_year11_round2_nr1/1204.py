#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <queue>
#include <set>
#include <map>
#include <vector>

using namespace std;

struct team{
	double fights, wins;
	double owp;
	double oowp;
	double ooowp;
	double rpi(){
		return 0.25 * owp + 0.50 * oowp + 0.25 * ooowp;
	}
} teams[101];

char res[101][101];

int main(){
	int cases, s;
	scanf("%d",&cases);
	for(int c=1; c<=cases; ++c){
		scanf("%d",&s);
		for(int i=0; i<s; ++i){
			teams[i].fights=teams[i].wins=0;
			scanf("%s",res[i]);
			for(int j=0; j<s; ++j){
				if(res[i][j]=='0'){
					++teams[i].fights;
				}
				if(res[i][j]=='1'){
					++teams[i].fights;
					++teams[i].wins;
				}
			}
			//printf("Wins=%lf,Losses=%lf\n",teams[i].wins,teams[i].fights);
			teams[i].owp=teams[i].wins/teams[i].fights;
			//printf("Team %c has owp=%.2lf\n",i+'A',teams[i].owp);
		}
		for(int i=0; i<s; ++i){
			double oowp=0;
			int ts=0;
			for(int j=0; j<s; ++j){
				if(res[j][i]=='.') continue;
				++ts;
				if(res[j][i]=='0'){
					oowp+=teams[j].wins/(teams[j].fights-1);
				}
				if(res[j][i]=='1'){
					oowp+=(teams[j].wins-1)/(teams[j].fights-1);
				}
			}
			teams[i].oowp=oowp/ts;
			//printf("Team %c has oowp=%.2lf\n",i+'A',teams[i].oowp);
		}
		for(int i=0; i<s; ++i){
			double ooowp=0;
			int ts=0;
			for(int j=0; j<s; ++j){
				if(res[i][j]=='.') continue;
				++ts;
				ooowp+=teams[j].oowp;
			}
			teams[i].ooowp=ooowp/ts;
		}
		printf("Case #%d:\n",c);
		for(int i=0; i<s; ++i){
			printf("%.8lf\n",teams[i].rpi());
		}	

	}

	return 0;
}

