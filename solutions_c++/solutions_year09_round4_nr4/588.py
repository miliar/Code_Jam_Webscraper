#include<iostream>
#include<math.h>
using namespace std;
int n;
struct node{
    double x,y,r;
}p[50];    
double ans,temp;
double dist(int i,int j)
{
    double len=sqrt((p[i].x-p[j].x)*(p[i].x-p[j].x)+
             (p[i].y-p[j].y)*(p[i].y-p[j].y));
    len+=p[i].r+p[j].r;
    return len;
}    
int main(void)
{
    FILE *fin = fopen("D-small-attempt0.in","r");
    FILE *fout = fopen("D-small-attempt0.out","w");
    int num;
    fscanf(fin,"%d",&num);
    for(int cas=1;cas<=num;cas++){
        fscanf(fin,"%d",&n);
        for(int i=0;i<n;i++)
            fscanf(fin,"%lf%lf%lf",&p[i].x,&p[i].y,&p[i].r);
        if(n==1){
            ans=p[0].r;
        }    
        else if(n==2){
            ans=p[0].r;
            if(p[1].r>ans)
                ans=p[1].r;
        }    
        else if(n==3){
            ans=dist(1,2)/2;
            if(p[0].r>ans)
                ans=p[0].r;
            temp=dist(0,2)/2;
            if(p[1].r>temp)
                temp=p[1].r;
            if(temp<ans)
                ans=temp;
            temp=dist(0,1)/2;
            if(p[2].r>temp)
                temp=p[2].r;
            if(temp<ans)
                ans=temp;
        }    
        fprintf(fout,"Case #%d: %lf\n",cas,ans);
    }    
    fclose(fout);
    fclose(fin);
    system("pause");
    return 0;
}    
