#include<iostream>
#include<cstring>
char s[333];
int x[333];
int y[40000000][11];
int chk(int num,int b){
    int p=0,n;
    if(num==1){
        return 1;
    }
    if(!y[num][b]){
        y[num][b]=2;
        n = num;
        while(n!=0){
            p+=(n%b)*(n%b);
            n/=b;
        }
        if(y[p][b]){
            y[num][b]=y[p][b];
        }else{
            y[num][b]=chk(p,b);
        }
    }
    return y[num][b];
}
main(){
    int ti,tt,n,i,j,fl;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    for(i=2;i<=10;i++){
        y[1][i]=1;
    }
    scanf("%d",&tt);
    gets(s);
    for(ti=1;ti<=tt;ti++){
        gets(s);
        n = (strlen(s)+1)/2;
        for(i=0;i<n;i++){
            x[i]=s[i*2]-'0';
        }
        if(strlen(s)%2==0){
            x[n-1]=10;
        }
        for(i=2;;i++){
            fl=0;
            for(j=0;j<n;j++){
                if(chk(i,x[j])!=1){
                    fl=1;
                    break;
                }
            }
            if(!fl){
                printf("Case #%d: %d\n",ti,i);
                fflush(stdout);
                break;
            }
        }
    }
    return 0;
}
