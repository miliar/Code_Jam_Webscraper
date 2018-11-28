#include <iostream>

using namespace std;

int main(){
    freopen("B-small-0.in","r",stdin);
    freopen("B-small-0.out","w",stdout);
    int t, n, s, p, x, ans;
    scanf("%d\n", &t);
    for(int i=0;i<t;i++){
        ans = 0;
        scanf("%d %d %d", &n, &s, &p);
        for(int j=0;j<n;j++){
            scanf(" %d", &x);
            switch(x%3){
                case 0:
                    if(x/3 >= p)    ans++;
                    else{
                        if((x-3)/3+2 >= p && s > 0 && x-3 > 0){
                            ans++;
                            s--;
                            }
                        }
                    break;
                case 1:
                    if((x-1)/3+1 >= p)    ans++;
                    else{
                        if((x-1)/3+1 >= p && s > 0){
                            ans++;
                            s--;
                            }
                        }
                    break;
                case 2:
                    if((x-2)/3+1 >= p)    ans++;
                    else{
                        if((x-2)/3+2 >= p && s > 0){
                            ans++;
                            s--;
                            }
                        }
                    break;
                }
            }
        printf("Case #%d: %d\n", i+1, ans);
        }
    return 0;
    }
