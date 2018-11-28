#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <set>
#include <algorithm>

using namespace std;

int main(int argc, char **argv)
{
    int NNNNN;
    cin >> NNNNN;
    for (int cccccc=1;cccccc<=NNNNN;++cccccc)
    {
        cout << "Case #" << cccccc << ": ";
        
        // CODE
        int k;
        cin >> k;
        string S;
        cin >> S;
        vector<int> a(k);
        for (int i=0;i<k;++i)
        {
            a[i] = i;
        }
        int now = S.size();
        do
        {
            string temp = S;
            for (int i=0;i<temp.size();++i)
            {
                temp[i] = S[(i/k)*k + a[i%k]];
            }
            int ss = 1;
            for (int i=1;i<temp.size();++i)
            {
                if (temp[i] != temp[i-1]) ++ss;
            }
            if (ss < now) {now = ss;}
        }while(next_permutation(a.begin(), a.end()));
        cout << now << endl;
        // END OF CODE
    }
    return 0;
}