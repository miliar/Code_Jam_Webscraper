#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>

using namespace std;

const int x[4][2]={0,1,1,1,1,0,1,-1};
char s[100][100],c[100][100];
int n,k;
bool red,blue;

bool check(){
     if(!red){
         for(int i=0;i<n;++i) if(!red)
             for(int j=0;j<n;++j) if(!red)
                 if(c[i][j]=='R'){
//                    printf("(%d,%d) ",i,j);
                     int l;
                     for(int t=0;t<4;++t) if(!red){
                         l=1;
                         while(c[i+l*x[t][0]][j+l*x[t][1]]=='R' && i+l*x[t][0]<n && j+l*x[t][1]>=0 && j+l*x[t][1]<n) ++l;
                         if(l>=k) red=true;
//                         cout<<l<<" ";
                     }
//                     cout<<endl;
                 }
     }
     if(!blue){
         for(int i=0;i<n;++i) if(!blue)
             for(int j=0;j<n;++j) if(!blue)
                 if(c[i][j]=='B'){
//                    printf("(%d,%d) ",i,j);
                     int l;
                     for(int t=0;t<4;++t) if(!blue){
                         l=1;
                         while(c[i+l*x[t][0]][j+l*x[t][1]]=='B' && i+l*x[t][0]<n && j+l*x[t][1]>=0 && j+l*x[t][1]<n) ++l;
                         if(l>=k) blue=true;
//                         cout<<l<<" ";
                     }
//                     cout<<endl;
                 }
     }
}

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int casenum;
    scanf("%d",&casenum);
    for(int t=1;t<=casenum;++t){
        red=false,blue=false;
        scanf("%d %d\n",&n,&k);
        memset(c,0,sizeof(c));
        for(int i=0;i<n;++i) cin.getline(s[i],100);
        
        for(int i=0;i<n;++i) for(int j=0;j<n;++j) c[i][j]=s[i][j];
        for(int j=n-2;j>=0;--j)
            for(int i=0;i<n;++i)
                if(c[i][j]!='.')
                    for(int k=j+1;(c[i][k]=='.' && k<n);++k) c[i][k]=c[i][k-1],c[i][k-1]='.';
   //     cout<<endl;
   //     for(int i=0;i<n;++i) cout<<c[i]<<endl;
        check();
        
        printf("Case #%d: ",t);
        if(red && blue) printf("Both\n");
        else if(red) printf("Red\n");
        else if(blue) printf("Blue\n");
        else printf("Neither\n");
    }
    return 0;
}
