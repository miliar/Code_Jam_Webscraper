#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <algorithm>
using namespace std;
#define SZ 102
struct node{
    bool r;
    int p;
}k[SZ];
int N;
char getR(){
    char ans;
    while(ans=getchar(), ans!='O' && ans!='B');
    return ans;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, res, cs, i;
    int b, o, tmp1, tmp2, tmp;
    char r;

    scanf("%d", &T);
    for(cs=1; cs<=T; cs++){
        scanf("%d", &N);
        b=o=1;
        res=0;
        memset(k, 0, sizeof(k));
        for(i=0; i<N; i++){
            r=getR();
            scanf("%d", &k[i].p);
            if(r=='B')k[i].r=0;
            else k[i].r=1;
        }
        if(N==1){
            if(k[0].r==0)res=abs(k[0].p-b)+1;
            else res=abs(k[0].p-o)+1;
            printf("Case #%d: %d\n", cs, res);
            continue;
        }
        for(i=0; i<N; ){
            tmp=0;
			tmp2=k[i].r;
            while(i<N-1){
				if(k[i].r==k[i+1].r){
					if(k[i].r==0){
						tmp+=abs(k[i].p-b)+1;
						b=k[i].p;
						tmp2=0;
					}
					else {
						tmp+=abs(k[i].p-o)+1;
						o=k[i].p;
						tmp2=1;
					}
				}
				else {
					if(k[i].r==0){
						tmp+=abs(k[i].p-b)+1;
						b=k[i].p;
						tmp2=0;
					}
					else {
						tmp+=abs(k[i].p-o)+1;
						o=k[i].p;
						tmp2=1;
					}
					i++;
					break;
				}
                i++;
            }
            if(i==N-1 && i>=1 && k[i].r==k[i-1].r){
                if(k[i].r==0)res+=tmp+abs(k[i].p-b)+1;
                else res+=tmp+abs(k[i].p-o)+1;
                break;
            }

            if(tmp2==0){
                res+=tmp;
                if(i<N-1){
                    tmp1=abs(k[i].p-o)+1;
                    if(tmp1<=tmp){o=k[i].p;}
                    else {
						if(k[i].p-o>=0){o+=tmp; o=(o<=100)?o:100;}
						else {o-=tmp; o=o>0?o:1;} 
					}
                }
                else if(i==N-1){
                    tmp1=abs(k[i].p-o)+1;
                    if(tmp1<=tmp){res++; break;}
                    else {res+=tmp1-tmp;break;}
                }
            }
            else{
                res+=tmp;
                if(i<N-1){
                    tmp1=abs(k[i].p-b)+1;
                    if(tmp1<=tmp){b=k[i].p;}
					else { 
						if(k[i].p-b>=0){b+=tmp; b=(b<=100)?b:100;}
						else {b-=tmp; b=b>0?b:1;}
					}
                }
                else if(i==N-1){
                    tmp1=abs(k[i].p-b)+1;
                    if(tmp1<=tmp){res++; break;}
                    else {res+=tmp1-tmp;break;}
                }

            }
        }

        printf("Case #%d: %d\n", cs, res);
    }
    return 0;
}
