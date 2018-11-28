#include <iostream>
#include <algorithm>
using namespace std;

int r,c;
string s[100];

int main()
{
    int tc; scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        scanf("%d%d",&r,&c);
        for(int i=0;i<r;i++) cin>>s[i];

        int changes=1;
        while(changes){
        changes=0;
        int fx=-1,fy=-1;
        for(int i=0;i<r-1;i++){
            for(int j=0;j<c-1;j++)
            if(s[i][j]=='#' && s[i][j+1]=='#' && s[i+1][j]=='#' && s[i+1][j+1]=='#') {
                changes++;
                fx=i; fy=j; break;
            }
            if(fx!=-1) break;
        }
        
        if(fx!=-1){
            s[fx][fy]='/'; s[fx][fy+1]='\\';
            s[fx+1][fy]='\\'; s[fx+1][fy+1]='/';
        }
        } //while
        
        int yes=1;
        for(int i=0;i<r;i++) for(int j=0;j<c;j++) if(s[i][j]=='#'){ yes=0; break; }
        
        printf("Case #%d:\n",t);
        if(yes){
            for(int i=0;i<r;i++){
                for(int j=0;j<c;j++){
                    printf("%c",s[i][j]);
                }
                printf("\n");
            }
        } else{
            printf("Impossible\n");
        }
    }
}
