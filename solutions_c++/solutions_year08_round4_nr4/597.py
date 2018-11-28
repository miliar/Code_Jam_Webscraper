#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int k;
string S;

int main()
{
    int N;
    scanf("%d", &N);
    for (int test = 1; test <= N; ++test)
    {
        scanf("%d", &k);
        cin >> S;
        
        int sol = 100000;
        vector<int> p(k); for (int i = 0; i < k; ++i) p[i] = i;
        do 
        {
            string s = S;
            for (int i = 0; i < s.size(); i += k)
            {
                for (int j = 0; j < k; ++j)
                    s[i + j] = S[i + p[j]];
            }
            
            s.resize(unique(s.begin(), s.end()) - s.begin());
            if (sol > s.size()) sol = s.size();
        } while (next_permutation(p.begin(), p.end()));
        
        printf("Case #%d: %d\n", test, sol);
    }
    
	return 0;
}
