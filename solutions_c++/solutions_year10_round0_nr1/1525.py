#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    long long i, t, n, k, b,z;
    fstream infile("A-large.in");
    ofstream outfile("A-large.out");
    infile >> t;
    for(i=1; i<=t; ++i)
    {
      infile >> n >>k;
      b=1;
      b=b<<n;
      cout << n << ' ' <<k <<' ' << b<<endl;      
      outfile << "Case #" <<i<<": ";
      if ((k%b)==(b-1))outfile <<"ON"<< endl;else outfile <<"OFF"<< endl;
    }
    infile.close();
    outfile.close();
cin.ignore();
}
