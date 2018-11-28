#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int num_digits(int a)
{
    int c;
    for (c=1; a>=10; ++c) a/=10; 
    return c;          
}

int rotate(int a, int n, int num=0)
{
    int divisor = 1;
    int multiplier = 1;
    int i;
    
    if (num <=0) num = num_digits(a);
    
    for (i=0; i<n; ++i) divisor *= 10;
    for (i=0; i<num-n; ++i) multiplier *= 10;
    
    return a/divisor + (a%divisor)*multiplier;
}

int has_recycled(int a, int max)
{
    if (a > max) return 0;

    int i, rotated, n;
    n = num_digits(a);
    int c=0;
    
    char snum[20];
    sprintf(snum, "%d", max);
    char first=snum[0];
    bool isInvalid = true;
    for (i=1; i<strlen(snum); ++i)
        if (snum[i] <= first)
        {
            isInvalid=false;
            break;
        }
    //if (isInvalid) return 0;
    
    set<int> r;
    for (i=1; i<n; ++i)
    {
        
        rotated = rotate(a,i,n); 
        //cout << "a: " << a << ", rot: " << rotated << endl;
        if (rotated <= max && rotated > a && r.find(rotated) == r.end())
        {
            //cout << "a: " << a << ", rot: " << rotated << endl;
            r.insert(rotated);
            ++c;
        }
    }
    return c;
}

int main()
{
    int n,i,j;
    int a, b;
    int c;
    cin >> n;
    for (i=0; i<n; ++i)
    {
        c=0;
        cin >> a >> b;
        for (j=a; j<b; ++j)
            c += has_recycled(j,b);
        cout << "Case #" << i+1 << ": " << c << endl;
    }
    return 0;
}


