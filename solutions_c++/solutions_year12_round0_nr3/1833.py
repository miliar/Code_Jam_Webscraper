#include <stdio.h>
#include <math.h>

using namespace std;

int reposit (int rep[], int k, int num){
  int i;
  for (i = 0; i < k; i++)
    if (rep[i] == num)
      return 1;
  return 0;
}

int main (){
  
  int T, A, AAux, ndig, i, POT, Q, R, nnum, B, x, y, pot, k;
  int rep [200];

  scanf ("%d ", &T);

  for (x = 0; x < T; x++){

    /*for (i = 0; i < 1300000; i++){
      rep[0][i] = 0;
      rep[1][i] = 0;
      }*/
    
    y = 0;

    scanf ("%d %d ", &A, &B);
    /*printf ("%d %d\n", A, B);*/
    while (A != B) {
      k = 0;
      AAux = A;
      ndig = 0;
      while (AAux != 0){
	AAux /= 10;
	ndig++;
      }
      i = 0;
      /*printf("%d: ", A);*/
      while (i < ndig - 1){
	pot = pow (10, i + 1);
	POT = pow (10, ndig - (i + 1));
	Q = A / pot;
	R = A % pot;
	nnum = R * POT + Q;
	
	if (nnum > A && nnum <= B && !reposit(rep, k, nnum)/*&& !(rep[0][A] == 1 && rep[1][nnum] == 1)*/){
	  rep[k++] = nnum;
	  /*rep[0][A] = 1;
	    rep[1][nnum] = 1;*/
	  /*printf ("%d ", nnum);*/
	  y++;
	}
	i++;
      }
      /*printf ("\n");*/
      A++;
    }
    printf ("Case #%d: %d\n", x + 1, y);
  }
  
  return 0;
}
