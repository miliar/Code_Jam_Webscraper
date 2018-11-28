
#include <vector>

#include <fstream>
#include <iostream>


static int solve( int surprises,
                  int highScore,
                  std::vector<int> &scores )
{
    int goodScore = 0;

    for(int i=0; i<scores.size(); ++i)
    {
        int score = scores[i];

        int remainder = score - highScore;
        
        // Not surprising, good to go
        if( remainder >= (highScore-1)*2 )
        {
            goodScore++;
        }
        // Surprising
        else if( (surprises > 0) && (remainder >= (highScore-2)*2) )
        {
            surprises--;
            goodScore++;
        }

    }

    return goodScore;
}


int main( int argc, char **argv )
{
    std::ifstream input(argv[1]);

    int cases = 0;

    input >> cases;

    for(int i=0; i<cases; ++i)
    {
        int numDancers = 0;
        int surprises = 0;
        int highScore = 0;
        std::vector<int> scores;

        input >> numDancers;
        input >> surprises;
        input >> highScore;

        for(int k=0; k<numDancers; ++k)
        {
            int score = 0;
            input >> score;

            if( score >= highScore )
            {
                scores.push_back(score);
            }
        }

        std::cout << "Case #" << i+1 << ": ";

        int goodScores = solve( surprises,
                                highScore,
                                scores );

        std::cout << goodScores << std::endl;
    }


    return 0;
}

