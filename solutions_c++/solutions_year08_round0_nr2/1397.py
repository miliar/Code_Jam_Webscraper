#include<stdio.h>
#include <fstream>
#include<iostream>
using namespace std;
struct node{
    int st;
    int et;
}a[120],b[120];
bool cmpst(node p,node q)
{
    return p.st<q.st;
}        
bool cmpet(node p,node q)
{
    return p.et<q.et;
}    
int main(void)
{
    FILE *fin  = fopen ("B-large.in", "r");
    FILE *fout = fopen ("B-large.out", "w");
    
    int num;
    fscanf(fin,"%d",&num);
    for(int k=1;k<=num;k++){
        int t,na,nb,ansa=0,ansb=0;
        fscanf(fin,"%d%d%d",&t,&na,&nb);
        ansa=na;
        ansb=nb;
        for(int i=0;i<na;i++){
            int h,m;
            fscanf(fin,"%d:%d",&h,&m);
            a[i].st=h*60+m;
            fscanf(fin,"%d:%d",&h,&m);
            a[i].et=h*60+m+t;
        }    
        for(int i=0;i<nb;i++){
            int h,m;
            fscanf(fin,"%d:%d",&h,&m);
            b[i].st=h*60+m;
            fscanf(fin,"%d:%d",&h,&m);
            b[i].et=h*60+m+t;
        }    
        sort(a,a+na,cmpst);
        sort(b,b+nb,cmpet);
        for(int i=0,j=0;i<na&&j<nb;i++,j++){
            while(i<na&&a[i].st<b[j].et)
                i++;
            if(i==na)
                break;
            ansa--;
        }    
        sort(b,b+nb,cmpst);
        sort(a,a+na,cmpet);
        for(int i=0,j=0;i<na&&j<nb;i++,j++){
            while(j<nb&&b[j].st<a[i].et)
                j++;
            if(j==nb)
                break;
            ansb--;
        }    
        fprintf(fout,"Case #%d: %d %d\n",k,ansa,ansb);
    }    
    return 0;
}    
