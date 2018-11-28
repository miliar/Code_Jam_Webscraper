#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int no=1;no<=T;no++) {
		int N;
		cin >> N;
		
		char map[110][110];
		for(int i=0;i<N;i++) {
			cin >> map[i];
		}
		
		double WP[110], win[110], lose[110];
		for(int i=0;i<N;i++) {
			win[i] = 0, lose[i] = 0;
			for(int j=0;j<N;j++) {
				if(map[i][j]=='1') win[i]++;
				else if(map[i][j]=='0') lose[i]++;
			}
			WP[i] = (double)win[i]/(win[i]+lose[i]);
		}
		
		double OWP[110];
		for(int i=0;i<N;i++) {
			int count = 0;
			OWP[i] = 0;

			for(int j=0;j<N;j++) {
				double wp;
				if(map[j][i]=='1') {
					count++;
					OWP[i] += wp = (double)(win[j]-1)/(win[j]+lose[j]-1);
				} else if(map[j][i]=='0') {
					count++;
					OWP[i] += wp = (double)(win[j])/(win[j]+lose[j]-1);
				}
			}
			OWP[i] /= count;
		}
		
		double OOWP[110];
		for(int i=0;i<N;i++) {
			int count = 0;
			OOWP[i] = 0;
			for(int j=0;j<N;j++) {
				if(map[i][j]!='.') {
					count++;
					OOWP[i] += OWP[j];
				}
			}
			OOWP[i] /= count;
		}
		
		cout << "Case #" << no << ":" << endl;
		for(int i=0;i<N;i++) {
			double RPI = 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i];
			printf("%.6f\n", RPI);
		}
	}
	return 0;
}
