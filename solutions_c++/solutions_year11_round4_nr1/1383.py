#include<stdio.h>
#include<vector>
#include<set>
#include<map>
#include<string.h>
#include<string>
#include<math.h>
#include<stdlib.h>
using namespace std;

int tests;
int len, walk, run, stam, n, sum;
vector<pair<double, double> > ints;
double stamd;

int main() {
  scanf("%d",&tests);
  for(int t=1;t<=tests;t++) {
    ints.clear();
    sum = 0;
    scanf("%d %d %d %d %d",&len,&walk,&run,&stam,&n);
    for(int i=0;i<n;i++) {
      int a, b, c;
      scanf("%d %d %d",&a,&b,&c);
      sum += (b-a);
      ints.push_back(make_pair(c,b-a));
    }
    ints.push_back(make_pair(0,len-sum));
    sort(ints.begin(), ints.end());
    double ret = 0.0;
    stamd = stam;
    for(int i=0;i<ints.size();i++) {
      //printf("%d %d\n",ints[i].first, ints[i].second);
      if(stamd > 0) {
        if(ints[i].second <= stamd * (ints[i].first + run)) {
          ret += ints[i].second / ((double)run + ints[i].first);
          stamd -= ints[i].second / ((double)run + ints[i].first);
          //printf("tu1");
        }
        else {
          ret += stamd;
          ints[i].second -= stamd * ((double)run + ints[i].first);
          stamd = 0;           
          i--;
          //printf("tu2");
        }
      }
      else {
        //printf("tu3");
        ret += ints[i].second / ((double)walk + ints[i].first);
      }
    }
      
    printf("Case #%d: %.9lf\n",t,ret);
  }
  return 0;  
}
            
      
    
    
      
    
    
