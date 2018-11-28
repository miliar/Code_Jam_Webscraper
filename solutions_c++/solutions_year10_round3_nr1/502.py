#include <map>
#include <vector>
#include <cstdlib>
#include <cstdio>


using namespace std;







int main(int argc, char** argv){
  unsigned tests, test;
  unsigned t[1002][2], n;
  scanf("%d", &tests);

  for (test=0;test<tests;test++){
    scanf("%d",&n);
    unsigned i,j;
    unsigned inter;
    inter = 0;
    for (i=0;i<n;i++){
      scanf("%d %d", &(t[i][0]), &(t[i][1]));
    }
    for (i=0;i<n;i++){
      for (j=i+1;j<n;j++){
	if ((t[i][0] < t[j][0] && t[j][1] < t[i][1]) ||
	    (t[i][0] > t[j][0] && t[j][1] > t[i][1]) ){
	  inter++;
	}
      }
    }

    printf("Case #%i: %i\n", test+1, inter);
  }

  return 0;
}
