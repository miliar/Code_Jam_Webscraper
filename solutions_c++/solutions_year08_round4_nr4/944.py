// Problem D
// Problem's source: Google Code Jam - Round 2
// Program by Plamen Petrov (C) 2008
// http://digitalphysics.org/~ppetrov

#include <iostream>
#include <cstring>
#include <vector>
#include <map>
#include <deque>
#include <algorithm>
#include <iterator>
using namespace std;

char s[65536], n[65536];
int k, lens, p[32];
    
int rle_size()
{
    int i, j=0, a, g=1;
    
    for(i=0; i<lens; i++) 
    {
        if(j==0) a=i;
        //cout << a+p[j] << " ";
        n[i]=s[a+p[j]];
        
        if(++j>=k) j=0;
    }
    n[lens]=0;
    
    for(i=1; i<lens; i++) 
        if(n[i]!=n[i-1]) g++; 
    
    //cout << "n=" << n << " g=" << g << endl;
    return g;
}

int main()
{
    //freopen("D-small.in", "r", stdin);
    //freopen("D-small.out", "w", stdout);
    
    //freopen("D-large.in", "r", stdin);
    //freopen("D-large.out", "w", stdout);

    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int test, tests, i, j, g;
    
    long long res;

    cin >> tests;
    for(test=1; test<=tests; test++)
    {
        cin >> k >> s;
        for(i=0; i<k; i++) p[i]=i; //init permutation array p
        
        lens=strlen(s);
        res=lens;

        do 
        {
            //debug
            //cout << "perm ";
            //for(i=0; i<k; i++) cout << p[i] << " ";
            //cout << endl;
            
            g=rle_size();
            if(res>g) res=g;
            
        } while (next_permutation(p, p+k));

        
        cout << "Case #" << test << ": " << res << endl;

    }

    return 0;
}
