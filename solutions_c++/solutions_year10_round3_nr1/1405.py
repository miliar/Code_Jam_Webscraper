#include<cstdio>
using namespace std;

int T;
int N;
int A[1000],B[1000];

int main(){
  scanf(" %d",&T);
  for(int pcnt=0;pcnt<T;++pcnt){
    int ans=0;
    scanf(" %d",&N);
    for(int i=0;i<N;++i){
      scanf(" %d %d",A+i,B+i);
      for(int j=0;j<i;++j){
	if((A[i]-A[j])*(B[i]-B[j])<0)++ans;
      }
    }
    printf("Case #%d: %d\n",pcnt+1,ans);
  }
  return 0;
}
