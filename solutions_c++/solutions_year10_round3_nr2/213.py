#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
int main()
{
    long long cc, i, n, k, b, t;
    double l, p, c, x;
    fstream infile("B-large.in");
    ofstream outfile("B-large.out");
//    fstream infile("B-small-attempt0.in");
//    ofstream outfile("B-small.out");
//    fstream infile("input.txt");
//    ofstream outfile("out.txt");
    infile >> t;
    for(cc=1; cc<=t; ++cc)
    {
      infile >> l >> p >> c;
      n=0;
      while ((p/l)>c){
            x=sqrt(p*l);
            if (x/l<p/x)l=x;else p=x;
            ++n;
      }
      cout << l << ' ' <<p <<' ' << c<<' '<<endl;      
      
      cout << "Case #" <<cc<<": ";
      cout <<n<< endl;
      
      outfile << "Case #" <<cc<<": ";
      outfile <<n<< endl;
    }
    infile.close();
    outfile.close();
cin.ignore();
}
