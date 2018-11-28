#include <iostream>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

bool compare (int i,int j)
{
    return (i < j);
}

int main ()
{
    ios_base::sync_with_stdio(false);

    int t;
    int n,p,k;
    int *score;
    int val[31] = {0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10};
    int sur[31] = {-1,-1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,-1,-1};
    
    cin >> t;
    
    for (int i = 0 ; i < t ; i++)
    {
        int sum = 0;
        cin >> n >> p >> k;
        score = new int[n];
        for (int j = 0 ; j < n ; j++)
            cin >> score[j];

        stable_sort (score,score+n,compare);
        for (int j = 0 ; j < n ; j++)
        {
            if (val[score[j]] >= k)
            {
                sum++;
                continue;
            }
            if (p == 0)
                continue;
            if (sur[score[j]] >= k)
            {
                p--;
                sum++;
            }
        }

        cout << "Case #" << i+1 << " " << sum << endl;

        delete []score;
    }

    exit (EXIT_SUCCESS);
}
