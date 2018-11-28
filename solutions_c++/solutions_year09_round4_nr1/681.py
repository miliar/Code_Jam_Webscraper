#include<iostream>
using namespace std;
int main(void)
{
    FILE *fin = fopen("A-large.in","r");
    FILE *fout = fopen("A-large.out","w");
    int num,n,b[50],ans,temp;
    char a[50][50];
    fscanf(fin,"%d",&num);
    for(int cas=1;cas<=num;cas++){
        fscanf(fin,"%d",&n);
        for(int i=0;i<n;i++){
            b[i]=-1;
            fscanf(fin,"%s",&a[i]);
            for(int j=0;j<n;j++){
                if(a[i][j]=='1')
                    b[i]=j;
            }    
        }    
        ans=0;
        for(int i=0,j;i<n;i++){
            for(j=i;b[j]>i;j++);
            ans+=j-i;
            temp=b[j];
            for(int k=j-1;k>=i;k--)
                b[k+1]=b[k];
            b[i]=temp;
        }    
        fprintf(fout,"Case #%d: %d\n",cas,ans);
    }    
    fclose(fout);
    fclose(fin);
    system("pause");
    return 0;
}    
