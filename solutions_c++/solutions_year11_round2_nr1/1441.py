#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

int main(){
	int i=0, n;
	cin >> n;
	while(++i<=n){
		int team_num;
		double result;

		int j=0;
		vector<string> team_row;
		string sbuf;
		cin >> team_num;
		while(++j<=team_num){
			cin >> sbuf;
			team_row.push_back(sbuf);
		}
		vector<double> opponent_num(team_num), WN(team_num), OWP(team_num), OOWP(team_num);
		
		for(int k=0;k<team_num;k++){
			WN[k]=0;
			for(int l=0;l<team_num;l++){
				if(team_row[k][l]=='1'){
					WN[k]+=1;
				}
				if(team_row[k][l]!='.'){
					opponent_num[k]+=1;
				}
			}
			//		cout << "WN" << WN[k] << endl;
		}

		for(int k=0;k<team_num;k++){
			OWP[k]=0;
			for(int l=0;l<team_num;l++){
				if(team_row[k][l]=='0'){
					OWP[k]+=(WN[l]-1)/(opponent_num[l]-1);
				}
				if(team_row[k][l]=='1'){
					OWP[k]+=WN[l]/(opponent_num[l]-1);
				}
			}
			OWP[k]/=opponent_num[k];
					//cout << "OWP" << OWP[k] << endl;
		}

		for(int k=0;k<team_num;k++){
			OOWP[k]=0;
			for(int l=0;l<team_num;l++){
				if(team_row[k][l]!='.'){
					OOWP[k]+=OWP[l];
				}
			}
			OOWP[k]/=opponent_num[k];
					//cout << "OOWP" << OOWP[k] << endl;
		}
		
		cout << "Case #" << i <<": " << endl;
		for(int k=0;k<team_num;k++){/*
					cout << "WN" << WN[k] << endl;
					cout << "OWP" << OWP[k] << endl;
					cout << "OOWP" << OOWP[k] << endl;*/
			result = 0.25*WN[k]/opponent_num[k] + 0.5*OWP[k] + 0.25*OOWP[k];
			cout << result <<endl;
		}
	}
	return 0;
}