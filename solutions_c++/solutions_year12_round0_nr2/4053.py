#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>

using  namespace std;

const string S = "yhesocvxduiglbkrztnwjpfmaq";

//#define small
#define large
int main()
{
#ifdef small
    freopen("B-small.in", "rt", stdin);
    freopen("B-small.out", "wt", stdout);
#endif

#ifdef large
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);
#endif

    int T, N, S, P, Case = 1;
    int num, ans;
    cin >> T;
    while(T --)
    {
        vector <int> nums;
        ans = 0;
        cin >> N >> S >> P;
        while(N --)
        {
            cin >> num;
            nums.push_back(num);
        }
        P = 3 * P;
        if(P == 0)
            ans = nums.size();
        else
        {
            for(int i = 0; i < nums.size(); i ++)
            {
                if(nums[i] == 0)
                    continue;
                if(nums[i] >= P)
                    ans ++;
                if(nums[i] < P)
                    switch(P - nums[i])
                    {
                        case 1: ans ++;break;
                        case 2: ans ++;break;
                        case 3:  
                            ans += S > 0 ? 1 : 0;
                            S --;
                            break;
                        case 4: 
                            ans += S > 0 ? 1 : 0;
                            S --;
                            break;
                    }
            }
        }
            cout << "Case #" << Case ++ << ": " << ans << endl;
    }
    return 0;
}
