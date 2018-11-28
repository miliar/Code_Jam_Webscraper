#include <fstream>
using namespace std;

void main(){
	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("A-large.out");
	int T;
	in>>T;
	for(int cases=0;cases<T;cases++){
		int N;
		in>>N;
		char schedule[100][101];
		for(int teams=0;teams<N;teams++) in>>schedule[teams];
		//Winning Percentage (WP)
		double WP[100];
		int WPTotal[100];
		for(int teams=0;teams<N;teams++){
			WP[teams]=0;
			int total=0;
			for(int matches=0;matches<N;matches++){
				if(schedule[teams][matches]=='1'){
					WP[teams]+=1;
					total++;
				}else if(schedule[teams][matches]=='0'){
					total++;
				}
			}
			WP[teams]/=total;
			WPTotal[teams]=total;
		}
		//Opponents' Winning Percentage (OWP)
		double OWP[100];
		for(int teams=0;teams<N;teams++){
			OWP[teams]=0;
			int total=0;
			for(int matches=0;matches<N;matches++){
				if(schedule[teams][matches]=='1'){
					double temp=WP[matches]*WPTotal[matches];
					OWP[teams]+=temp/(WPTotal[matches]-1);
					total++;
				}else if(schedule[teams][matches]=='0'){
					double temp=WP[matches]*WPTotal[matches];
					OWP[teams]+=(temp-1)/(WPTotal[matches]-1);
					total++;
				}
			}
			OWP[teams]/=total;
		}
		//Opponents' Opponents' Winning Percentage (OOWP)
		double OOWP[100];
		for(int teams=0;teams<N;teams++){
			OOWP[teams]=0;
			int total=0;
			for(int matches=0;matches<N;matches++){
				if(schedule[teams][matches]=='1'||schedule[teams][matches]=='0'){
					OOWP[teams]+=OWP[matches];
					total++;
				}
			}
			OOWP[teams]/=total;
		}
		//Print Case
		out<<"Case #"<<(cases+1)<<":"<<endl;
		//RPI
		double RPI;
		out.setf(ios::fixed,ios::floatfield);
		out.precision(10);
		for(int teams=0;teams<N;teams++){
			RPI=(0.25*WP[teams])+(0.50*OWP[teams])+(0.25*OOWP[teams]);
			out<<RPI<<endl;
		}
	}
	in.close();
	out.close();
}