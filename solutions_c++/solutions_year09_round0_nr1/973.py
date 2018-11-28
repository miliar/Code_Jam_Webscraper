/* 
 * File:   A.cpp
 * Author: GongZhi
 * Problem:
 * Created on 2009年9月3日, 下午8:24
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

/*
 *
 */
char data[5100][20];
char temp[5100];
char mark[200][100];
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int l,d,n;
    int i,k,j;
    int ans;
    scanf("%d%d%d",&l,&d,&n);
    for(i=0;i<d;i++)scanf("%s",data[i]);
    for(k=1;k<=n;k++){
        ans=0;
        memset(mark,0,sizeof(mark));
        scanf("%s",temp);
        i=0;
        j=0;
        int f=0;
        while(temp[i]){
            if(temp[i]=='('){
                f=1;
                i++;
                continue;
            }
            if(temp[i]==')'){
                f=0;
                i++;
                j++;
                continue;
            }
            mark[j][temp[i]-'a']=1;
            i++;
            if(f==0)j++;
        }
        ans=0;
        for(j=0;j<d;j++){
            for(i=0;i<l;i++)if(mark[i][data[j][i]-'a']==0)break;
            if(i==l)ans++;
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}

