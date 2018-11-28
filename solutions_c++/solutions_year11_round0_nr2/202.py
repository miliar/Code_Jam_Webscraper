#include<iostream>
using namespace std;

char combine[8][8];
bool oppose[8][8]; 
bool exists[8];
char seq[100];
int currSeq;

int i(char a) {
    switch(a) {
	    case 'Q': return 0;
		case 'W': return 1;
		case 'E': return 2;
		case 'R': return 3;
		case 'A': return 4;
		case 'S': return 5;
		case 'D': return 6;
		case 'F': return 7;
	}
	return -1;
}

void clearRound() {
    for(int i=0; i<8; i++) {
	    for(int j=0; j<8; j++) {
		    combine[i][j]=0;
			oppose[i][j]=false;
		}
		exists[i]=false;
	}
	currSeq = 0;
}

bool clearSeq() {
    for(int i=0; i<8; i++) {
	    exists[i] = false;
	}
	currSeq = 0;
}

int main() {
    int T, Cs=1;
	cin >> T;
	
	while(T--) {
	    clearRound();
	    int C, D, N, k;
		cin >> C;
		
		char string[101];
		while(C--) {
		    cin >> string;
			combine[i(string[0])][i(string[1])] = string[2];
			combine[i(string[1])][i(string[0])] = string[2];
		}
		
		cin >> D;
		while(D--) {
		    cin >> string;
			oppose[i(string[0])][i(string[1])] = true;
			oppose[i(string[1])][i(string[0])] = true;
		}
		
		cin >> N;
		cin>>string;
		for(k=0; k<N; k++) {
		    char e = string[k];
			if(currSeq != 0) {
			    char prev = seq[currSeq-1];
				if(i(prev) != -1 && combine[i(e)][i(prev)] != 0) {
				    seq[currSeq-1] = combine[i(e)][i(prev)];
					continue;
				}
				
				int j;
				for(j=0; j<currSeq; j++) {
				    char check = seq[j];
					if(i(check) == -1) continue;
				    if(oppose[i(e)][i(check)] == true) {
					    break;
					}
				}
				
				if(j == currSeq) {
				    seq[currSeq++] = e;
					continue;
				} else {
				    clearSeq();
					continue;
				}
			} else {
			    seq[currSeq++] = e;
			}
		}
		
		cout << "Case #" << Cs++ << ": [";
		for(k=0; k<currSeq-1; k++) {
		    cout<<seq[k] << ", ";
		}
		
		if(currSeq > 0) {
		    cout<<seq[currSeq-1];
		}
		
		cout << "]" << endl;
	}
}
