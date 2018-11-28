#include <iostream>
#include <vector>
#include <algorithm>
#define VI vector<int>
using namespace std;

VI getScores(int n)
{
    int nHigh = n % 3 ;
    
    VI res(3,n/3);
    for (int i=2; i>2-nHigh; --i)
        res[i]++;
        
    return res;
}

bool isPossible(int score, int mx)
{
    VI scores = getScores(score);
    
    if (score <= 1)
    {
        if (score == 1) return mx <= 1;
        if (score == 0) return mx == 0;
    }
    
    int numToConsider = score % 3 == 2 ? scores[2] : scores[0];
    
    if (numToConsider + 1 >= mx)
        return true;
    return false;
}

int main()
{
    int t;
    cin >> t;
    for (int z=1; z<=t; z++)
    {
        int n, surp, mx, res=0;
        cin >> n >> surp >> mx;
        VI scores;
        for (int i=0; i<n; i++)
        {
            int ti;
            cin >> ti;
            scores.push_back(ti);
        }
        
        sort(scores.rbegin(), scores.rend());
        
        //cout << "Scores in order: " << endl;
        //for (int i=0; i<scores.size(); i++)
        //    cout << scores[i] << " ";
        //cout << endl;
        
        
        for (int i=0; i<scores.size(); i++)
        {
            VI crScores = getScores(scores[i]);
            //cout << " Scores of " << scores[i] << ": " << crScores[0] << ", " << crScores[1] << ", " << crScores[2] << endl;
            int crMx = crScores[2];
            if (crMx >= mx) res++;
            else if (surp > 0 && isPossible(scores[i], mx)) 
            {
                res++;
                surp--;
            }
        }
        
        cout << "Case #" << z << ": " << res << endl;
    }
}
