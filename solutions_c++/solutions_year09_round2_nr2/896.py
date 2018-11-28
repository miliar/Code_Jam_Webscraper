#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>

const int size = 25;
int n;
char now[size];
char map[size];
int mark[10];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&n);
    for(int _case = 1 ; _case <= n ; _case++){
            scanf("%s",now);
            if( strcmp (now,"100000000000000000000") == 0  )
            {
            printf("Case #%d: 1000000000000000000000\n",_case);
            continue;
            }
            printf("Case #%d: ",_case);
            int len = strlen(now);
            int j = len;
           // printf("%c\n",now[j-1]);
            for(int i = 20 ; i>=0 ; i--){
                if(j<=0) map[i] = '0';
                else{
                     --j;
                     map[i] = now[j];
                     //printf("?? %d %c\n",i,now[j]);
                }
            }
            map[21] = '\0';
            //printf("    %s\n",map);
            memset(mark,0,sizeof(mark));
            int wei = 20;
            int ht = map[20] - '0';
            int res = ht;
            mark[ht]++;
            for(int i = 19 ; i>=0 ;i-- ){
                if( map[i]-'0' >= ht ) {
                    mark[ map[i]-'0' ]++;
                    ht = map[i]-'0';
                    continue;
                }
                else{
                    wei = i ;
                    res = map[i] - '0';
                    break;
                }
            }
            for(int i = 0 ; i<= 9 ; i++){
                 if(mark[i] && i>res){
                    mark[i]--;
                    map[wei] ='0'+i;
                    mark[res]++;
                    break;
                 }
            }

            int key  = 0;

            for(int i = 0 ; i<= wei ; i++){
                if(key == 0 && map[i]=='0') continue;
                key = 1;
                printf("%c",map[i]);
            }
            for(int i = 0 ; i<=9; i++){
                while(mark[i]){
                    printf("%c",i+'0');
                    mark[i]--;
                }
            }
            printf("\n");
    }


    return 0;
}
