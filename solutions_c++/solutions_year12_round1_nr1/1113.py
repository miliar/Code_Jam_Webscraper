#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list> 
#include <numeric>
#include <regex.h>  
using namespace std; 
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef vector<vs> vvs;
#define pb push_back 
#define sz(v) ((int)(v).size()) 
 
int main()
{
  int i=0,j=0,k=0; char buf[1000]="";

  int keeses; scanf("%d",&keeses);
  int a,b;
  for(int kees=1;kees<=keeses;kees++) {
    scanf("%d %d",&a,&b);
    vector<long double> d(1,0.0); double f;
    vector<long double> logsom(1,0.0);
    for(i=0;i<a;i++) { scanf("%lf",&f); d.pb(f); logsom.pb(logsom.back()+log(f)); /*printf("logsom = %lf\n",logsom.back());*/ }
    long double bestexp = b+2;

    for (int hou=0;hou<=a;hou++) {
        long double nulog = logsom[hou];
        long double nugoedp = exp(nulog);
        long double nuexp = (a-hou+ a-hou + b-a +1) + (1.0-nugoedp) * (b+1);
        bestexp=min(nuexp,bestexp);
//printf("-- hou = %d, nugoedp = %lf, nuexp = %lf\n",hou, nugoedp, nuexp);
    }

    double best = bestexp;
    printf("Case #%d: %.8lf\n",kees,best);
  }

  return 0;
}
