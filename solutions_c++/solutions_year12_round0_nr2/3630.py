// code_jam2012-2-dancing.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
using namespace std;

int dancing(int N, int S, int p, int * score)
{
    int count(0);
    if (p==0)
        return N;

    int highScore = 3*p-2;
    int midScore  = highScore - 2;
    if (midScore < p)
        midScore = p;

    for (int i=0; i<N; i++) {
        if (score[i]>=highScore)
            count++;
        else {
            if (S > 0 && score[i] >=midScore) {
                S--;
                count++;
            }
        }
    }

    return count;
}


int main(int argc, char * argv[])
{
    int score[100];

    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    clock_t start_clock = clock();

    int T;
    fin >> T;

    int case_no = 0;
    for (int i=0; i<T; i++) {
        int N, S, p;
        fin >> N >> S >> p ;
        for (int j=0; j<N; j++) 
            fin>>score[j];

        int ans = dancing(N, S, p, score);
        fout << "Case #" << ++case_no << ": " << ans << endl;
    }
    clock_t end_clock = clock();
    // cout << (end_clock - start_clock) / double(CLOCKS_PER_SEC) << endl;

	return 0;
}

