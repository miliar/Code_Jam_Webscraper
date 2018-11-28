#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

double getOWP(int win, int tot, int game)
{
	if(game<0) return ((double)win)/tot;
	if(game>0) return ((double)(win))/(tot-1);
	if(game==0) return ((double)(win-1))/(tot-1);
	return 0;
}

void TC(int T)
{
    int N = 0;
    cin >> N;
    if(N<=0) {
        cerr << "N<=0" << endl;
        return;
    }
    vector<int> games = vector<int>(N*N);
    vector<int> Win = vector<int>(N);
    vector<int> Tot = vector<int>(N);
   	vector<double> OWP = vector<double>(N);
    vector<vector<int> > opps = vector<vector<int> >(N);
//    vector<double> RPIs = vector<double>(N);
    for(int i = 0; i < N; ++i){
    	int win = 0, lose = 0;
	    for(int j = 0; j < N; ++j){
	        char ch;
	        cin >> ch;
	        switch(ch) {
	            case '0': games[i*N+j] = 0; ++lose; opps[i].push_back(j); break;
	            case '1': games[i*N+j] = 1; ++win; opps[i].push_back(j); break;
	            case '.': games[i*N+j] = -1; break;
	            default: cerr << "???" << endl; return;
	        }
	    }
	    Win[i] = win;
	    Tot[i] = win + lose;
    }
    // ...!!!
    for(int i = 0; i < N; ++i){
    	size_t O = Tot[i];
		double OWPs = 0;
    	for(size_t j = 0; j < O; ++j){
	    	OWPs += getOWP(Win[opps[i][j]], Tot[opps[i][j]], games[i*N+opps[i][j]]);
    	}
    	OWP[i] = OWPs / O;
    }
    cout << "Case #" << (T + 1) <<":" << endl;
    for(int i = 0; i < N; ++i){
    	size_t O = Tot[i];
		double RPI = 0, OWPs = 0;
		// WP
		RPI += (0.25 * Win[i] / O);
		//OWP
		RPI += (0.5 * OWP[i]);
		//OOWP
    	for(size_t j = 0; j < O; ++j){
			OWPs += OWP[opps[i][j]];
    	}
    	RPI += (0.25 * OWPs / O);
//        cout << RPIs[i] << endl;
        printf("%.12f\n", RPI);
    }
}

int main()
{
    int N = 0;
    cin >> N;
    for(int i = 0; i < N; ++i) {
        TC(i);
    }
    return 0;
}
