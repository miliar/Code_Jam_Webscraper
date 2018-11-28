#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <fstream>
using namespace std;

int power(int b, int exp)
{
    int ans = 1;
    for(int j = 0; j < exp; j++)
    {
        ans *= b;
    }
    return ans;
}

void disp(vector<long int> v)
{
    for(int x = 0; x < v.size(); x++)
    {
        cout << v[x] << " ";
    }
}

int len(int N)
{
    int ans = 0;
    while(N > 0)
    {
        N /= 10;
        ans++;
    }
    return ans;
}

vector<long int> recycled(long int N)
{
    vector<long int> v(len(N)-1);
    for(int x = 0; x < v.size();x++)
    {
        v[x] = (N%power(10,x+1))*(power(10,len(N)-x-1)) + N/(power(10,x+1));
    }
    return v;
}

bool is_recycled(long int n, long int m)
{
    if(n == m)
    return false;

    if(len(n) != len(m))
    return false;

    vector<long int> x;
    x = recycled(n);
    for(int j = 0; j < x.size(); j++)
    {
        if(x[j] == m)
        return true;
    }
    return false;
}

int recycled_between(long int A, long int B)
{
    int res = 0;
    if(is_recycled(A,B) == true)
    res+=2;
        for(int n = A; n <= B; n++)
        {
            for(int m = n; m <= B; m++)
            {
                if(is_recycled(n,m) == true and m <= B and m > n)
                res++;
            }
        }
    return res;
}
int main()
{
   ifstream fin("C-small-attempt11.in");
   ofstream fout("c_small.out");
   int N;
   fin >> N;
   for(int x = 0; x < N; x++)
   {
       long int A, B;
       fin >> A >> B;
       fout << "Case #" << x+1 << ": " << recycled_between(A,B) << endl;
   }
    return 0;
}
