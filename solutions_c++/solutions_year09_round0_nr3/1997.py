#include <iostream>
#include <stdio.h>
#include <string>
#include <iomanip>

using namespace std;

string line ;
string welcome = "welcome to code jam" ;
int rek(int k, int pos)
{
    
    if(k>=19) return 1 ;
    else if(pos >= line.size()) return 0 ;

    int count = rek(k,pos+1 ) ;

    if(line[pos] == welcome[k])
	count += rek(k+1, pos+1) ;

    return count ;
}

int main()
{
  int n ;
  

  scanf("%d", &n) ;
  getline(cin, line) ;
  for(int i=1;i<=n;i++)
  {
      getline(cin, line) ;
      cout << "Case #" << i << ": " << setfill('0') <<setw(4) << (rek(0, 0)%10000) << endl ;
  }

  return 0;
}