#include <cstdio>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[]) {

  int T, N, S, p;
  int tp[100][4];

  //Read number of test cases
  scanf("%d", &T);
  for(int t=1; t<=T; t++) {

    //Read test case data
    scanf("%d %d %d", &N, &S, &p);
    for(int i=0; i<N; i++)
      scanf("%d", &tp[i][0]);
    
    //Compute max scores for every googler
    for(int i=0; i<N; i++) {
      int x = tp[i][0] / 3;
      int remain = tp[i][0] - 3*x;

      if( remain==0 )
	tp[i][1] = tp[i][2] = tp[i][3] = x;
      else if( remain==1 ) {
	tp[i][1] = x+1;
	tp[i][2] = tp[i][3] = x;
      }
      else { //remain=2
	tp[i][1] = tp[i][2] = x+1;
	tp[i][3] = x;
      }

      //printf("%d %d %d %d\n", 
      //	     tp[i][0], tp[i][1], tp[i][2], tp[i][3]);
    }

    //Use surprising triples to increase scores of cases
    //where best score is less than p
    for(int i=0, s=0; i<N && s<S; i++) {
      if( tp[i][1] == p-1 && tp[i][2] > 0 && tp[i][1] < 10) {
	tp[i][1]++;
	tp[i][2]--;
	s++;
	//printf("%d %d %d %d Surprising!\n", 
	//       tp[i][0], tp[i][1], tp[i][2], tp[i][3]);
      }
    }

    int res=0;
    for(int i=0; i<N; i++)
      if( tp[i][1] >= p )
	res++;

    printf("Case #%d: %d\n", t, res);
  }

  return 0;
}
