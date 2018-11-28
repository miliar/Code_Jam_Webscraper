#include <cstdio>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>


using namespace std;

int main(){
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    int n;
    cin>>n;
    int place[2]={1,1},time[2]={0,0};
    for (int i=1;i<=n;i++){
      char temp;
      int where;
      cin>>temp>>where;
      int who=0;
      if (temp == 'O')
	who=0;
      else
	who=1;
      time[who]+=abs(where-place[who]);
      time[who]=max(time[who],time[!who]);
      place[who]=where;
      time[who]++;
    }
    cout<<"Case #"<<ccount<<": "<<max(time[0],time[1])<<endl;
  }
}
