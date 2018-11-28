#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main(){
	 int T,N;
	 int *notes;
	 int L,H;
	 bool fail;
	 scanf("%d", &T);
	 for(int i=0;i<T;i++){
       scanf("%d %d %d", &N, &L, &H);
       notes=new int[N];
       for(int j=0;j<N;j++)
          scanf("%d", notes+j);
       if(L==1){
	        printf("Case #%d: 1\n", i+1);
	        continue;
       }
       fail=0;
       for(int j=L;j<=H;j++){
          //printf("\n[%d<%d:%d]", j,H,j<=H);
          fail=0;
		    for(int k=0;k<N;k++){
		       //printf("(%d)", notes[k]);
	 		    if(j%notes[k]!=0&&notes[k]%j!=0){
					 fail=1;
					 break;
				 }
	       }
	       if(!fail){
			    printf("Case #%d: %d\n", i+1, j);
			    break;
	       }
		 }
		 if(fail)printf("Case #%d: NO\n", i+1);
		 
    }
}
