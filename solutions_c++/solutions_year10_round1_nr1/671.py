#include<iostream>
using namespace std;

const long dx[4]={1,0,1,1};
const long dy[4]={0,1,-1,1};

char c[200][200];
long n,m;
bool red,blue;

void init(){
     red=false;
     blue=false;
     memset(c,0,sizeof(c));
     cin>>n>>m;
     for(int i=1;i<=n;i++)
         for(int j=1;j<=n;j++)
             cin>>c[i][j];
}

bool search(long x,long y,char xp){
     for(int k=0;k<4;k++){
             for(int i=1;i<m;i++){
                     long X=x+dx[k]*i,Y=y+dy[k]*i;
                     if(c[X][Y]!=xp) break;
                     if(X<0||X>n||Y<0||Y>n) break;
                     if(i==m-1) return true;
             }
     }
     return false;
}

void change(){
     for(int i=1;i<=n;i++){
             long x=0;
             for(int j=n;j>=1;j--){
                     if(c[i][j]=='.'&&x==0) x=j;
                     if(c[i][j]!='.'&&x!=0){
                         c[i][x]=c[i][j];
                         c[i][j]='.';
                         x--;
                     }
             }
     }
     
}

void doit(){
     for(int i=1;i<=n;i++)
             for(int j=1;j<=n;j++){
                     if(c[i][j]!='.'){
                         if(red&&c[i][j]=='R') continue;
                         if(blue&&c[i][j]=='B') continue;
                         bool flag=search(i,j,c[i][j]);
                         if(flag&&c[i][j]=='R') red=true;
                         if(flag&&c[i][j]=='B') blue=true;
                     }
             }
}

void print(long t){
     cout<<"Case #"<<t<<": ";
     if(red&&blue) { cout<<"Both"<<endl; return; }
     if(red)       { cout<<"Red"<<endl;  return; }
     if(blue)      { cout<<"Blue"<<endl; return; }
     cout<<"Neither"<<endl;

}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long t;
    cin>>t;
    for(int i=1;i<=t;i++){
            init();
            doit();
            change();
            doit();
            print(i);
    }
    return 0;
}
