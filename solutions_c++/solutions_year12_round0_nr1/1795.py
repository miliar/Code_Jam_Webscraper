#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
using namespace std;
char st[100001];
int t;

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&t);
    getchar();
    for (int j=1;j<=t;j++){
        gets(st);
        printf("Case #%d: ",j);
        int l=strlen(st);
        for (int i=0;i<l;i++){
            if (st[i]==' ') printf(" ");
            if (st[i]=='a') printf("y");
            if (st[i]=='b') printf("h");
            if (st[i]=='c') printf("e");
            if (st[i]=='d') printf("s");
            if (st[i]=='e') printf("o");
            if (st[i]=='f') printf("c");
            if (st[i]=='g') printf("v");
            if (st[i]=='h') printf("x");
            if (st[i]=='i') printf("d");
            if (st[i]=='j') printf("u");
            if (st[i]=='k') printf("i");
            if (st[i]=='l') printf("g");
            if (st[i]=='m') printf("l");
            if (st[i]=='n') printf("b");
            if (st[i]=='o') printf("k");
            if (st[i]=='p') printf("r");
            if (st[i]=='q') printf("z");
            if (st[i]=='r') printf("t");
            if (st[i]=='s') printf("n");
            if (st[i]=='t') printf("w");
            if (st[i]=='u') printf("j");
            if (st[i]=='v') printf("p");
            if (st[i]=='w') printf("f");
            if (st[i]=='x') printf("m");
            if (st[i]=='y') printf("a");
            if (st[i]=='z') printf("q");
        }
        printf("\n");
    }
}
/*

ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
 
 */
