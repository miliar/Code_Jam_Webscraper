#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;


int main(){
    FILE* in;
    FILE* out;
    in=fopen("d:/input.in","r");
    out=fopen("d:/output.out","w");
    int nn;
    int normal[31];    normal[0]=0;
    int surp[31]; surp[0]=0; surp[1]=1;
    int c=1;
    for(int i=1;i<31;){
        if(i<=30)normal[i++]=c;
        if(i<=30)normal[i++]=c;
        if(i<=30)normal[i++]=c;
        c++;
    }
    c=2;
    for(int i=2;i<31;){
        if(i<=30)surp[i++]=c;
        if(i<=30)surp[i++]=c;
        if(i<=30)surp[i++]=c;
        c++;
    }
    fscanf(in,"%d",&nn);
    //scanf("%d",&nn);
    int n,s,p,count;
    int point[101];
    for(int i=1;i<=nn;i++){
        //scanf("%d %d %d",&n,&s,&p);
        fscanf(in,"%d %d %d",&n,&s,&p);
        for(int j=0;j<n;j++){
            //scanf("%d",&point[j]);
            fscanf(in,"%d",&point[j]);
        }
        sort(point,point+n);
        count=0;
        for(int j=n-1;j>=0;j--){
            if(normal[point[j]]>=p)count++;
            else if(surp[point[j]]>=p && s>0){
                count++;
                s--;
            }
        }
        //printf("Case #%d: %d",i,count);
        fprintf(out,"Case #%d: %d\n",i,count);
    }
    //system("pause");   
}
