#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int permutation[16];

int k;

string s;

char luls[10000];

int N;

void reset()
{
    for(int i = 0; i < k; ++i)
        permutation[i] = i;
}

void next()
{
    next_permutation(permutation, permutation+k);
    
    /*
    for(int i = 0; i < k; ++i)
    {
        cout << permutation[i] << " ";
    }
    
    cout << endl;
    */
}

void rearrange()
{
    for(int i = 0; i < s.length(); ++i)
    {
        luls[i] = s[k*(i/k)+permutation[i%k]];
        
        //cout << luls[i];
    }
    
    //cout << endl;
}

int rle()
{
    int rol = 0;
    char last = '-';
    
    for(int i = 0; i < s.length(); ++i)
    {
        //cout << luls[i];
        if(luls[i] != last)
        {
            ++rol;
            last = luls[i];
        }
    }
    
   // cout << " " << rol << " " << k << endl;
    
    return rol;
}

bool check()
{
    for(int i = 0; i < k; ++i)
        if(permutation[i] != i)
            return false;
    
    return true;
}

int main()
{
    cin >> N;
    
    for(int i = 1; i <= N; ++i)
    {
        cin >> k;
        
        cin >> s;
         
        int ans = 100000;
        
        reset();
        
        do
        {
            rearrange();
            ans = min(ans, rle());
            next();
        }
        while(!check());
        
        cout << "Case #" << i << ": " << ans << endl;
    }
}
