#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int l,d,n;
int match(char * soal,  char * st){
    int inc,i,j,len;
    
    for(i=0,j=0,len=l;i<len;i++,j++){
        if(soal[j]=='('){
            inc=0;
            while(soal[j]!=')'){
                if(st[i]==soal[j]) inc=1;
                j++;
            }
            if(inc==0)return 0;
        }else{
            if(soal[j]!=st[i])return 0;
        }
    }
    return 1;
}

char st[6000][20];
char soal[2000];

int main(){
    int i,j,ans;
    
    scanf("%d %d %d",&l,&d,&n);
    for(i=0;i<d;i++){
        scanf("%s",st[i]);
    }
    for(i=0;i<n;i++){
        scanf("%s",soal);
        ans=0;
        for(j=0;j<d;j++){
            if(match(soal,st[j]))ans++;
        }
        printf("Case #%d: %d\n",i+1,ans);
    }
    
    return 0;
}
