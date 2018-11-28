#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include<algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<float> vf;

#define For(i,a,b) for (int i(a),_b(b);i<b;i++)
#define Rep(i,a) for (int i(0),_a(a);i<a;i++)
#define Repd(i,a) for (int i(a),_a(a);i>0;i--)

int main(void){
 freopen("A-large.in","rt",stdin);
  freopen("output.txt","wt",stdout);
  int cases;
  scanf("%d\n",&cases);

  Rep(i,cases){
    int r,c;
    scanf("%d %d\n",&r,&c);
    char ti[r][c];

    Rep(j,r){
      scanf("%s\n",&ti[j]);
      // printf("%s\n",&ti[j]);
    }
    int result=1;
    for(int j=0;j<r && result!=0;j++){
      Rep(k,c){
	if(ti[j][k]=='#' && k!=c && j !=r){
	  if(k!=c || j!=r){
	    if(ti[j][k+1]=='#' && ti[j+1][k]=='#' && ti[j+1][k+1]=='#'){
	      ti[j][k]=ti[j+1][k+1]='/';
	      ti[j][k+1]=ti[j+1][k]='\\';
	    }
	  else{
	    result=0;
	  }
	  }
	  else{
	    result=0;
	  }
	}
      }
    }
    printf("Case #%d:\n",i+1);
    if(result==0){
      printf("Impossible\n");
    }
    else{
      Rep(j,r){
	Rep(k,c)
	printf("%c",ti[j][k]);
	printf("\n");
      }      
    }
  }
}
