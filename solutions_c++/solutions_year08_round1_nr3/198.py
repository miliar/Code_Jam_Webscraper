#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <cassert>
using namespace std;
typedef long long ll;

// for n>=3, list of numbers generated using the following bash script:
   
//export BC_LINE_LENGTH=0; for((i=3;i<=30;i++)) do a=`echo "scale=2000; (sqrt(5)+3)^$i"| bc -l -q | sed 's/\(.*\)\..*/\1/g'`; echo "\"${a: -3}\","; done


char ans[][10]={
  "",
  "",
"027",
"143",
"751",
"935",
"607",
"903",
"991",
"335",
"047",
"943",
"471",
"055",
"447",
"463",
"991",
"095",
"607",
"263",
"151",
"855",
"527",
"743",
"351",
"135",
"407",
"903",
"791",
"135",
"647"
};

int main()
{
  int T;
  scanf("%d", &T);
  for(int t=1; t<=T; t++){
    int N;
    scanf("%d", &N);
    
    printf("Case #%d: %s\n", t, ans[N]);
  }
  return 0;
}
