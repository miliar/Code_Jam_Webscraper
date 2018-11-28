#include <iostream>

using namespace std;


#define SMALL_NON_ZERO 0.00000001 /* or something else small */
double ABS(double a)
{
   return ((a)<0?-(a):a);
}
bool DBL_EQ(double X,double Y)
{
   return ( ABS(X - Y) < SMALL_NON_ZERO ); /* X == Y */
}

int main() {
  int cases;

  cin >> cases;

  for(int c = 1; c <= cases; c++) {
    int n, pd, pg;
    
    cin >> n >> pd >> pg;
    
    if( ((pg == 100) && (pd != 100)) || ((pg==0) && (pd > 0))) {
      cout << "Case #" << c << ": Broken" << endl;
      continue;
    } else {
      bool achou = false;
      for(int i=1; i<=n;i++) {
	double x = (double) ((i * pd)/100),
	       y = (double)i * (((double)pd)/100.0);
	if(DBL_EQ(x,y)) {
	  //cout << x << " - " << y << "--->" << i << endl;
	  cout << "Case #" << c << ": Possible" << endl;
	  achou = true;
	  break;
	}
      }
      if(!achou)
	cout << "Case #" << c << ": Broken" << endl;
    }
  }
  return 0;
}