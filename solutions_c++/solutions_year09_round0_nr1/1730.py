
#include <iostream>
#include <cstdio>
#include <cctype>
using namespace std;

int parse(int ok[], int pos){
        int c=getchar();
        if(c==EOF || c=='\n')return 0;

        if(isalpha(c)){
                ok[pos]|=(1<<(c-'a'));
        }else{
                while(1){
                        int d=getchar();
                        if(d==')')break;
                        ok[pos]|=(1<<(d-'a'));
                }
        }
        parse(ok,pos+1);

        return 0;
}

int main(){
        int l,d,n;scanf("%d%d%d",&l,&d,&n);
        char word[d][l+2];
        for(int i=0;i<d;i++)scanf("%s",word[i]);

        for(int npr=0;npr<n;npr++){
                int ok[l];memset(ok,0,sizeof(ok));
                scanf(" ");parse(ok,0);

                int ans=0;
                for(int i=0;i<d;i++){
                        int ng=0;
                        for(int k=0;ng==0 && k<l;k++){
                                if( (ok[k] & (1<<(word[i][k]-'a'))) ==0)ng=1;
                        }
                        if(ng==0)ans++;
                }

                printf("Case #%d: %d\n",npr+1,ans);
        }

        return 0;
}
