#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

typedef enum
{
    POSSIBLE,
    SURPRISING,
    IMPOSSIBLE
} Possibility;

Possibility possibleScore( int score, int p, bool surprising )
{
    int scorePos = score - 3*p;

    if( score < p )
    {
        return IMPOSSIBLE;
    }

    if( (abs(scorePos) == 4 || abs(scorePos) == 3) && surprising )
    {
        return SURPRISING;
    }

    if( scorePos <= -3 )
    {
        return IMPOSSIBLE;
    }

    return POSSIBLE;
}

int solve( int N, int S, int p, const vector<int>& scores )
{
    int result = 0;
    for( size_t i=0; i < scores.size(); i++ )
    {
        Possibility scorePoss = possibleScore( scores[i], p, S != 0 );
        if( scorePoss == POSSIBLE   )
        {
            ++result;
        }
        else if( scorePoss == SURPRISING )
        {
            ++result;
            --S;
        }
    }
    return result;
}

int main()
{
    ifstream input("B-large.in");
    ofstream output("output.txt");
    unsigned int N;
    input >> N;

    vector<int> scores;
    scores.reserve( 128 );
    for( unsigned int i=1; i <= N; i++ )
    {
        output << "Case #" << i << ": ";

        int googlers, surprisingScores, p;
        input >> googlers >> surprisingScores >> p;

        scores.resize( googlers );
        for( unsigned int j=0; j < googlers; j++ )
        {
            int score;
            input >> score;
            scores[j] = score;
        }

        int result = solve( googlers, surprisingScores, p, scores );

        output << result << endl;
    }

    return 0;
}
