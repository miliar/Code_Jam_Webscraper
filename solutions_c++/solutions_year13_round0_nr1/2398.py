#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void){
	int T;
	cin >> T;
	char P[2] = {'X','O'};
	vector<string> b(4);
	for(int t=1;t<=T;t++){
		cout << "Case #"<<t<<": ";
		for(int i=0;i<4;i++)
			cin >> b[i];
		bool won = false;
		for(int p=0;p<2;p++){
			for(int i=0;i<4;i++){
				won = true;
				for(int j=0;j<4;j++)
					if(b[i][j] != 'T' && b[i][j] != P[p]) won = false;
				if(won)break;
			}
			if(won){ cout << P[p] << " won" << endl; break; }
			
			for(int i=0;i<4;i++){
				won = true;
				for(int j=0;j<4;j++)
					if(b[j][i] != 'T' && b[j][i] != P[p]) won = false;
				if(won)break;
			}
			if(won){ cout << P[p] << " won" << endl; break; }
			
			won = true;
			for(int i=0;i<4;i++)
				if(b[i][i] != 'T' && b[i][i] != P[p]) won = false;
			if(won){ cout << P[p] << " won" << endl; break; }
			
			won = true;
			for(int i=0;i<4;i++)
				if(b[3-i][i] != 'T' && b[3-i][i] != P[p]) won = false;
			if(won){ cout << P[p] << " won" << endl; break; }
		}
		if(won) continue;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				if(b[i][j]=='.')won=true;
		}
		if(!won) cout << "Draw" << endl;
		else cout << "Game has not completed" << endl;
	}
}