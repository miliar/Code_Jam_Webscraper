#include <stdlib.h>
#include <fstream>

using namespace std;

int main(void){
    ifstream infile("B.in");
    ofstream outfile("B.out");    

    int T;
    infile >> T;

    for (int j = 1; j <= T; j++){
    	int N;
	int s;
	int p;
	
	infile >> N;
	infile >> s;
	infile >> p;

	int numThere = 0;
	int numClose = 0;

	for (int i = 0; i < N; i++){
	    int totalScore;
	    infile >> totalScore;
	    
	    int bestScore = (totalScore+2) / 3;
	    if (bestScore >= p)
	       numThere++;
	    else if (bestScore == p - 1 && totalScore % 3 != 1 && totalScore >= 2 && totalScore <= 28)
	    	 numClose++;
	}

	int answer;
	if (numClose > s)
	   answer = numThere + s;
	else
	   answer = numThere + numClose;

	outfile << "Case #" << j << ": " << answer << endl;
    }


    outfile.close();

    return 0;
}
