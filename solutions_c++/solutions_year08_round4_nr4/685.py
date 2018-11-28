#include <string>
#include <iostream>
using namespace std;

int K;
string str;

bool pass[32];
int buf[32];
int ans;

void go(int loc)
{
    if(loc < K)
    {
        for(int i = 0; i < K; i++)
            if(!pass[i])       
            {
                buf[loc] = i;
                pass[i] = true;
                go(loc + 1);
                pass[i] = false;
            }
    }
    else
    {
        int len = 0;
        char c = 0;
        for(int i = 0; i < str.size(); i++)
            if(str[i - (i % K) + buf[i % K]] != c)
                len++, c = str[i - (i % K) + buf[i % K]];
                
        
        if(ans > len)
            ans = len;
    }     
}

int main()
{
    int N;
    cin >> N;
    for(int z = 1; z <= N; z++)
    {
        cin >> K >> str;
        ans = INT_MAX;
        
        go(0);
        
        cout << "Case #" << z << ": " << ans << '\n';
            
            
    }
    
    
    return 0;   
}
