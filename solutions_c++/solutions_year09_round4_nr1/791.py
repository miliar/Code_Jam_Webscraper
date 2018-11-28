#include <iostream>
#include <cstdio>
#include <queue>
#include <stack>
#include <cctype>
#include <sstream>
#include <fstream>

using namespace std;

int main() {

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    cin >> T;

    for( int test=1; test<=T; test++ ) {
        int N;
        cin >> N;
        string grid[50];
        vector<int> nums, sorted;
        bool used[50];
        for( int i=0; i<N; i++ ) {
            cin >> grid[i];
            used[i]=false;
            bool found=false;
            for( int j=N-1; j>=0; j-- )
                if( grid[i][j]=='1' ) { nums.push_back(j); found=true; break; }
            if(!found) nums.push_back(0);
        }

        int ans=0;

        for( int i=0; i<N; i++ ) {
            int f=-1;
            for( int j=i; j<nums.size(); j++ ) { //try and find and swap
                if( nums[j]<=i ) {
                    f=j;
                    break;
                }
            }

            //keep swapping

            //for( int i=0; i<nums.size(); i++ ) cout << nums[i] << " ";
            //cout << endl;
            if(f==-1) break;
            for( int j=f; j>i; j-- ) {
                swap(nums[j],nums[j-1]);
                ans++;
            }
        }


        cout << "Case #" << test << ": " << ans << endl;
    }


    return 0;
}
