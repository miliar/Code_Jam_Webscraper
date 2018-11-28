#include <stdio.h>
#include <vector>
#include <string>
#include <set>


using namespace std;


int main() 
{
  int cases;

  scanf("%d", &cases);
  
  for(int i=0;i< cases; i++) {
    int wires;
    scanf("%d", &wires);

    int wirestart[wires];
    int wireend[wires];

    for(int j=0;j<wires;j++) {
      scanf("%d%d", &wirestart[j], &wireend[j]);
      //printf("wire %d: %d to %d\n", j, wirestart[j], wireend[j]);
    }

    int intersect = 0;

    for(int j=0;j<wires;j++) {
      for(int k=j+1;k<wires;k++) {
	bool above = wirestart[j] > wirestart[k];
	bool endabove = wireend[j] > wireend[k];
	//printf("wires %d and %d, above = %d endabove = %d\n", j, k, above, endabove);
	if(above != endabove && j!=k) {
	  intersect++;
	}
      }
    }
    printf("Case #%d: %d\n", i+1, intersect);
  }

  return 0;
}
