#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;


#define SMALL_NON_ZERO 0.00000001 /* or something else small */
double ABS(double a)
{
   return ((a)<0?-(a):a);
}

bool results[102][102];
bool played[102][102];
int tplayed[102];
int wins[102];
double owp[102];

int main() {
  int cases;

  cin >> cases;

  for(int c = 1; c <= cases; c++) {
    int n;
    cin >> n;
    
    string temp;
    for(int i = 0; i < n; i++) {
      tplayed[i] = 0;
      wins[i] = 0;
      owp[i] = 0.0;
      cin >> temp;
      for(int j = 0; j < n; j++) {
	if (temp[j] == '.'){
	  played[i][j] = false;
	}else{
	  played[i][j] = true;
	  tplayed[i]++;
	  
	  if (temp[j] == '1'){
	    results[i][j] = true;
	    wins[i]++;
	  }else
	    results[i][j] = false;
	}
      }
    }
    cout << "Case #" << c << ":"<< endl;
    
    for(int i = 0; i < n; i++) {
      double cowp = 0.0;
      for(int j = 0; j < n; j++) {
	if( i != j && played[i][j]) {
	  if(!results[i][j])
	    cowp += (double)(wins[j] - 1) / (double)(tplayed[j]-1) ;
	  else 
	    cowp += (double)(wins[j]) / (double)(tplayed[j]-1);
	  
	  //cout << i << "," << j << " === "<< cowp << endl;
	}
	
      }
      
      owp[i] = cowp / (double)tplayed[i];
    }
    
    for(int i = 0; i < n; i++) {
      double rpi;
      rpi = ((double)wins[i]/tplayed[i]) * 0.25;

      rpi += owp[i] * 0.5;

      double oowp = 0.0;
      for(int j = 0; j < n; j++) {
	if( i != j && played[i][j]) {
	  oowp += owp[j];
	}
      }
      rpi += 0.25 * ( oowp / (tplayed[i]));
      
      cout << setprecision(12) << rpi << endl;
    }
    
    
    
  }
  
  return 0;
}