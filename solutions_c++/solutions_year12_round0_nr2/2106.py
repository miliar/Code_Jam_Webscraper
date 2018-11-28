#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

int main(){

    int testN;
    scanf("%d",&testN);
    for( int test=1; test<=testN; ++test) {
        // READ TEST CASE
        int n,s,p;
        scanf("%d %d %d",&n, &s, &p);
        int t_score[n];
        int scores[n][3];
        for( int i=0; i<n; ++i)
            scanf("%d",&t_score[i]);

        sort(t_score,t_score+n, less<int>());
        bool suprise[n];
        bool used[n];
        //PREPARE score_tab
        for(int i=0; i<n; ++i ) {
            suprise[i]=false;
            used[i]=false;
            int mid = t_score[i]/3;
            scores[i][0]=scores[i][1]=scores[i][2]=mid;
            t_score[i]-=mid*3;
                switch(t_score[i]) {
                case 0 :
                    if ( s>0 &&scores[i][0]>0 &&mid<10 && mid+1==p) {
                        scores[i][0]+=1;
                        scores[i][2]-=1;
                        s--;
                        suprise[i]=true;
                        used[i]=true;
                    }
                    break;
                case 1:
                    if (s>0 && mid+1==p) {
                        scores[i][0]+=1;
                        scores[i][1]+=1;
                        scores[i][2]-=1;
                        s--;
                        used[i]=true;
                    } else
                        scores[i][0]+=1;
                    used[i]=true;
                    break;
                case 2:
                    if (s>0 && mid<9 && mid+2==p) {
                        scores[i][0]+=2;
                        s--;
                        suprise[i]=true;
                        used[i]=true;
                    } else {
                        scores[i][0]+=1;
                        scores[i][1]+=1;
                        used[i]=true;
                    }
                    break;
                default :
                    break;
                }
        }

        for(int i=0; i<n; ++i ) {
            if(!used[i])
                switch(t_score[i]) {
                case 0 :
                    if ( s>0 &&scores[i][0]>0 &&scores[i][0]<10 ) {
                        scores[i][0]+=1;
                        scores[i][2]-=1;
                        s--;
                        suprise[i]=true;
                        used[i]=true;
                    }
                    break;
            case 1:
                    if (s>0 ) {
                        scores[i][0]+=1;
                        scores[i][1]+=1;
                        scores[i][2]-=1;
                        s--;
                        used[i]=true;
                    } else
                    scores[i][0]+=1;
                    used[i]=true;
                    break;
                case 2:
                    if (s>0 && scores[i][0]<9 ) {
                        scores[i][0]+=2;
                        s--;
                    suprise[i]=true;
                    used[i]=true;
                    } else {
                        scores[i][0]+=1;
                        scores[i][1]+=1;
                        used[i]=true;
                }
                    break;
                default :
                    break;
                }
        }

        int max=0;
        for( int i=0; i<n; ++i) {
//            printf("%d %d %d %s",scores[i][0],scores[i][1],scores[i][2],(suprise[i]?"(*)\n":"\n"));
            if (scores[i][0] >= p ) max++;
        }
        printf("Case #%d: %d\n",test,max);

    }
    return 0;
}

