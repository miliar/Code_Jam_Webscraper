/* 
 * File:   main.cpp
 * Author: perpetuity
 *
 * Created on 2011年5月7日, 上午7:58
 */

#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

/*
 * 
 */
char map1[128][128];
int map2[128][128];

int main(int argc, char** argv) {
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        int c;
        memset(map1,0,sizeof(map1));
        memset(map2,0,sizeof(map2));
        scanf("%d",&c);
        for(int i=0;i<c;i++){
            char str[4];
            scanf("%s",str);
            map1[str[0]][str[1]]=str[2];
            map1[str[1]][str[0]]=str[2];
        }
        int d;
        scanf("%d",&d);
        for(int i=0;i<d;i++){
            char str[4];
            scanf("%s",str);
            map2[str[0]][str[1]]=1;
            map2[str[1]][str[0]]=1;
        }
        int n;
        scanf("%d",&n);
        char s[101],r[101];
        scanf("%s",s);
        int len=0;
        for(int i=0;i<n;i++){
            if(len==0){
                r[0]=s[i];
                len++;
            }
            else{
                r[len]=s[i];
                len++;
                while(len>1&&map1[r[len-1]][r[len-2]]!=0){
                    r[len-2]=map1[r[len-1]][r[len-2]];
                    len--;
                }
                for(int j=0;j<len-1;j++){
                    if(map2[r[j]][r[len-1]]==1){
                        len=0;
                        break;
                    }
                }
            }
        }
        r[len]='\0';
        printf("Case #%d: [",cas);
        for(int i=0;i<len-1;i++)
            printf("%c, ",r[i]);
        if(len>0) printf("%c",r[len-1]);
        printf("]\n");
    }
    return 0;
}

