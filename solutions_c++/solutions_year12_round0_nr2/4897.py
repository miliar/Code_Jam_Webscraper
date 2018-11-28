#include <iostream>

using namespace std;

int main()
{
  int cases,n,s,p;
  char a;
  cin >> cases;
  for ( int i = 0; i < cases; i++ ){
    cout << "Case #" << i + 1 << ": ";
    cin >> n;
    cin >> s;
    cin >> p;
    int temp;
    int total = 0;
    for ( int j = 0; j < n; j++)
      {
	cin >> temp;
	if ( temp >= (3*p - 2) )
	  {
	  total++;
	  }
	else if ( temp >= (3*p - 4) && s > 0 && !(temp == 0 && p != 0)){
	  s--;
	  total++;
	}
      }
    cout << total << endl;
  }
}
	 
      
