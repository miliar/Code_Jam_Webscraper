#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int nums[3][1024];
bool pass[1024];
int N;

int ans;


void go(int loc)
{
    if(loc == N)
    {
        int t = 0;
        for(int i = 0; i < N; i++)
            t += nums[1][i] *  nums[2][i];
            
        ans = min(ans, t);
    }
    else
    {
        for(int i = 0; i < N; i++)
            if(!pass[i])   
            {
                pass[i]= true;
                nums[2][loc] = nums[0][i];
                go(loc + 1);
                pass[i] = false;               
            }
    } 
}

int main()
{
    int T;
    cin >> T;
    
    for(int z = 1; z <= T; z++)
    {
            memset(pass, 0, sizeof(pass));
        ans = INT_MAX;
        cin >> N;
        for(int j = 0; j < 2; j++)
        for(int i = 0; i < N; i++)
            cin >> nums[j][i];
            
        go(0);
            
        cout << "Case #" << z << ": " << ans << '\n';
    }
    
    return 0;   
}
