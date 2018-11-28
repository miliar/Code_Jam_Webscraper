#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;

char w[100][100],d[100][100];
int v[100][100];
int main(){
        int t, cnt= 1;
        int r,c,no=0;
        scanf("%d", &t);
        while(t--){
                no = 0;
                memset(v,0,sizeof(v));
                scanf("%d%d", &r,&c);
                for(int i=0; i<r;i++){
                        getchar();
                        for(int j=0; j<c;j++){
                                w[i][j] = getchar();
                                if(w[i][j]=='#') no++;
                        }
                }
                printf("Case #%d:\n", cnt++);
                if(no%4 !=0) {printf("Impossible\n");continue;}

                int f = 0;
                for(int i=0; i<r;i++){
                        for(int j=0;j<c;j++){
                                if(w[i][j]=='.') d[i][j] = '.';
                                if(w[i][j]=='#' && !v[i][j]){
                                        v[i][j] = 1;
                                        if(w[i+1][j] !='#' || w[i][j+1] !='#' || w[i+1][j+1]!='#') f= 1;
                                        else{
                                                v[i+1][j] = v[i][j+1] = v[i+1][j+1] = 1;
                                                d[i][j] = d[i+1][j+1] = '/';
                                                d[i][j+1] = d[i+1][j] = '\\';
                                        }
                                }
                        }
                }
                if(f)  {printf("Impossible\n");continue;}
                else{
                        for(int i=0; i<r;i++){
                                for(int j=0; j<c;j++){
                                        printf("%c", d[i][j]);
                                }
                                printf("\n");
                        }
                }
        }
        return 0;
}
