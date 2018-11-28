#include<iostream>
#include<cstdio>
#include<algorithm>
#define MAX 110
using namespace std;

int main(){
    int t,n,s,p,i,j,a[MAX+1],t1,t2,count,cas=1;
    scanf("%d",&t);
    while (t--){
          scanf("%d%d%d",&n,&s,&p);
          pair<int,int>pq[MAX+1],pq1[MAX+1];
          for (i=0;i<n;++i){
              scanf("%d",&a[i]);
              if (a[i]%3==0){t1=a[i]/3;   t2=t1+1;}
              if (a[i]%3==1){t1=a[i]/3+1; t2=t1+0;}
              if (a[i]%3==2){t1=a[i]/3+1; t2=t1+1;}
              if (a[i]==0)t2=0;
              pq[i].first = t1;
              pq[i].second = t2;
              }
          sort(pq,pq+n);
          //for (i=0;i<n;++i){cout<<pq[i].first<<"-"<<pq[i].second<<"  ";}cout<<endl;
          count=0;
          for (i=0;i<n;++i){
              if (pq[i].first>=p)break;
              }
          count+=(n-i);
          for (j=0;j<i;++j){
              pq1[j].first=pq[j].second;
              pq1[j].second=pq[j].first;
              }
          sort(pq,pq+j);
          //cout<<count<<endl;
          //for (i=0;i<j;++i){cout<<pq1[i].first<<"-"<<pq1[i].second<<"  ";}cout<<endl;
          for (i=0;i<j;++i){
              if (s==0)break;
              if (pq1[i].first>=p){++count;--s;}
              }
          printf("Case #%d: %d\n",cas,count);
          ++cas;
          }
    
    return 0;
    } 
