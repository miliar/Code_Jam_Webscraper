#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)

using namespace std;

int main(){
	int T;cin>>T;
	for(int tt=1 ; tt<=T ; tt++){
		int N;cin>>N;
		vector<string> sch;
		sch.resize(N);
		REP(i,N)cin>>sch[i];

		vector<double> WP;WP.resize(N);
		REP(i,N){
			double a = 0;
			double b = 0;
			REP(j,N){
				if(sch[i][j]=='1'){a+=1;b+=1;}
				else if(sch[i][j]=='0'){b+=1;}
			}
			WP[i] = a/b;
		}

		vector<double> OWP;OWP.resize(N);
		REP(i,N){
			double c = 0;
			double d = 0;
			REP(j,N){
				if(i==j)continue;
				if(sch[i][j]=='0' || sch[i][j]=='1'){
					double a = 0;
					double b = 0;
					REP(k,N){
						if(k==i)continue;
						if(sch[j][k]=='1'){a+=1;b+=1;}
						else if(sch[j][k]=='0'){b+=1;}
					}
					c += a/b;
					d += 1;
				}
			}
			OWP[i] = c/d;
		}

		vector<double> OOWP;OOWP.resize(N);
		REP(i,N){
			double a = 0;
			double b = 0;
			REP(j,N){
				if(sch[i][j]=='0' || sch[i][j]=='1'){
					a += OWP[j];
					b += 1;
				}
			}
			OOWP[i] = a/b;
		}

		vector<double> res;res.resize(N);
		REP(i,N)res[i] = 0.25*WP[i]+0.50*OWP[i]+0.25*OOWP[i];

		printf("Case #%d:\n",tt);
		REP(i,N){
			printf("%.9f\n",res[i]);
		}
	}
	return 0;
}