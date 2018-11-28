#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#define PI 3.141592653589793
#define DEBUG 0
#define INF 1000000007 

using namespace std;

int n,A,B,cases;
vector<float>prob;
float del[101][101],tdel[101][101],tdel2[101][101],exd[101],head[101],back[101];
float minimum(float a,float b,float c){
    if(a<=b&&a<=c)return a;
    if(b<=a&&b<=c)return b;
    return c;
}
void init(){
    int i;
    head[1]=prob[0];back[A]=prob[A-1];
    for(i=2;i<=A;i++)head[i]=head[i-1]*prob[i-1];
    for(i=A-1;i>0;i--)back[i]=back[i+1]*prob[i-1];
}
void getNum(){
    int l,i,j,k;
    memset(del,0,101*101*sizeof(float));
    init();
    float keep,right=INF,part=prob[0];
    for(i=1;i<A;i++){part*=prob[i];}
    if(A==B)right=part*1+(1-part)*(2+B);
    else right = (2+B);
    keep=part*(B-A+1)+(1-part)*(B-A+2+B);
    
    tdel[0][0]=1;
    for(i=1;i<=A;i++){del[i][0]=head[i];tdel[i][0]=del[i][0];
        if(DEBUG)printf("%d %d: %f %f\n",i,0,del[i][0],del[i][0]);
        }
    for(l=1;l<=A;l++)
        for(j=l;j<=A;j++){
            del[j][l]=tdel[j-1][l-1]*(1-prob[j-1]);
            tdel[j][l]=tdel[j-1][l]+del[j][l];
            if(j+1<=A)tdel2[j][l]=tdel2[j-1][l]+del[j][l]*back[j+1];
            else tdel2[j][l]=tdel2[j-1][l]+del[j][l];
            if(DEBUG)printf("%d %d: %f %f %f\n",j,l,del[j][l],tdel[j][l],tdel[j-1][l-1]);
        }
    float min=INF,tmp;
    for(k=1;k<=A;k++){              //delete k chars
        for(i=1;i<=k;i++){
            tmp+=(tdel2[A][i]-tdel2[k][i])*(B-A+2*k+2+B)+tdel2[k][i]*(B-A+2*k+1);
            if(DEBUG)printf("tdel2[%d][%d](%d->%d): %f\n",k,i,k,(B-A+2*k+1),tdel2[k][i]);
            if(DEBUG)printf("%d-%d(%d->%d): %f\n",A,k,k,(B-A+2*k+2+B),tdel2[A][i]-tdel2[k][i]);
        }
        for(i=k+1;i<=A;i++)
            tmp+=(tdel2[A][i])*(B-A+2*k+2+B);//+tdel2[k][i]*(B-A+2*k+1);
        if(DEBUG)printf("part %f %d\n",part,(B-A+2*k+1));
        tmp+=part*(B-A+2*k+1);
        if(DEBUG)printf("k %d %f\n",k,tmp);
        if(tmp<min)min=tmp;
    }
    
    printf("Case #%d: %.6f\n",cases, minimum(keep,right,min));
}
int main(){
    int i,j;
    float a;
    vector<float>prob2;
    scanf("%d\n",&n);
    for(i=0;i<n;i++){
        cases = i+1;
        scanf("%d%d\n",&A,&B);
        prob.clear(),prob2.clear();
        for(j=0;j<A;j++){
            scanf("%f",&a);
            prob2.push_back(a);
        }
        for(j=prob2.size()-1;j>=0;j--)prob.push_back(prob2[j]);
        getNum();
    }
    return 0;
}
