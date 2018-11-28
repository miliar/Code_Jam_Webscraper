#include<stdio.h>

int main(){

    char rep[26][26],c1,c2,c3,str[101],temp;
    int del[26], count[26];
    int T, N, cas = 0,ind;
    scanf("%d", &T);
    while (cas++ < T) {
        /*reset*/
        ind=0;
        for(int i=0;i<26;i++) {
            del[i]=count[i]=0;
            for(int j=0;j<26;j++) {
                rep[i][j]=0;
            }
        }
        /*read transformation*/
        scanf("%d ",&N);
        for(int i=0; i<N;i++) {
            scanf("%c%c%c ",&c1,&c2,&c3);
//            printf("\nc: %c%c=%c",c1,c2,c3);
            rep[(c1-'A')][(c2-'A')] = c3;
            rep[(c2-'A')][(c1-'A')] = c3;
        }
        scanf("%d ", &N);
        for(int i=0;i<N;i++) {
            scanf("%c%c ",&c1,&c2);
//            printf("\ndel:%c,%c",c1,c2);
            del[(c1-'A')]=c2;
            del[(c2-'A')]=c1;
        }
        /*process string*/
        scanf("%d ", &N);
//        printf("\n%d\n",N);
        for(int i=0;i<N;i++,ind++) {
            if(ind == 0){
                scanf("%c",str+ind);
//                printf("%c",str[ind]);
                count[str[ind]-'A']++;
//                printf("\n count:%c,%d\n",str[ind],count[str[ind]-'A']);
                continue;
            }
            scanf("%c",str+ind);
//            printf("%c",str[ind]);
            if(rep[str[ind-1]-'A'][str[ind]-'A']!=0){
                count[str[ind-1]-'A']--;
//                printf("\n count:%c,%d\n",str[ind-1],count[str[ind-1]-'A']);
                str[(ind-1)] = rep[str[ind-1]-'A'][str[ind]-'A'];
                ind--;
                count[str[ind]-'A']++;
//                printf("\n count:%c,%d\n",str[ind],count[str[ind]-'A']);
            }
            temp=del[str[ind]-'A'];
            if(temp != 0){
                if(count[temp-'A'] > 0){
                    ind=-1;
                    for(int j=0;j<26;j++){
                        count[j]=0;
                    }
                    continue;
                }
            }
            count[str[ind]-'A']++;
        }
        printf("Case #%d: [",cas);
        for(int i=0;i<ind;i++){
            if(i == 0){
                printf("%c",str[i]);
            }
            else {
                printf(", %c",str[i]);
            }
        }
        printf("]\n");
    }
    return 0;
}
