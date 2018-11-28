#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int brute_force(vector<int> &candy)
{
    unsigned int mask = 0x01;
    vector<int> left, right;
    int i;
    int corsumP, incorsumP;
    int corsumS, incorsumS;
    int maxsum;

    maxsum = 0;
    while (mask < (0x01 << candy.size())-1)
    {
        for (i=0; i<candy.size(); i++)
        {
            if ((0x01 << i) & mask)
            {
                left.push_back(candy[i]);
            }
            else
            {
                right.push_back(candy[i]);
            }
        }
        sort(left.begin(), left.end()); 
        sort(right.begin(), right.end()); 

        corsumP = incorsumP = 0;
        corsumS = incorsumS = 0;
        for (i=0; i<left.size(); i++)
        {
            corsumP += left[i];
            incorsumP ^= left[i];
        }
        for (i=0; i<right.size(); i++)
        {
            corsumS += right[i];
            incorsumS ^= right[i];
        }
        if (incorsumP == incorsumS)
        {
            if (corsumP > maxsum)
                maxsum = corsumP;
            if (corsumS > maxsum)
                maxsum = corsumS;
        }
        
        left.clear();
        right.clear();
        mask += 1;
    }
    return maxsum > 0 ? maxsum : -1;
}

int candy_sum(vector<int> &candy)
{
    int corsumP, incorsumP;
    int corsumS, incorsumS;
    int i;

    corsumP = incorsumP = 0;
    corsumS = incorsumS = 0;

    if (candy.size() == 0)
        return -1;

    for (i=candy.size()-1; i>=0; i--)
    {
        if (incorsumP^candy[i] < incorsumS^candy[i])
        {
            incorsumP ^= candy[i];
            corsumP += candy[i];
        }
        else if (incorsumS^candy[i] < incorsumP^candy[i])
        {
            incorsumS ^= candy[i];
            corsumS += candy[i];
        }
        else
        {
            incorsumS ^= candy[i];
            corsumS += candy[i];
        }
    }

    if (incorsumP != incorsumS)
        return -1;
    if (corsumP > corsumS)
        return corsumP;
    else 
        return corsumS;
}

int main(void)
{
    int T, N;
    int i, j;
    int val, sum;
    vector<int> candy;

    // Get the number of test cases
    cin >> T;

    for (i=1; i<=T; i++)
    {
        cin >> N;
        for (j=0; j<N; j++)
        {
            cin >> val;
            candy.push_back(val);
        }
        sort(candy.begin(), candy.end()); 
        sum = candy_sum(candy);
        cout << "Case #" << i << ": "; 
        if (sum != -1)
            cout << sum << endl;
        else
            cout << "NO" << endl;
        candy.clear();
    }
}
