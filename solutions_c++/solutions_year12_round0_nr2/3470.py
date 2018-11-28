#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int T;
    std::cin >> T;
    ++T;//test cases are indexed from 1

    for( int test_case=1 ; test_case<T ; ++test_case )
    {
    //Prep
        unsigned short num_dancers,surprising_scores,p;
        std::cin >> num_dancers >> surprising_scores >> p;

        std::vector<unsigned short> t(num_dancers);
        for( unsigned short i=0 ; i<num_dancers ; ++i)
        { std::cin >> t[i]; }

    //Work
        short score_for_unsurprising_pass = (3*p)-2; // p + (p-1) + (p-1)
        short score_for_surprising_pass   = (3*p)-4; // p + (p-2) + (p-2)

        //fix an edge case, else 0>=-1 implies possible suprising pass
        //but would actually require negative scores
        if( p==1 ) { score_for_surprising_pass = score_for_unsurprising_pass; }

        unsigned short unsurprising_passes = 0;
        unsigned short potential_surprising_passes = 0;

        for( unsigned short i=0 ; i<num_dancers ; ++i)
        {
            if( t[i] >= score_for_unsurprising_pass )
                ++unsurprising_passes;
            else if( t[i] >= score_for_surprising_pass )
                ++potential_surprising_passes;
        }

        unsigned short surprising_passes = std::min( potential_surprising_passes , surprising_scores );

        unsigned short passes = surprising_passes + unsurprising_passes;

    //Results
        std::cout << "Case #" << test_case << ": " << passes << std::endl;
    }
}
