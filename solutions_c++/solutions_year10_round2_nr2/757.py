#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    long long cc, x[51], v[51], c, i, n, k, b, t, z, y;
    fstream infile("B-large.in");
    ofstream outfile("B-large.out");
//    fstream infile("B-small-attempt0.in");
//    ofstream outfile("B-small.out");
//    fstream infile("input.txt");
//    ofstream outfile("out.txt");
    infile >> c;
    for(cc=1; cc<=c; ++cc)
    {
      infile >> n >> k >> b >> t;
      cout << n << ' ' <<k <<' ' << b<<' '<<t<<endl;      
      for (i=1; i<=n;++i){infile >> x[i];cout <<x[i]<<' ';}
      cout<<endl;
      for (i=1; i<=n;++i){infile >> v[i];cout <<v[i]<<' ';}
      cout<<endl;
      y=0;
      z=0;
      for (i=n; i>0;--i) {
          if (b-x[i]-t*v[i]<=0) ++z;
          else y+=k-z;
          if (z==k)break;
          }    
      cout << "Case #" <<cc<<": ";
      if (z<k)cout <<"IMPOSSIBLE"<< endl;else cout <<y<< endl;
      outfile << "Case #" <<cc<<": ";
      if (z<k)outfile <<"IMPOSSIBLE"<< endl;else outfile <<y<< endl;
    }
    infile.close();
    outfile.close();
cin.ignore();
}
