#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <sstream>
using namespace std;

int main()
{
  int ncase=1;
 string d[31];
 // generated with windows calculator
 d[1]="005";
 d[2]="027";
 d[3]="143";
 d[4]="751";
 d[5]="935";
 d[6]="607";
 d[7]="903";
 d[8]="991";
 d[9]="335";
 d[10]="047";
 d[11]="943";
 d[12]="471";
 d[13]="055";
 d[14]="447";
 d[15]="463";
 d[16]="991";
 d[17]="095";
 d[18]="607";
 d[19]="263";
 d[20]="151";
 d[21]="855";
 d[22]="527";
 d[23]="743";
 d[24]="351";
 d[25]="135";
 d[26]="407";
 d[27]="903";
 d[28]="791";
 d[29]="135";
 d[30]="647";
 
 
  int t;
  cin >> t;
  while(t--) 
  {
    int n;
    cin >> n;
    cout << "Case #" << ncase++ << ": " <<d[n]<< endl;
  }
  return 0;
}

  
