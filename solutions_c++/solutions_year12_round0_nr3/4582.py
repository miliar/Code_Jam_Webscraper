#include <stdio.h>
#include <fstream>
#include <iostream>

using namespace std;

long length(int k)
{
    int ans = 0;
    while (k != 0)
    {
        k = k/10;
        ans++;
    }
    return ans;
}

long powLong(long n)
{
    long res = 1;
    for(long i = 0; i<n; i++)
    {
        res = res * 10;
    }
    return res;
}

long rotate( long k, long n)
{
    long l = length(k);
    long ost = k % (long)powLong((long)n);
    k = k / powLong((long)n);
    k = k + (powLong(l-n) * ost);
    return k;
}

long CalcPairs(long k, long a, long b)
{
    long pairs = 0;
    for(int i = 1; i<length(k); i++)
    {
        long newK = rotate(k, i);
        if( ((a <= newK) && (newK <= b)) &&
             (length(k) == length(newK)) &&
             (k < newK))
        {
            pairs ++;
        }
    }
    return pairs;
}

long CalcNumbers(long a, long b)
{
    long ans = 0;
    int a1=0, a2=0, a3=0;
    for(long i = a; i<=b; i++)
    {
        long res = CalcPairs(i, a, b);
        if(res == 1)
            a1++;
        if(res == 2)
            a2++;
        if(res == 3)
            a3++;
        ans += res;
    }
    return ans;
}

int main()
{
    ifstream inp("input.txt");
    ofstream out("output.txt");
    if(!inp.is_open())
        cout<<"input file is invalid!"<<endl;
    if(!out.is_open())
        cout<<"output file is invalid!"<<endl;
    long long t;
    long long a,b;
    inp>>t;
    for(long i = 0; i<t; i++)
    {
        inp>>a>>b;
        out<<"Case #"<<i+1<<": "<<CalcNumbers(a, b)<<endl;
    }
    inp.close();
    out.close();
}