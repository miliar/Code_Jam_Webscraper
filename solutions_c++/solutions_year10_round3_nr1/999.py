#include <cstdio>
#include <vector>
using namespace std;
int main(){
   FILE * f=fopen("A.in","r");
   FILE * f2=fopen("A.out","w");
   int T,N,A1,B1;
   fscanf(f,"%ld",&T);
   for(int i=0;i<T;i++){
         fscanf(f,"%ld",&N);
         vector<int> a,b;
         int answ=0;
         for(int j=0;j<N;j++){
                               fscanf(f,"%ld %ld",&A1,&B1);
                               for(int k=0;k<a.size();k++){
                                                              if(a[k]<A1 && b[k] > B1) answ++;
                                                              if(a[k]>A1 && b[k] < B1) answ++;


                                                          }
                               a.push_back(A1);
                               b.push_back(B1);
                             }

       fprintf(f2,"Case #%ld: %ld\n",i+1,answ);



   }

return 0;
}
