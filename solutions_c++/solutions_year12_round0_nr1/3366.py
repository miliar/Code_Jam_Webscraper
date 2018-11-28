#include<iostream>
using namespace std;
char C[26] =
{
  /*a*/ 'y',
  /*b*/ 'h',
  /*c*/ 'e',
  /*d*/ 's',
  /*e*/ 'o',
  /*f*/ 'c',
  /*g*/ 'v',
  /*h*/ 'x',
  /*i*/ 'd',
  /*j*/ 'u',
  /*k*/ 'i',
  /*l*/ 'g',
  /*m*/ 'l',
  /*n*/ 'b',
  /*o*/ 'k',
  /*p*/ 'r',
  /*q*/ 'z',
  /*r*/ 't',
  /*s*/ 'n',
  /*t*/ 'w',
  /*u*/ 'j',
  /*v*/ 'p',
  /*w*/ 'f',
  /*x*/ 'm',
  /*y*/ 'a',
  /*z*/ 'q'
};


int main()
{
  int t;
  cin >> t;

  char c;
  cin.get(c);

  for(int i=1;i<=t;++i)
  {
    cout << "Case #" << i << ": ";
    while(cin.get(c))
    {
      if(c=='\n')
        break;
      if(c==' ')
        cout << c;
      else
        cout << C[c-97];
    }
    cout << endl;
  }
}

