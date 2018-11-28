#include<cstdio>
#include<cstring>
int i,len,j,n,ca;
char a[200];

int check(int x){
    if (x==1) return 25; else
    if (x==2) return 8; else
    if (x==3) return 5; else
    if (x==4) return 19; else
    if (x==5) return 15; else
    if (x==6) return 3; else
    if (x==7) return 22; else
    if (x==8) return 24; else
    if (x==9) return 4; else
    if (x==10) return 21; else
    if (x==11) return 9; else
    if (x==12) return 7; else
    if (x==13) return 12; else
    if (x==14) return 2; else
    if (x==15) return 11; else
    if (x==16) return 18; else
    if (x==17) return 26; else
    if (x==18) return 20; else
    if (x==19) return 14; else
    if (x==20) return 23; else
    if (x==21) return 10; else
    if (x==22) return 16; else
    if (x==23) return 6; else
    if (x==24) return 13; else
    if (x==25) return 1; else
    if (x==26) return 17;
}
int main(){
    //freopen("a.in","r",stdin);
    //freopen("a.out","w",stdout);
    scanf("%d\n",&n);
    ca=0;
    for (i=1;i<=n;i++){
        printf("Case #%d: ",++ca);
        gets(a);
        len=strlen(a)-1;
        for (j=0;j<=len;j++)
        if (a[j]==' ') printf(" ");
        else printf("%c",check(a[j]-96)+96);
        printf("\n");
    }
    return 0;
}
