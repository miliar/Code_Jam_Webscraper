#include<cstdio>
using namespace std;

int main(){
    FILE* fin = fopen("D-large.in","r");
    FILE* fout = fopen("D-large.out","w");
    int t;
    int sum,n,in;
    fscanf(fin,"%d",&t);
    for(int i = 1;i <= t;i ++){
        sum = 0;
        fscanf(fin,"%d",&n);
        for(int j = 1;j <= n;j ++){
            fscanf(fin,"%d",&in);
            if(in != j){
                sum ++;
            }
        }
        fprintf(fout,"Case #%d: %d.000000\n",i,sum);
    }

    return 0;
}
