#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    long long a[1001], b[1001], cc,c, i, n, k,  t;
    fstream infile("A-large.in");
    ofstream outfile("A-large.out");
//    fstream infile("input.txt");
//    ofstream outfile("out.txt");
    infile >> t;
    for(cc=1; cc<=t; ++cc)
    {
      infile >> n;
      cout << n <<endl;      
      for (i=1; i<=n;++i){infile >> a[i] >> b[i]; cout <<a[i]<<' '<<b[i]<<endl;}
      c=0;
      for (i=1; i<n;++i) for (k=i+1;k<=n;++k) if ((a[i]-a[k])*(b[i]-b[k])<0)++c;
      outfile << "Case #" <<cc<<": ";
      outfile <<c<< endl;
    }
    infile.close();
    outfile.close();
cin.ignore();
}
