#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main(){

	freopen("A-large.in","r",stdin);
	freopen("outA.txt","w",stdout);

	bool finished=false;

	int cases,outCases=0;
	cin >> cases;

	for(;cases>0;cases--){
		++outCases;
		int buttons;

		vector<int> orange,blue;
		vector<char> robot;
		
		cin >> buttons;
		int lposO=1,lposB=1;
		for(int i=0;i<buttons;i++){
			char ch;
			int btn;
			cin >> ch >> btn;
			if(ch=='O'){
				orange.push_back(abs(btn-lposO));
				lposO=btn;
			}else{
				blue.push_back(abs(btn-lposB));
				lposB=btn;
			}

			robot.push_back(ch);
		}

		int cO=0,cB=0;
		int seconds=0;
		for(int cBtn=0;cBtn<buttons;seconds++){
			if(robot[cBtn]=='O'){
			// if orange is pushing the button
				if(orange[cO] == 0){
					cO++;
					cBtn++;
				}else{
					orange[cO]--;
				}

				if( blue.size()>0 && blue[cB]>0 )  // if needed move
					blue[cB]--;
			}else{
			// blue is pushing the button
				if(blue[cB] == 0){
					cB++;
					cBtn++;
				}else{
					blue[cB]--;
				}

				if( orange.size()>0 && orange[cO]>0 )	// if needed move
					orange[cO]--;
			}
		}

		cout << "Case #"<<outCases<<": "<<seconds<<endl;
	}// end cases


	return 0;
}
