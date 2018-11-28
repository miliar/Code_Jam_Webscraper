#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,i,k,n,m,j,ct,ans,a[1000],b[1000],lena,lenb,OR,BL;
    char ch,c,list[1000];
    scanf("%d",&t);
    for(ct=1;ct<=t;ct++) {
        OR=BL=1;
        lena=lenb=ans=0;
        scanf("%d ",&n);
        for(i=0;i<n;i++) {
            scanf("%c %d%c",&ch,&m,&c);
            if(ch=='O') a[lena++]=m;
            else b[lenb++]=m;
            list[i]=ch;
        }
        
        i=j=k=0;
        while(1) {
            if(i==lena&&j==lenb) break;
            ans++;
            if(list[k]=='O'&&OR==a[i]) {
                i++;
                k++;
                if(j<lenb) {
                    if(BL<b[j]) BL++;
                    if(BL>b[j]) BL--;
                }
                continue;
            }
            if(list[k]=='B'&&BL==b[j]) {
                j++;
                k++;
                if(i<lena) {
                    if(OR<a[i]) OR++;
                    if(OR>a[i]) OR--;
                }
                continue;
            }
            if(i<lena) {
                if(OR<a[i]) OR++;
                if(OR>a[i]) OR--;
            }
            if(j<lenb) {
                if(BL<b[j]) BL++;
                if(BL>b[j]) BL--;
            }
            
            //printf("%d %d\n",OR,BL);
        }
        
        printf("Case #%d: %d\n",ct,ans);
    }
    return 0;
}
