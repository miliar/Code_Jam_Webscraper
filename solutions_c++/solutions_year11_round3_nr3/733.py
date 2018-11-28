#include <iomanip>
#include <stdio.h>
#include <map>
#include <set>

using namespace std;
int main(){
  FILE *in = fopen("C-small-0.in","r");
  FILE *out = fopen("small.out","w");
  int T;
  fscanf(in,"%d", &T);
  for (int t = 0; t < T; t++){
    int N,L,H; char tmpc; int notes[110];
    fscanf(in,"%d %d %d", &N,&L, &H);
    for (int i = 0; i < N; i++){
      fscanf(in,"%d",&notes[i]);
    }
    int note=0;
    for (int i = L; i < H+1; i++){   
      bool found=true;
      for(int j = 0; j < N; j++){
        if ((notes[j]%i != 0) && (i%notes[j]!=0)) found=false;
      }   
      if (found) {note = i;break;}
    } 
    
    if (note !=0)
    printf("Case #%d: %d\n",t+1, note);
    else  printf("Case #%d: NO\n",t+1);

/*    for (int i = 0; i < N+1; i++){
        for (int j = 0; j< N+1; j++){
        printf("%d ",din[i][j]);
        }
        printf("\n");
    }
*/
  }
    
}
