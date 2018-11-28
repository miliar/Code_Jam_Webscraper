#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
    unsigned int T,R,k,N; // run R times, k person per ride , N number of groups
    unsigned int temp;
    cin >> T;
    for(unsigned int i = 1; i <= T; i++)
    {
        cin >> R >> k >> N;

        vector<unsigned int> groups;

        temp = N;
        while(temp--)
        {
            unsigned int t;
            cin >> t;
            groups.push_back(t);
        }

        temp = R;
        while(temp--)
        {
            for(unsigned int i = 0; i < N; i++)
            {
                groups.push_back(groups[i]);
            }
        }

        // generate the vector

//now calculate
        unsigned int result = 0;

        temp = R;
        while(temp--)
        {
            unsigned int total = 0;
            unsigned int i ;

            for(i = 0; total <= k && i <= N; i++)
            {
                total += groups[i];
            }

            total -= groups[i];

            i--;
            while(i--)
            {
                result += groups[i];
                groups.erase(groups.begin()+i);
            }
        }

        cout << "Case #" << i << ": " << result << endl;
        // now groups have the groups

        //I need at most R* vector times of it in my vector
    }
    return 0;
}
