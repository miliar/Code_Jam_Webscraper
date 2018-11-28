#include<iostream>
#include<cstdio>

using namespace std;

int main(int artc, char* argv[]) {

    int TIME;// number of test
    int answer;// Final answer
    cin >> TIME;
    double score[100];
    int N;
    int game[100][100];
    int meet[100][100];
    int WP[100];
//    int OWP[100];
//    int OOWP[100];
    int ngame[100];
    char tmp;
    for (int t = 0 ; t < TIME; t++) {
	cin >> N;
//	cout << "WP" << endl;
	for (int i = 0 ; i < N; ++i) {
	    ngame[i] = 0;
		WP[i] = 0;
	    for (int j = 0 ; j < N; ++j) {
		cin >> tmp;
		if (tmp=='0') {
		    game[i][j] = 0;
		    meet[i][j] = 1;
		    ngame[i]++;
		}
		if (tmp=='1') {
		    game[i][j] = 1;
		    meet[i][j] = 1;
		    ngame[i]++;
		    WP[i]++;
		}
		if (tmp=='.') {	
		    game[i][j] = -1;
		    meet[i][j] = 0;
		}
//		cout << game[i][j] <<"\t";
	    }
//	    cout << endl;
//	    cout << ngame[i] <<"\t"<<(double)WP[i] / (double)ngame[i] << endl;
	}
	double OWP[100][100];
	double final_OWP[100];

//	cout << endl;
//	cout << "OP" << endl;
	for (int i = 0 ; i < N; ++i) {
	    final_OWP[i] = 0.0;
	    for (int j = 0 ; j < N; ++j) {
		if (i==j) continue;
		if (meet[i][j] == 0) continue;
		OWP[i][j] = (double) (WP[j] - game[j][i]) / (ngame[j] - 1);
		final_OWP[i] += OWP[i][j];
	    }
	     final_OWP[i] /= (double) (ngame[i]);
//	     cout << final_OWP[i] << endl;
	}

	double OOWP[100];
//	cout << "OOWP" << endl;

	for (int i = 0 ; i < N; ++i) {
	    OOWP[i] = 0.0;
	    for (int j = 0 ;j < N; ++j) {
		if (i==j) continue;
		if (meet[i][j] == 0) continue;
		OOWP[i] += final_OWP[j];
	    }
	    OOWP[i] /= (double) (ngame[i]);
//	     cout << OOWP[i] << endl;
	}

	//output
	printf("Case #%d:\n", t+1);
	for (int i = 0 ; i < N ; ++i) {
	    printf("%lf\n",0.25 * (double)WP[i]/ ngame[i]+0.50* final_OWP[i] + 0.25 * OOWP[i]);
	}
    }
    return 0;
}
