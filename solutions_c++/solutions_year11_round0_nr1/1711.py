#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int ab(int x){
    return x>0?x:-x;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large-out.txt","w",stdout);

    int T,N;
    scanf("%d",&T);
    for(int _case=1;_case<=T;_case++){
        scanf("%d",&N);
        int p1=1,p2=1,c1=0,c2=0,a,d,cost=0;
        char ch;
        for(int i=0;i<N;i++){
            scanf(" %c %d",&ch,&a);
            if(ch=='O'){
                d=ab(a-p1);
                p1=a;
                if(d>c2){
                    cost+=d-c2;
                    c1+=d-c2;
                }
                cost++;
                c1++;
                c2=0;
            }
            else{
                d=ab(a-p2);
                p2=a;
                if(d>c1){
                    cost+=d-c1;
                    c2+=d-c1;
                }cost++;
                c2++;
                c1=0;
            }
        }
        printf("Case #%d: %d\n",_case,cost);

    }

    return 0;
}
