#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
char MAP[]="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
void convert(char str[],int n,int B)
{
	int k=0;
	while(n){
		str[k++]=MAP[n%B];
		n/=B;
	}
	str[k]='\0';
}

bool check(int base,int num,int deep)
{
    if(deep>10)return false;
    char str[100];
    convert(str,num,base);
    int x=0;
    for(int i=0;str[i];i++)
        x+=(str[i]-'0')*(str[i]-'0');
    if(x==1)return true;
    return check(base,x,deep+1);


}



int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,a[11];
    scanf("%d",&T);
    int C=1;
    while(T--){
        int n=0;
        do{
            scanf("%d",&a[n]);
            n++;

            if(getchar()=='\n')break;
        }while(true);
        sort(a,a+n);
        int i,j;
        for( i=2; ;i++){
//            printf("%d ",i);
            for( j=0;j<n;j++){
                if( !check(a[j],i,0))break;

            }
            if( j==n)break;
        }
        printf("Case #%d: %d\n",C,i);
        C++;
        
    }
    return 0;
}