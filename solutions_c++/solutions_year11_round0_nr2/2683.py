#include<stdio.h>

int co[256][256],op[256][256];

int main(){
    freopen("bin.txt", "r", stdin);
    freopen("bout.txt", "w", stdout);
    int t,Case=1;
    scanf("%d",&t);
    while(t--){
        int x=0;
        for(int i=0;i<256;i++){
            for(int j=0;j<256;j++){
                co[i][j]=0;
            }
        }
        for(int i=0;i<256;i++){
            for(int j=0;j<256;j++){
                op[i][j]=0;
            }
        }
        scanf("%d",&x);
        while(x--){
            char str[10];
            scanf("%s",str);
            co[str[0]][str[1]]=co[str[1]][str[0]]=str[2];
        }
        scanf("%d",&x);
        while(x--){
            char str[10];
            scanf("%s",str);
            op[str[0]][str[1]]=op[str[1]][str[0]]=1;
        }
        scanf("%d",&x);
        char str1[110];
        int achar[27];
        for(int i=0;i<27;i++){
            achar[i]=0;
        }
        scanf("%s",str1);
        char str2[110];
        int str2len=1; 
        str2[0]=str1[0];
        achar[str1[0]-'A']++;
        for(int i=1;i<x;i++){
            bool fr=true;
            if(str2len>0){
                char c=co[str1[i]][str2[str2len-1]];
                if(c>='A'&&c<='Z'){
                    achar[str2[str2len-1]-'A']--;
                    str2[str2len-1]=c;
                    fr=false;
                }
            }
            if(fr){
                int j;
                for(j=0;j<26;j++){
                    if(achar[j]>0&&op[str1[i]][j+'A']==1){
                        break;
                    }
                }
                if(j>=26){
                    str2[str2len++]=str1[i];
                    achar[str1[i]-'A']++;
                }
                else{
                    str2len=0;
                    for(j=0;j<27;j++){
                        achar[j]=0;
                    }
                }
            }
        }
        printf("Case #%d: [",Case++);
        if(str2len>0){
            printf("%c",str2[0]);
            for(int i=1;i<str2len;i++){
                printf(", %c",str2[i]);
            }
        }
        printf("]\n");
    }
    return 0;
}


