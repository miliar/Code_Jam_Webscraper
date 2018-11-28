#include<iostream>
#include<vector>
using namespace std;
int h,w;
int a[101][101];
char l[101][101],ch;
struct st{int h,x,y;};
char move(int i,int j){ 
     if( l[i][j]>0) return l[i][j];
     int mi=10000000,ii,jj;
     ii=i+1; jj=j;
     if( ii<h   &&  mi>a[ii][jj]  && a[i][j]>a[ii][jj] ) mi=a[ii][jj];
     ii=i-1; jj=j;
     if( ii>=0   &&  mi>a[ii][jj] && a[i][j]>a[ii][jj]) mi=a[ii][jj];
     ii=i; jj=j+1;
     if( jj<w   &&  mi>a[ii][jj] && a[i][j]>a[ii][jj]) mi=a[ii][jj];
     ii=i; jj=j-1;
     if( jj>=0  &&  mi>a[ii][jj] && a[i][j]>a[ii][jj]) mi=a[ii][jj];
     
     ii=i-1; jj=j;
     if( ii>=0    &&  mi==a[ii][jj]){ l[i][j]=move(ii,jj); return l[i][j];}
     else{
       ii=i; jj=j-1;
       if( jj>=0   &&  mi==a[ii][jj]){ l[i][j]=move(ii,jj);return l[i][j];}
       else{
         ii=i; jj=j+1;
         if( jj<w    &&  mi==a[ii][jj]){ l[i][j]=move(ii,jj);return l[i][j];}
         else{
           ii=i+1; jj=j;
           if( ii<h   &&  mi==a[ii][jj]){ l[i][j]=move(ii,jj);return l[i][j];}
           else {  ch++; l[i][j]=ch;return ch;}
         }
       }
     }
    
}
bool cmp(st aa,st bb){ 
     if( aa.h !=bb.h) return aa.h>bb.h;
     if( aa.x !=bb.x) return aa.x<bb.x;
     return aa.y<bb.y;
}
void bfs(int i,int j,char c){ 
     if( i+1<h &&  c==l[i+1][j]) {l[i+1][j]=ch; bfs(i+1,j,c);}
     if( j+1<w &&  c==l[i][j+1]) {l[i][j+1]=ch; bfs(i,j+1,c);}
     if( i-1>=0 && c==l[i-1][j]) {l[i-1][j]=ch; bfs(i-1,j,c);}
     if( j-1>=0 && c==l[i][j-1]) {l[i][j-1]=ch; bfs(i,j-1,c);}
}
int main(){
    int t;cin>>t; int caseid=1;
    while(t--){
       cin>>h>>w;
       vector<st > v;
       for(int i=0;i<h;i++)
         for(int j=0;j<w;j++){
           cin>>a[i][j];
           st s; s.h=a[i][j];
           s.x=i; s.y=j; v.push_back(s);
         }
       memset(l,-1,sizeof(l));
       ch='A';
       sort(v.begin(),v.end(),cmp);
       int sz=v.size();
       for(int i=0;i<sz;i++){
          int x,y; x=v[i].x; y=v[i].y;
          if( int(l[x][y])==-1 ){ l[x][y]=move(x,y); }
       }
        printf("Case #%d:\n",caseid); caseid++; 
        ch='a';
        for(int i=0;i<h;i++)
          for(int j=0;j<w;j++)
            if( l[i][j]<'a' ){ char tchar; tchar=l[i][j]; l[i][j]=ch; bfs(i,j,tchar); ch++;}
        for(int i=0;i<h;i++){
           for(int j=0;j<w-1;j++)
             cout<<l[i][j]<<" ";
             cout<<l[i][w-1]<<endl;
        }                         
    }
    return 0;
}
