#include <iostream>
using namespace std;


int main()
{
	int T;
	cin >> T;

	for (int t = 0; t < T; t++) {
		int com[256][3];
		int opp[256][2];

		int C,D;
		cin >> C;
		int cm = 0;
		for (int c = 0; c < C; c++) {
			char ch1,ch2,ch3;
			cin >> ch1>>ch2>>ch3;
			com[cm][0] = ch1;
			com[cm][1] = ch2;
			com[cm++][2] = ch3;
			com[cm][0] = ch2;
			com[cm][1] = ch1;
			com[cm++][2] = ch3;
		}
		cin >> D;
		int op = 0;
		for (int d = 0; d < D; d++) {
			char ch1,ch2;
			cin >> ch1 >> ch2;
			opp[op][0] = ch1;
			opp[op++][1] = ch2;
			opp[op][0] = ch2;
			opp[op++][1] = ch1;
		}

		int N;
		cin >> N;
		int items[200];
		int it = 0;
		for (int n = 0; n < N; n++) {
			char ch;
			cin >> ch;
			int i;
			for (i = 0; i < cm; i++) {
				if(it>0 && com[i][0]==ch && com[i][1] == items[it-1]){ 
					items[it-1] = com[i][2];
					break;	
				}
			}

			if(i==cm){
				items[it++] = ch;
			}

			bool clear = false;
			for (i = 0; i < op; i++) {
				if(opp[i][0] == items[it-1]){
					for (int j = 0; j < it; j++) {
						if(opp[i][1] == items[j]){
							clear = true;
							break;		
						}
					}	
				}
			}

			if(clear){
				for (i = 0; i < 200; i++) {
					items[i] = 0;
				}
				it = 0;
			}


		}
		
		cout<<"Case #"<<t+1<<": [";
		for (int i = 0; i < it; i++) {
			cout<<(char)items[i];
			if(i!=it-1)
				cout<<", ";
		}
		cout<<"]"<<endl;

	}
	
}
