#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    ofstream fout ("jam2.txt");
    ifstream fin ("jam2.in");
    
    int c;
    long long int n, k, b, t;
    
    fin >> c;
    
    
    for(int i=0; i < c; i++)
    {
    fin >> n;
    fin >> k;
    fin >> b;
    fin >> t;
    
    int x[n];
    int v[n];
    
    for(int j=0; j < n; j++)
    fin >> x[j];
    
    for(int j=0; j < n; j++)
    fin >> v[j];
    
    int aux=0;
    
    for(int j=0; j<n; j++)
    if( v[j]*t >= b-x[j])
    aux++;
    
    if(aux < k)
    fout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
    else
    {
        
    aux=0;
    int res=0;
    
    for(int j=n-1; j>=0; j--)
    {
    if(aux == k)
    break;        
    
    if(v[j]*t >= b-x[j])
    {
    res = res + (n-1)-j-aux;
    aux++;   
    }
    }
    
    fout << "Case #" << i+1 << ": " << res << endl;
    
    
    }     
    }
        
    return 0;
    
}
