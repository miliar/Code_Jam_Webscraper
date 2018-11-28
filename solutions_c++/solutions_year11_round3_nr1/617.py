#include <stdio.h>
#include <iostream>
using namespace std;

char a[100][100];
int t,r,c;

bool hefa(int i,int j){
    if(i>=r||j>=c)
        return 0;
    if(a[i][j]!='#')
        return 0;
    return 1;
}

bool get(){
    int i,j;
    for(i=0;i<r;++i){
        for(j=0;j<c;++j){
            if(a[i][j]=='#'){
                a[i][j]='/';
                if(!hefa(i+1,j))
                    return 0;
                else
                    a[i+1][j]='\\';

                if(!hefa(i,j+1))
                    return 0;
                else
                    a[i][j+1]='\\';

                if(!hefa(i+1,j+1))
                    return 0;
                else
                    a[i+1][j+1]='/';
            }
        }
    }
    return 1;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A.txt","w",stdout);
    int i,j;
    scanf("%d",&t);
    for(i=1;i<=t;++i){
        printf("Case #%d:\n",i);
        scanf("%d%d",&r,&c);
        for(j=0;j<r;++j)
            scanf("%s",a[j]);
        if(!get())
            printf("Impossible\n");
        else
            for(j=0;j<r;++j)
                printf("%s\n",a[j]);
    }
    return 0;
}

