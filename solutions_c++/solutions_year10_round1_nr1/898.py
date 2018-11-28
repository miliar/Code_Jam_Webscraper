#include<cstdio>
#include<algorithm>
using namespace std;

char og[55][55];
char ga[55][55];

int testCase, n, k;/*k is winning condition*/
int rwin, bwin;

int main(){
  freopen("A-large.in", "r", stdin);
  freopen("out.out", "w", stdout);
    
    scanf("%d", &testCase);
    for(int i=1; i<=testCase; ++i){
        rwin = bwin = 0;
        scanf("%d%d", &n, &k);
        for(int j=0; j<n; ++j){
            scanf("%s", og[j]);
            for(int z=0; z<n; ++z){
                ga[j][z] = og[j][z];
            }
        }
        
        /* process in gavity */
        for(int j=0; j<n; j++){
            for(int z=n-1; z>=0; z--){
                if(ga[j][z]!='.'){
                    for(int d=1; d+z<n; ++d){
                        if(ga[j][z+d]!='.') break;
                        ga[j][z+d] = ga[j][z+d-1];
                        ga[j][z+d-1] = '.';
                    }
                }
            }
        }
        /*
        for(int j=0; j<n; ++j){
            for(int z=0; z<n; ++z){
                printf("%c ", ga[j][z]);
            }
            puts("");
        }
        */
        
        for(int j=0; j<n; ++j){
            for(int z=0; z<n; ++z){
                if(ga[j][z]!='.'){
                    int cnt = 1;
                    int chk1, chk2;
                    
                    chk1 = chk2 = 0;
                    for(int d=1; d<=k; ++d){
                        if(d+j<n && ga[d+j][z] == ga[j][z] && !chk1){
                            cnt++;
                        }else{
                            chk1 = 1;
                        }
                        if(j-d>=0 && ga[j-d][z] == ga[j][z] && !chk2){
                            cnt++;
                        }else{
                            chk2 = 1;
                        }
                    }
                    if(cnt >=k ){
                        if(ga[j][z] == 'R')
                            rwin ++;
                        else
                            bwin ++;
                    }
                    
                    cnt = 1;
                    chk1 = chk2 = 0;
                    for(int d=1; d<=k; ++d){
                        if(d+z<n && ga[j][z+d] == ga[j][z] && !chk1){
                            cnt++;
                        }else{
                            chk1 = 1;
                        }
                        if(z-d>0 && ga[j][z-d] == ga[j][z] && !chk2){
                            cnt++;
                        }else{
                            chk2 = 1;
                        }
                    }
                    if(cnt >=k ){
                        if(ga[j][z] == 'R')
                            rwin ++;
                        else
                            bwin ++;
                    }
                    
                    cnt = 1;
                    chk1 = chk2 = 0;
                    for(int d=1; d<=k; ++d){
                        if(d+z<n && d+j<n && ga[j+d][z+d] == ga[j][z] && !chk1){
                            cnt++;
                        }else{
                            chk1 = 1;
                        }
                        if(z-d>=0 && j-d>=0 && ga[j-d][z-d] == ga[j][z] && !chk2){
                            cnt++;
                        }else{
                            chk2 = 1;
                        }
                    }
                    if(cnt >=k ){
                        if(ga[j][z] == 'R')
                            rwin ++;
                        else
                            bwin ++;
                    }
                    
                    cnt = 1;
                    chk1 = chk2 = 0;
                    for(int d=1; d<=k; ++d){
                        if(d+z<n && j-d>=0 && ga[j-d][z+d] == ga[j][z] && !chk1){
                            cnt++;
                        }else{
                            chk1 = 1;
                        }
                        if(z-d>=0 && j+d<n && ga[j+d][z-d] == ga[j][z] && !chk2){
                            cnt++;
                        }else{
                            chk2 = 1;
                        }
                    }
                    if(cnt >=k ){
                        if(ga[j][z] == 'R')
                            rwin ++;
                        else
                            bwin ++;
                    }
                }
            }
        }
        printf("Case #%d: ", i);
        if(rwin==0 && bwin==0){
            printf("Neither\n");
        }else if(rwin >0 && bwin >0){
            printf("Both\n");
        }else if(rwin >0){
            printf("Red\n");
        }else if(bwin >0){
            printf("Blue\n");
        }
        
    }

    return 0;
}
