#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    ofstream fout ("jam3.txt");
    ifstream fin ("jam3.in");
    
    int binom[501][501];
    for(int i=0; i<=500; i++)
    for(int j=0; j<=i; j++)
    if(j==0)
    binom[i][j]=1;
    else
    binom[i][j] = (binom[i-1][j] + binom[i-1][j-1])%100003;
    
    int solve[501][501];
    int res[501];
    
    for(int i=0; i<501; i++)
    for(int j=0; j<501; j++)
    solve[i][j] = 0;
        
    for(int i=2; i<=500; i++)
    for(int j=1; j<i; j++)
    if(j==1)
    solve[i][j]=1;
    else
    {
    solve[i][j]=0;
    for(int s=1; s<j; s++)
    solve[i][j] = (solve[i][j] + solve[j][s]*binom[i-j-1][j-s-1])%100003;
    }
    
    res[0]=0;
    res[1]=0;
    
    for(int i=2; i<=500; i++)
    {
    res[i]=0;
    for(int j=1; j<i; j++)
    res[i] = (res[i] + solve[i][j])%100003;
    }
    
    int t;
    fin >> t;
    int n;
    
    for(int i=0; i<t; i++)
    {
    fin >> n;
    fout << "Case #" << i+1 << ": " << res[n] << endl;
    }
        
    return 0;
    
}
