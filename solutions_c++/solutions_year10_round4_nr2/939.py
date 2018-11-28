#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair
int M[2000];
int R[2000];

bool zeros(int P){
	for (int i=0; i<(1<<P) ; i++) {
		if(M[i]) return false;
	}
	return true;
}

int least(int P){
	int cost = 0;
	int teams = (1<<P);
	while(!zeros(P)){
		for(int rounds = 0;!zeros(P) && rounds<(1<<P)/teams;rounds++){
			bool ok=false;
			for(int k=rounds*teams; k<(rounds+1)*(teams);k++){
				if(M[k]){ok=true; M[k]--;}
			}
			if(ok)cost++;
		}
		teams>>=1;
		if(teams<2) break;
	}
	
	/*for (int i= 0; !zeros(P) && i<(1<<P)/round; i++) {
		for (int j=i*round; j<(i+1)*round; j++) {
			if(M[j])M[j]--;
		}
		cost++;
		round>>=1;
		if(round<2) break;
	}*/
	
	return cost;
}

int main(){
	int K; cin>>K; K++;
	for (int k=1; k<K ; k++) {
		int P; cin>>P; int teams = (1<<P); //cout<<"TEAMS: "<<teams<<endl;
		for (int i=0; i<teams; i++) {
			cin>>M[i]; M[i] = P-M[i];
		}
		for (int p=0; p<teams-1 ;p++ ) {
			cin>>R[p];
		}
		
		cout<<"Case #"<<k<<": "<<least(P)<<endl;
	}
}