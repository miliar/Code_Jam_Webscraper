#include <stdio.h>

int each[105];
int extra[105];
int pass[105];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    
    int Test;
    scanf("%d",&Test);
    for(int t=1;t<=Test;t++){
        int n, s, p;
        scanf("%d %d %d",&n, &s, &p);
        for(int i=0;i<n;i++){
            int get;
            scanf("%d",&get);
            extra[i] = get % 3;
            each[i] = get / 3;
            if(each[i] >= p)
                pass[i] = 1;
            else 
                pass[i] = 0;
        }
        int ch = 1;
        do {
            ch = 0;
            for(int i=0;i<n;i++){
                if(!pass[i]){
                    if(extra[i] == 1){
                        if(each[i] + 1 >= p)
                            pass[i] = 1;
                    } else if(extra[i] == 2){
                        if(each[i] + 1 >= p)
                            pass[i] = 1;
                        else if(each[i] + 2 >= p && s){
                            ch = 1;
                            s--;
                            pass[i] = 1;
                        }
                    } else {
                        if(each[i] + 1 >= p && s && each[i] > 0){
                            ch = 1;
                            s--;
                            pass[i] = 1;
                        }
                    }
                }
            }
        } while(s && ch);
        int ans = 0;
        for(int i=0;i<n;i++)
            ans += pass[i];
        printf("Case #%d: %d\n", t, ans);
    }
    
return 0;
}
