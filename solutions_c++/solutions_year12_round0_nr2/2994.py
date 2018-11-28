#include <cassert>
#include <iostream>
#include <fstream>

using namespace std;

int count(int nJudges, int nSurprising, int qualifyScore, int* totalScore);

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    if(!fin.is_open())
        cerr << "Failed to open input file" << endl;
    if(!fout.is_open())
        cerr << "Failed to open output file" << endl;

    int nSamples;
    fin >> nSamples;
    for(int i = 0; i < nSamples; i++) {
        int nJudges;
        int nSurprising;
        int qualifyScore;
        fin >> nJudges >> nSurprising >> qualifyScore;
        int* totalScore = new int[nJudges];
        for(int j = 0; j < nJudges; j ++)
            fin >> totalScore[j];
        fout << "Case #" << i+1 << ": " << count(nJudges, nSurprising, qualifyScore, totalScore) << endl;
        cout << "Case #" << i+1 << ": " << count(nJudges, nSurprising, qualifyScore, totalScore) << endl;
        delete[] totalScore;
    }
    return 0;
}

int count(int nJudges, int nSurprising, int qualifyScore, int* totalScore) {
    assert(nJudges >0 && nSurprising >=0 && qualifyScore >=0 && totalScore);
    int lowScore = 3 * qualifyScore - 4;
    lowScore = lowScore > 0 ? lowScore : qualifyScore; // Below lowScore, not qualified
    int highScore = 3 * qualifyScore - 2; // Higher or equal to highScore, qualified without surprising
    highScore = highScore > 0 ? highScore : qualifyScore; // score within [lowScore, highScore) can be qualified with surprising
    int nQualify = 0;
    int nToBeDetermined = 0;
    for(int i = 0; i < nJudges; i ++) {
        if(totalScore[i] >= lowScore) {
            if(totalScore[i] >= highScore)
                ++nQualify;
            else
                ++nToBeDetermined;
        }
    }
    nQualify += nSurprising < nToBeDetermined ? nSurprising : nToBeDetermined;
    return nQualify;
}
