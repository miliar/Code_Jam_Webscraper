
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<math.h>
#include<string.h>
#include<iostream>

using namespace std;

inline int max(int a,int b){
   return(a>b)?a:b;
}

inline int min(int a,int b){
   return(a<b)?a:b;
}

inline int abs(int a){
    return(a<0)?-a:a;
}
//qsort(array,arraysize,sizeof(int),compare);
int compare(const void*a,const void*b){
    return (*(int*)a-*(int*)b);
}
int comp(const void* p1, const void* p2) {
  int* arr1 = (int*)p1;
  int* arr2 = (int*)p2;
  int diff1 = arr1[0] - arr2[0];
  if (diff1) return diff1;
  return arr1[1] - arr2[1];
}

int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

	int t;
	scanf("%d",&t);

    int N;
    for(int z=1;z<=t;z++){
        scanf("%d",&N);

        char table[N][N+1];
        double answer[N];

        for(int i=0;i<N;i++){
            scanf("%s",&table[i]);
        }

        int win[N];
        int play[N];
        double wp[N];
        double owp[N];
        double oowp[N];

        for(int i=0;i<N;i++){
            win[i]=0;
            play[i]=0;
            for(int j=0;j<N;j++){
                if(table[i][j]=='.')continue;
                else{
                    if(table[i][j]=='1'){
                        win[i]++;
                        play[i]++;
                    }else{
                        play[i]++;
                    }
                }
            }
            wp[i]= ((double)win[i])/((double)play[i]);
        }

        double tmp[N];

        for(int i=0;i<N;i++){
            int point=0;
            for(int j=0;j<N;j++){
                if(table[j][i]=='1'){
                    tmp[point++]=((double)(win[j]-1))/((double)(play[j]-1));
                }
                else if(table[j][i]=='0'){
                    tmp[point++]=((double)(win[j]))/((double)(play[j]-1));
                }
            }
            double avg=0;
            for(int j=0;j<point;j++){
                avg+=tmp[j];
            }
            avg = avg / (double)point;
            owp[i] = avg;
        }

        double tt;
        int count;
        for(int i=0;i<N;i++){
            tt=0;
            count=0;
            for(int j=0;j<N;j++){
                if(table[i][j]!='.'){
                    tt+=owp[j];
                    count++;
                }
            }
            tt/=(double)count;
            oowp[i] = tt;
        }


        for(int i=0;i<N;i++){
            answer[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
        }

        printf("Case #%d:\n",z);
        for(int i=0;i<N;i++){
            printf("%.12lf\n",answer[i]);
        }

    }
	return 0;
}
