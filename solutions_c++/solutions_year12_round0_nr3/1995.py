#include <iostream>
#include <stdio.h>
#define MAX 2000001
#define PMAX 8

using namespace std;

int list[PMAX];
int plist[PMAX];
int *found=new int[MAX];

void clear_plist(){
    for(int i=0;i<PMAX;i++)
        plist[i]=0;
}
bool exist_plist(int value){
    for(int i=0;i<PMAX;i++)
        if(plist[i]==value)
            return true;
    return false;
}
int to_list(int n){
    int length=0;
    while(n!=0){
        list[length++]= (n%10);
        n=n/10;
    }
    return length;
}
int to_int(int length){
    int n=0,m=1;
    for(int i=0;i<length;i++){
        n += (list[i]*m);
        m*=10;
    } return n;
}
void run_list(int from,int len){
    int t;
    for(int i=0;i<len;i++){
        t=list[from+1];
        list[from+1]=list[from];
        list[from--]=t;
     }
}
void move_list(int from,int length){
    int t,k=0;
    for(int i=from;i>=0;i--){
        for(int j=i;j<length-1-k;j++){
            t=list[j+1];
            list[j+1]=list[j];
            list[j]=t;
        }k++;
    }
}

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int c,n,m,mlen,nlen,new_n,total=0,out=false,pi=0;
    scanf("%i",&c);
    for(int i=1;i<MAX;i++){found[i]=0;}
    for(int i=0;i<c;i++){
        scanf("%i %i",&n,&m);
        total=0;
        for(int ni=n;ni<m;ni++){
            nlen = to_list(ni);
            pi=0;clear_plist();
            out=false;
            for(int j=0;j<nlen-1;j++){
                move_list(j,nlen);
                new_n = to_int(nlen);
                if(new_n>ni && new_n<=m){
                    if(!exist_plist(new_n)){
                        plist[pi++]=new_n;
                        total++;
                    }
                }to_list(ni);
            }
        }
        printf("Case #%i: %i\n",(i+1),total);
    }
    return 0;
}
