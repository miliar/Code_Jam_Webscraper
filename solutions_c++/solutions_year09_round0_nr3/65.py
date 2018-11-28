
#include <iostream>
#include <gmpxx.h>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

//"welcome to code jam"

mpz_class count(string& input)
{
  const string welcome("welcome to code jam");
  vector<mpz_class> res(welcome.size());

  for(string::iterator itr=input.begin(),end=input.end();itr!=end;++itr)
  {
    switch(*itr)
    {
    case ' ':res[7] += res[6];res[10] += res[9];res[15] += res[14];break;
    case 'a':res[17] += res[16];break;
    case 'c':res[3] += res[2];res[11] += res[10];break;
    case 'd':res[13] += res[12];break;
    case 'e':res[1] += res[0];res[6] += res[5];res[14] += res[13];break;
    case 'j':res[16] += res[15];break;
    case 'l':res[2] += res[1];break;
    case 'm':res[5] += res[4];res[18] += res[17];break;
    case 'o':res[4] += res[3];res[12] += res[11];res[9] += res[8];break;
    case 't':res[8] += res[7];break;
    case 'w':res[0] += 1;break;
    }
  }

  return res.back();
}

int main(int,char**)
{
  int N;
  cin >> N;

  {
    string input;
    getline(cin,input);
  }

  for(int n=0;n<N;++n)
  {
    string input;
    getline(cin,input);
    cout << "Case #" << (n+1) << ": " << setfill('0') << setw(4) << (count(input)%10000) << '\n';
  }

  return 0;
}
