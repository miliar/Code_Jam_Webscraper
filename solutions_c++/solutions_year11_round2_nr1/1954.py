#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
using namespace std;
int N;

class team{
	public:
		int win;
		int lose;
		int n_opp;
		double WP;
		double OWP;
		double OOWP;
		double RPI;
		int opp[200];
		void get_OWP(int );
		void get_OOWP();
		void get_RPI();
		team(string info);
};

	vector<team> NCAA;

team::team(string info){
	int i;
	lose = win =n_opp=0;
	WP = OWP = OOWP =RPI=0.0;
	memset(opp,0,sizeof(opp));

	for(i=0;i<info.length();i++){
		if(info[i]=='0'){
			opp[i] = -1;		
			lose++;
		}
		else if(info[i] =='1'){
			opp[i] = 1;
			win++;
		}
	}
	n_opp = lose+win;
	WP = (double)win/(double)(win+lose);
}
void team::get_OWP(int which){
	int i;
	double sum=0;
	for(i=0;i<N;i++){
		if(this->opp[i] == 1){
			sum+=(double)(NCAA[i].win)/(double)(NCAA[i].lose+NCAA[i].win-1);
		}
		else if(this->opp[i] == -1)
			sum+=(double)(NCAA[i].win-1)/(double)(NCAA[i].lose+NCAA[i].win-1);
	}
	sum/= (double)n_opp;

	this->OWP=sum;

}
void team::get_OOWP(){
	int i;
	double sum=0;
	for(i=0;i<N;i++){
		if(this->opp[i]!=0){
			sum+=NCAA[i].OWP;
		}
	}
	sum/=(double)n_opp;
	this->OOWP = sum;
}
void team::get_RPI(){
this->RPI = 0.25*WP+0.5*OWP+0.25*OOWP;
}
int main(){
	int T;
	int i,j,k;
	string in;
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		NCAA.clear();
		scanf("%d",&N);
		for(j=0;j<N;j++){
			cin >> in;
			NCAA.push_back(team(in));	
		}
		for(j=0;j<N;j++){
			NCAA[j].get_OWP(j);
		}
		for(j=0;j<N;j++){
			NCAA[j].get_OOWP();
		}
		for(j=0;j<N;j++){
			NCAA[j].get_RPI();
		}

		printf("Case #%d:\n",i);
		for(j=0;j<N;j++){
			printf("%lf\n",NCAA[j].RPI);
		}

	}

	return 0;


}
