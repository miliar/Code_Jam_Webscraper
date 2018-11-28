#include<cstdio>

using namespace std;

int main(){
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    //input
    int N;
    char data[200][200];
    scanf("%d\n",&N);
    for(int i=0;i<N;i++)
      scanf("%s",data[i]);

    //calc
    double WP[200];
    int P[200];
    for(int i=0;i<N;i++){
      WP[i]=P[i]=0;
     for(int j=0;j<N;j++){
	if(data[i][j]!='.'){
	  P[i]++;
	  if(data[i][j]=='1')
	    WP[i]++;
	}
      }
    }
    double OWP[200];
    for(int i=0;i<N;i++){
      OWP[i]=0.;
      for(int j=0;j<N;j++)
	if(data[i][j]!='.'){
	  OWP[i]+=(WP[j]-(data[j][i]=='1'?1:0))/(P[j]-1);
	}
      OWP[i]/=P[i];
    }
    double OOWP[200];
    for(int i=0;i<N;i++){
      OOWP[i]=0.;
      for(int j=0;j<N;j++)
	if(data[i][j]!='.') OOWP[i]+=OWP[j];
      OOWP[i]/=P[i];
    }
   

    //answer
    printf("Case #%d:\n",t);
    for(int i=0;i<N;i++){
      //printf("%.6lf %.6lf %.6lf\n",WP[i]/P[i],OWP[i],OOWP[i]);
      printf("%.12lf\n",
	     WP[i]/(4.*P[i])+OWP[i]/2.+OOWP[i]/4.);
    }
  }
}
