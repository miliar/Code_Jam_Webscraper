#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>

using namespace std;

int main(){
	freopen("A-large.in","rt", stdin);
	freopen("A-large.out","wt",stdout);
	int T, N;
	cin>>T;
    string lines[100];
    int gamesPlayed[100];
    int gamesWon[100];
    double WP[100];
    double OWP[100];
    double OOWP[100];
    int oppenents[100][100];

	for(int t = 0; t<T; t++){
		printf("Case #%d:\n", t+1);
        cin>>N;
        for(int n = 0; n<N; n++) {
            cin>>lines[n];
            gamesPlayed[n] = 0;
            gamesWon[n] = 0;
            for(int n2 = 0; n2<N; n2++) {

                char a = lines[n][n2];
                oppenents[n][n2] = 0;
                if(a=='1') {
                    gamesPlayed[n] += 1;
                    gamesWon[n] += 1;
                    oppenents[n][n2] = 2;
                }
                if(a=='0') {
                    gamesPlayed[n] += 1;
                    oppenents[n][n2] = 1;
                }
            }
            WP[n] = (double)gamesWon[n]/(double)gamesPlayed[n];
        }
        for(int n = 0; n<N; n++) {
            int count = 0;
            double totalOWP = 0;
            for(int n2 = 0; n2<N; n2++) {
                if(oppenents[n2][n] == 1) {
                    count++;
                    double tempWP = double(gamesWon[n2])/double(gamesPlayed[n2] - 1);
                    totalOWP += tempWP;
                }else if(oppenents[n2][n] == 2) {
                    count++;
                    double tempWP = double(gamesWon[n2] - 1)/double(gamesPlayed[n2] - 1);
                    totalOWP += tempWP;
                }
            }
            OWP[n] = totalOWP/count;
        }

        for(int n = 0; n<N; n++) {
            int count = 0;
            double totalOOWP = 0;
            for(int n2 = 0; n2<N; n2++) {
                if(oppenents[n][n2] > 0) {
                    count++;
                    totalOOWP += OWP[n2];
                }
            }
            OOWP[n] = totalOOWP/count;
        }
        for(int n = 0; n<N; n++) {
            //cout<<lines[n]<<"\n";
            //cout<<"GamesWon = "<<gamesWon[n]<<"\n";
            //cout<<"GamesPlayed = "<<gamesPlayed[n]<<"\n";
            //cout<<"WP = "<<WP[n]<<"\n";
            //cout<<"OWP = "<<OWP[n]<<"\n";
            //cout<<"OOWP = "<<OOWP[n]<<"\n";

            double RPI = 0.25*WP[n] + 0.5*OWP[n] + 0.25*OOWP[n];
            printf("%.12g\n",RPI);
            //cout<<RPI<<"\n";
        }
        //cout<<"\n";
	}
	return 0;
}