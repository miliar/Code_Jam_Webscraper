#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    long long i, k, s, n, p, t, s1, s2, y, m;
//    fstream infile("B-small-attempt0.in");
    fstream infile("B-large.in");
    ofstream outfile("B-large.out");
//    ofstream outfile("B-small.out");
    infile >> t;
    for(i=1; i<=t; ++i)
    {
      infile >> n >> s >> p;
      y=0;
      switch(p)
      {
               case 0:
                    s1=0; s2=0; break;
               case 1:
                    s1=1; s2=1; break;
               case 2:
                    s1=4; s2=2; break;
               case 3:
                    s1=7; s2=5; break;
               case 4:
                    s1=10; s2=8; break;
               case 5:
                    s1=13; s2=11; break;
               case 6:
                    s1=16; s2=14; break;
               case 7:
                    s1=19; s2=17; break;
               case 8:
                    s1=22; s2=20; break;
               case 9:
                    s1=25; s2=23; break;
               case 10:
                    s1=28; s2=26; break;
               }
      cout << i << " -> ";
      for (k=0;k<n;++k)
      {
          infile >> m; cout <<m<<' ';
          if (m>=s1)++y; else if ((m>=s2)&&(s>0)){++y;--s;}
      }
      cout << endl;
      
      outfile << "Case #" <<i<<": "<<y<<endl;
      cout << "Case #" <<i<<": "<<y <<endl;
    }
    infile.close();
    outfile.close();
cin.ignore();
}
