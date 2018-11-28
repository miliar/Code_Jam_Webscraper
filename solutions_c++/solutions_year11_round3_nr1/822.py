#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main(int artc, char* argv[]) {

    int TIME;// number of test
    int answer;// Final answer
    cin >> TIME;
    int R,C;
    int table[50][50];
    int old[50][50];
    int label[50][50];
    char tmp;
    for (int t = 0 ; t < TIME; t++) {
	answer = 0;
	cin >> R >> C;
	for (int i = 0 ; i < R; ++i) {
	    for (int j = 0 ;j < C; ++j) {
		cin >> tmp;
		if (tmp=='.') old[i][j] = 0;
		if (tmp=='#') old[i][j] = 1;
		label[i][j] = 0;
	    }
	}

	int flag;

	flag = 1;

	for (int i = 0 ; i < R; ++i) {
	    for (int j = 0 ; j < C; ++j){
		if (old[i][j] == 0) {
		    table[i][j] = 0;
		    label[i][j] = 1;
		    continue;
		}
		if (old[i][j] == 1) {
		    if (label[i][j] == 0) {
			if ((i+1 < R && old[i+1][j] == 1) &&
				(j+1 < C && old[i][j+1] == 1) &&
			    (i+1 < R && j+1 < C && old[i+1][j+1] == 1) 	) {
			    table[i][j] = table[i+1][j+1] = 2;
			    table[i+1][j] = table[i][j+1] = 3;
			    label[i][j] = label[i][j+1]= label[i+1][j]= label[i+1][j+1] = 1;
			}
			else {
			    flag = 0;
			}
		    }
		}
	    }
	}

	//output
	printf("Case #%d:\n",t+1);
	if (flag==1) {
	    for (int i = 0 ;i < R; ++i) {
		for (int j = 0 ; j < C; ++j){
		    switch (table[i][j]) {
			case 0: cout << ".";
				break;
			case 2: cout <<"/"; break;
			case 3: cout <<"\\"; break;
		    }
		}
		cout << endl;
	    }
	}
	else {
	    cout << "Impossible\n";
	}
    }
    return 0;
}
