/* {{{ */
#include<cstdio>
#include<climits>
#include<cmath>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
#include<list>
#include<sstream>
#include<set>
#include<queue>
#include<vector>
#include<string>
#include<fstream>
#include<istream>
#include<iostream>
#include<bitset>
using namespace std;
/* }}}  */

typedef long long ll;
typedef unsigned long long ull;
const int MAX=50;
char arr[MAX][MAX],rot[MAX][MAX],f[MAX][MAX];

int K,N;

bool checkrow(int row,char ch){
        int j,k;
        for(j=0;j<N;j++){
                if(rot[row][j]==ch){
                        int cnt=1;
                        for(k=j+1;k<N;k++) if(rot[row][k]==ch) cnt++ ; else break;
                        if(cnt>=K) return true;
                }
        }
        return false;
}

bool checkcol(int col,char ch){
        int j,k;
        for(j=0;j<N;j++){
                if(rot[j][col]==ch){
                        int cnt=1;
                        for(k=j+1;k<N;k++) if(rot[k][col]==ch) cnt++ ; else break;
                        if(cnt>=K) return true;
                } 
        }
        return false;
}



bool checkdiag(int diag,char ch){
        int row=diag,col=0;
        if(diag >= N) row=N-1,col=diag-N+1;
        int sx=-1,sy=+1;
        while(row>=0 and col<N){
                int cnt=0;
                if(rot[row][col]==ch){
                        cnt=1;
                        int tx=row+sx,ty=col+sy;
                        while(tx>=0 and ty <N) {
                                if(rot[tx][ty]==ch) cnt++;
                                else break;
                                tx+=sx; ty+=sy;
                        }
                            if(cnt>=K) return true;
                 }
                row+=sx;col+=sy;
        }
        return false;
}



bool checkdiag1(int diag,char ch){
        int row=0,col=0;
        if(diag < N) col=N-1-diag;
        else { row=diag-N-1, col=0; }
        int sx=+1,sy=+1;
        while(row<N and col<N){
                int cnt=0;
                if(rot[row][col]==ch){
                        cnt=1;
                        int tx=row+sx,ty=col+sy;
                        while(tx<N and ty <N) {
                                if(rot[tx][ty]==ch) cnt++;
                                else break;
                                
                                tx+=sx; ty+=sy;
                        }
                            if(cnt>=K) return true;

                 }
                row+=sx;col+=sy;
        }
        return false;
}


int main(int argc,char **argv){
    int tc,NC;
        scanf(" %d",&NC);
        for(tc=1;tc<=NC;tc++){
                memset(arr,0,sizeof(arr));
                memset(rot,0,sizeof(rot));
                memset(f,0,sizeof(f));
            scanf(" %d %d",&N,&K);

            int i,j;
            for(i=0;i<N;i++) scanf(" %s",arr[i]);

            for(i=0;i<N;i++) for(j=0;j<N;j++) rot[j][N-i-1]=arr[i][j];

 //           for(i=0;i<N;i++) printf("%s\n",rot[i]);


            int col=0;
            for(col=0;col<N;col++)
            {
                int last=N-1;
                while(1){
                for(i=last;i>=0;i--) if(rot[i][col]=='.') break;
                for(j=i-1;j>=0;j--) if(rot[j][col]!='.') break;
                if(j<0) break;
                rot[i][col]=rot[j][col];
                rot[j][col]='.';
                }
            }

            
//            for(i=0;i<N;i++) printf("%s\n",rot[i]);

            bool isred=false,isblue=false;
            for(i=0;i<N;i++){
                    if(checkrow(i,'R') or checkcol(i,'R'))  isred=true;
                    if(checkrow(i,'B') or checkcol(i,'B')) isblue=true;
            }
            for(i=0;i<2*N-1;i++){
                    if(checkdiag1(i,'R') or checkdiag(i,'R'))  isred=true;
                    if(checkdiag1(i,'B') or checkdiag(i,'B')) isblue=true;
            }
            printf("Case #%d: %s\n",tc,(isred&&isblue)?"Both":(isred?"Red":(isblue?"Blue":"Neither")));
                
        }
    return 0;
}
