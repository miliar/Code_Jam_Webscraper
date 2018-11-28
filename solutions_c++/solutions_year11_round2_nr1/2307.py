#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	ifstream f;
	f.open("in");
	int tcn;
	f >> tcn;
	for( int i=0; i<tcn; i++) {
		int teamsn;
		f >> teamsn;
		char board[101][101]= {0};
		int wins[101]={0};
		int loses[101] ={0};
		for(int j=0; j<teamsn; j++) {
			for(int k=0; k<teamsn; k++) {
				char a;
				f >> a;
				board[j][k] = a;
				if(a=='1') {
					wins[j]++;
				}
				else if(a=='0') {
					loses[j]++;
				}
			}
		}

		//get wop
		float wops[101] = {0.0};
		for(int j=0; j<teamsn; j++) { //each teams
			vector<float> ops_wps;
			for(int k=0; k<teamsn; k++) {
				if(board[j][k] != '.') {
					//this is opponent.
					float ops_wp;
					if(board[j][k] == '1') {
						ops_wp = wins[k]/(wins[k]+loses[k]-1.0);
						ops_wps.push_back(ops_wp);
					}
					else if(board[j][k] == '0') {
						ops_wp = (wins[k]-1.0)/(wins[k]+loses[k]-1.0);
						ops_wps.push_back(ops_wp);
					}
				}
			}
			float sum=0;
			for(int k=0;k<ops_wps.size(); k++) {
				sum += ops_wps[k];
			}
			float wop = sum / ops_wps.size();
			wops[j] = wop;
		}

		//get oowp
		float oowps[101];
		for(int j=0; j<teamsn; j++) {
			int my_ops=0;
			float sum = 0.0;
			for(int k=0; k<teamsn; k++) {
				if(board[j][k] != '.') { //my op.
					sum += wops[k];
					my_ops++;
				}
			}

			oowps[j] = sum/my_ops;
		}

		cout << "Case #" << i+1 << ":" << endl;
		for(int j=0; j<teamsn; j++) {
			cout << 0.25*((float)wins[j]/(wins[j]+loses[j])) +
				0.50*wops[j] + 0.25*oowps[j] << endl;
		}
	}
}
					
						
					
		
