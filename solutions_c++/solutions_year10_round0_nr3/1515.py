#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    long long i, t, r, k, n, sum[1000], c[1000], g[1000], b,z,h, bufer, loopsum, looplen;
    fstream infile("C-large.in");
    ofstream outfile("C-large.out");
    infile >> t;
    for(i=1; i<=t; ++i)
    {
      infile >> r >> k >> n;
      cout << r << ' ' <<k <<' ' << n<<endl;      
      
      z=0;
      for(b=0; b<n; ++b) 
      {
        infile >> g[b];z+=g[b];
        cout << g[b] <<' ';      
      }
      cout << endl;
      if (z<=k)
      {
       outfile << "Case #" <<i<<": " <<r*z<<endl;
       cout << "Case #" <<i<<": " <<r*z<<endl;
       continue;
      }

      for(h=0; h<n; ++h){c[h]=0;sum[h]=0;}
      b=0;z=0;
      
      for(h=0; (h<r)&&(c[b%n]==0); ++h)
      {
        bufer=0;
        c[b%n]=h+1;
        sum[b%n]=z;
        while ((bufer+g[b%n])<=k)
        {
          bufer+=g[b%n];
          ++b;
        }
        z+=bufer;
      }
      if (h<r)
      {
        loopsum=z-sum[b%n];
        looplen=h-c[b%n]+1;
        r=r-h+looplen;
        z=z+loopsum*(r/looplen-1);
        r%=looplen;
        for(h=0; (h<r); ++h)
        {
          bufer=0;
          while ((bufer+g[b%n])<=k)
          {
            bufer+=g[b%n];
            ++b;
          }
          z+=bufer;
        }
      }
      outfile << "Case #" <<i<<": " <<z<<endl;
      cout << "Case #" <<i<<": " <<z<<endl;
    }
    infile.close();
    outfile.close();
cin.ignore();
}
