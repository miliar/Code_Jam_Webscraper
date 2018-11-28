#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <memory.h>
using namespace std;
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    long turn,test,cnt,len,sum;
    long c,d,n,i,j;
    long hash[1000]={0},dh[200]={0},rd[200]={0},v26[200]={0},v1[200]={0};
    char str[2000],list[2000];
    for(i='A';i<='Z';i++){
        v1[i]=i-'A';
        v26[i]=(i-'A')*26;
    }
    scanf("%ld",&test);
    for(turn=1;turn<=test;turn++){
        printf("Case #%ld: ",turn);
        for(i='A';i<='Z';i++)
            dh[i]=rd[i]=0;
        memset(hash,0,sizeof(hash));
        scanf("%ld",&c);
        for(i=0;i<c;i++){
            scanf("%s",str);
            hash[v26[str[0]]+v1[str[1]]]=str[2];     //hash
            hash[v26[str[1]]+v1[str[0]]]=str[2];
        }
        scanf("%ld",&d);
        for(i=0;i<d;i++){
            scanf("%s",str);
            dh[str[0]]=str[1];
            dh[str[1]]=str[0];
        }
        scanf("%ld",&n);
        scanf("%s",list);
        len=strlen(list);
        cnt=-1;
        for(i=0;i<len;i++){
            if(cnt!=-1)
                sum=v26[str[cnt]]+v1[list[i]];
            else
                sum=999;
            if(hash[sum]==0){          //str's size
                str[++cnt]=list[i];
                rd[list[i]]++;
            }
            else{
                rd[str[cnt]]--;
                rd[hash[sum]]++;
                str[cnt]=hash[sum];
            }
            if(rd[dh[str[cnt]]]!=0){
                cnt=-1;
                for(j='A';j<='Z';j++)
                    rd[j]=0;
            }
        }
        //printf("cnt %ld\n",cnt);
        printf("[");
        for(i=0;i<cnt;i++){
            printf("%c, ",str[i]);
        }
        if(i==cnt)
            printf("%c",str[i]);
        printf("]\n");
    }
    return 0;
}
