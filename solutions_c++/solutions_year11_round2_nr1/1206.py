#include<stdio.h>
#include<string.h>
#include<ctype.h>
double cal(char s[103][103],int n,int exclude,int now){
    int count=0;
    double temp=0;
    for(int j=0;j<n;j++)
        if(isdigit(s[now][j])&&j!=exclude){
            temp+=s[now][j]-'0';
            count++;
        }
    return temp/count;
}
int main(){
    int C,n,count,Case=1;
    double WP[3][103];
    char s[103][103];
    scanf("%d",&C);
    while(C--){
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%s",s[i]);
        memset(WP,0,sizeof(WP));
        for(int i=0;i<n;i++)
            WP[0][i]=cal(s,n,-1,i);
        for(int i=0;i<n;i++){
            count=0;
            for(int j=0;j<n;j++)
                if(isdigit(s[i][j])){
                    WP[1][i]+=cal(s,n,i,j);
                    count++;
                }
            WP[1][i]/=count;
        }
        for(int i=0;i<n;i++){
            count=0;
            for(int j=0;j<n;j++)
                if(isdigit(s[i][j])){
                    WP[2][i]+=WP[1][j];
                    count++;
                }
            WP[2][i]/=count;
        }
        /*for(int k=0;k<3;k++,puts("-----"))
            for(int i=0;i<n;i++,puts(""))
                printf("%.3lf ",WP[k][i]);*/
        printf("Case #%d:\n",Case++);
        for(int i=0;i<n;i++)
            printf("%.12lf\n",WP[0][i]*0.25+WP[1][i]*0.5+WP[2][i]*0.25);
    }
}
