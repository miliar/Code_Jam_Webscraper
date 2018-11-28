#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t,n,s,p,score,best;

    cin >> t;

    for (int i=1 ; i<=t ; i++){
        vector<int> scores;
        cin >> n >> s >> p;
        for (int j=0 ; j<n ; j++){
            cin >> score;
            scores.push_back(score);
        }

        int conform = 0;
        int possible = 0;

        for (int j=0; j<n ; j++){
            if (scores[j] >= (3*p-2)){
                conform++;
            } else if (scores[j] >= (3*p-4) && scores[j] > 0) {
                possible++;
            }
        }

        if (p == 0){
            best = n;
	} else {
            best = conform + min(possible,s);
        }

        cout << "Case #" << i << ": " << best << endl;
    }
    return 0;
}