
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const char str[]="welcome to code jam";

int main(){
        int n;scanf("%d",&n);
        for(int npr=1;npr<=n;npr++){
                scanf(" ");
                char buf[600];fgets(buf,sizeof(buf),stdin);
                int len=strlen(buf);
                if(buf[len-1]=='\n')buf[--len]=0;

                int lenstr=strlen(str);
                int cnt[1+len][lenstr];memset(cnt[0],0,sizeof(cnt[0]));
                for(int i=0;i<len;i++){
                        //for(int k=0;k<lenstr;k++)cout<<cnt[i][k]<<" ";cout<<endl;
                        for(int k=0;k<lenstr;k++){
                                cnt[i+1][k]=cnt[i][k];
                                if(buf[i]==str[k]){
                                        if(k==0)cnt[i+1][k]+=1;
                                        else    cnt[i+1][k]+=cnt[i][k-1];
                                }
                                cnt[i+1][k]%=1000;
                        }
                }

                printf("Case #%d: %04d\n",npr,cnt[len][lenstr-1]);
        }

        return 0;
}
