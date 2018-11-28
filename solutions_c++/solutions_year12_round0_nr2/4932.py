#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int bestResultsGooglers ( const string & );

int main ()
{
    unsigned int test_cases;
    string line;

    cin >> test_cases;
    cin.ignore ();
    int actual_case = 1;
    for ( unsigned int i = 0; i < test_cases; ++i )
    {
        getline ( cin, line );
        cout << "Case #" << actual_case << ": " << bestResultsGooglers ( line );
        cout << "\n";
        actual_case += 1;
    }
    return 0;
}

int bestResultsGooglers ( const string &line )
{
    istringstream iss ( line );
    int N, S, P;
    vector<int> googlers_vector;
    iss >> N;
    iss >> S;
    iss >> P;
    int total_points;
    for ( int x = 0; x < N; ++x )
    {
        iss >> total_points;
        googlers_vector.push_back ( total_points );
    }
    int total_googlers = 0;
    int score_1, score_2, score_3, mod;
    int surprising_triplets = 0;
    for ( int x = 0; x < N; ++x )
    {
        if ( googlers_vector[x] >= 3 )
        {
            mod = (googlers_vector[x] % 3);
            score_1 = score_2 = score_3 = (googlers_vector[x] / 3);
        }
        else
        {
            mod = 0;
            if ( googlers_vector[x] == 2 )
            {
                score_1 = score_2 = 1;
                score_3 = 0;
            }
            else
            {
                score_1 = googlers_vector[x];
                score_2 = score_3 = 0;
            }
        }

        if ( score_1 >= P )
        {
            total_googlers += 1;
        }
        else if ( (score_1 + 1) == P )
        {
            if ( mod == 0 )
            {
                if ( ( score_2 >= 1 || score_3 >= 1 )  && surprising_triplets < S )
                {
                    surprising_triplets += 1;
                    total_googlers += 1;
                }
            }
            else if ( mod >= 1 )
                total_googlers += 1;
        }
        else if ( (score_1 + 2) == P )
        {
            if ( mod == 2 && surprising_triplets < S )
            {
                surprising_triplets += 1;
                total_googlers += 1;
            }
        }
        //else is lower than P, and isn't possible being equal or bigger
    }
    return total_googlers;
}
