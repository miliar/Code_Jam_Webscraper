// GCJ '08 
// Question D
// Solution by sql_lall
#include <map>
#include <cmath>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int nCases;

int nums[15];

int solve(){
    int k; string inp; 
    cin >> k >> inp;
    int nBlock = inp.size() / k;
    for(int i = 0; i < k; i++) nums[i] = i;
    int ans = inp.size();
    do{
        char last = '.';
        int amt = 0;
        for(int i = 0; i < nBlock; i++){
            for(int j = 0; j < k; j++){
                char curr = inp[i * k + nums[j]];
                if(curr != last) amt++;
                last = curr;
            }
        }
        ans = min(amt, ans);
    } while(next_permutation(nums, nums + k));
    return ans;
}

int main(){
    cin >> nCases;
    for(int c = 1; c <= nCases; c++)
        cout << "Case #" << c << ": " << solve() << endl;
}
