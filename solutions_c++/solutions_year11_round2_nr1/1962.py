#include <cstdio>
#include <vector>
using namespace std;

typedef pair<int,int> ii;


int T,N;
double sum;
int played,win;
char stats[128][128];
ii wp[128];
double owp[128],oowp[128],res[128];

int main(){

  scanf("%d",&T);
  for(int t=0;t<T;t++){
    scanf("%d",&N);
    for(int i=0;i<N;i++)
      scanf("%s",stats[i]);

    // wp
    for(int i=0;i<N;i++){
      played=win=0;
      for(int k=0;k<N;k++){
        if(stats[i][k]=='.') continue;
        if(stats[i][k]=='1') win++,played++;
        if(stats[i][k]=='0') played++;
      }
      wp[i] = make_pair(win,played);
    }

    // average owp without i
    for(int i=0;i<N;i++){
      sum=0.0;
      played=0;
      for(int k=0;k<N;k++){
        if(stats[i][k]=='.') continue;
        if(stats[i][k]=='1'){
          sum+=(double)wp[k].first/(double)(wp[k].second-1);
          played++;
        }
        if(stats[i][k]=='0'){
          if(wp[k].first>0) sum+=((double)wp[k].first-1)/(double)(wp[k].second-1);
          played++;
        }
      }
      owp[i]=sum/(double)played;
    }

    // oowp
    for(int i=0;i<N;i++){
      sum=0.0;
      played=0;
      for(int k=0;k<N;k++){
        if(stats[i][k]=='.') continue;
        sum+=owp[k];
        played++;
      }
      oowp[i]=sum/played;
      res[i]=0.25*((double)wp[i].first/(double)wp[i].second) + 0.5*owp[i] + 0.25*oowp[i];
    }

    printf("Case #%d:\n",t+1);
    for(int i=0;i<N;i++)
      printf("%.12lf\n",res[i]);
      //printf("wp: %lf owp: %lf oowp: %lf %.6lf\n",(double)wp[i].first/(double)wp[i].second,owp[i],oowp[i],res[i]);
  }

  return 0;
}
