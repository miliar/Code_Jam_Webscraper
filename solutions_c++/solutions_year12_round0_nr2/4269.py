#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int t=0;
    cin >> t;

    for(int set=1; set<=t; set++)
    {
        int n, s, p, overP=0;
        cin >> n; cin >> s; cin >> p;
        for(int j=0; j<n; j++)
        {
            int score;
            cin >> score;
            score -= p;
            if(score>=p)
                if((score/2)-p>=-1)
                    overP++;
                else if((score/2)-p>=-2 && s)
                {
                    s--;
                    overP++;
                }

        }
        cout << "Case #" << set << ": " << overP << endl;
    }

    return 0;
}
