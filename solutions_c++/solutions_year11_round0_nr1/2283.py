#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    //freopen("in.txt","r",stdin);
    int T;
    cin>>T;
    for (int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        int k;
        cin>>k;
        int s[2];
        s[0]=s[1]=1;
        k--;
        char ch;
        int x;
        int cnt=0,last=0;
        int who=0;
        cin>>ch>>x;
        cnt=x;
        if (ch=='O'){
            who=0;
        }else{
            who=1;
        }
        s[who]=x;
        while (k--){
            char ch;
            int x;
            int w;
            cin>>ch>>x;
            if (ch=='O'){
                w=0;
            }else{
                w=1;
            }
            if (w==who){
                int temp=s[w]-x;
                if (temp<0)
                    temp=-temp;
                s[w]=x;
                cnt+=temp+1;
            }else{
                int temp=s[w]-x;
                if (temp<0)
                    temp=-temp;
                int length=cnt-last;
                if (length<temp){
                    last=cnt;
                    cnt+=temp-length+1;
                }else{
                    last=cnt;
                    cnt++;
                }
                who=w;
                s[w]=x;
            }
        }
        printf("%d\n",cnt);
    }
    return 0;
}