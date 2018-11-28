#include<iostream>
using namespace std;
int l,n,m;
int a[120][120]={0};
int b[120][120],c[100],k;
void dpf(int i0,int j0)
{
    int i1=i0,j1=j0,mi=a[i0][j0];
    int fx[4][2]={-1,0,0,-1,0,1,1,0};
    for(int z=0;z<4;z++){
        int i2=i0+fx[z][0],j2=j0+fx[z][1];
        if(i2>=0&&i2<n&&j2>=0&&j2<m){
            if(a[i2][j2]<mi){
                i1=i2;
                j1=j2;
                mi=a[i2][j2];
            }    
        }    
    }    
    if(i1==i0&&j1==j0){
        b[i0][j0]=k++;
    }    
    else{
        if(b[i1][j1]==-1)
            dpf(i1,j1);
        b[i0][j0]=b[i1][j1];
    }    
}    
int main(void)
{
    FILE *fin = fopen("B-large.in","r");
    FILE *fout = fopen("B-large.out","w");
    fscanf(fin,"%d",&l);
    for(int cas=1;cas<=l;cas++){
        fscanf(fin,"%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++){
                fscanf(fin,"%d",&a[i][j]);
                b[i][j]=-1;
            }    
        k=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(b[i][j]==-1)
                    dpf(i,j);
        int kk=0;
        for(int i=0;i<100;i++)
            c[i]=-1;
        fprintf(fout,"Case #%d:\n",cas);
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(c[b[i][j]]==-1)
                    c[b[i][j]]=kk++;
                if(j<m-1)
                    fprintf(fout,"%c ",c[b[i][j]]+'a');
                else
                    fprintf(fout,"%c\n",c[b[i][j]]+'a');
            }    
        }    
    }    
    //system("pause");
    return 0;
}    
