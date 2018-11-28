#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <math.h>
#include <sstream>
#include <cstring>

using namespace std;

int main()
{


 freopen("B-large.in","r",stdin);
 freopen("outlarge.out","w",stdout);

int T , N ,S , P;
cin >> T;
int start = 1;
string cas = "Case #";

while(start <= T){
int count = 0;

 cin >> N >> S >> P;

int ti,fl,eq ,ce;

for(int i = 0;i < N;++i){
 cin >> ti;
 fl = floor(ti/3.0);
 eq = (ti/3.0);
 ce = ceil(ti/3.0);

 if(fl + eq + ce < ti){

  if(S > 0 && ce+1 == P){
        ce++;
        S--;
  }
  else
   eq++;
 }


/*if(fl+eq+ce != ti)
 cout << "Big Problemmmmmm\n";
if(ce - fl > 2)
 cout << "Big second Problemmmmmm\n";
*/

 if(S > 0 && ce+1 == P && ce  == fl){
  if(fl > 0 && ce < 10){
  fl--;
  ce++;
  S--;
  }
 }


//cout << fl << "  " << eq <<"  " << ce << endl;
 if(fl  >= P || eq  >= P || ce  >= P )
  count++;
}


cout << cas << start << ": " << count << endl;
start++;
}
    return 0;
}
