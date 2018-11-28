#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstring>
using namespace std;
string t[51];
int dx[]={0,0,1,1};
int dy[]={0,1,0,1};
string s="/\\/";
int n,m,caso;
bool isValid(int x,int y){
    return x>=0 && x<n && y>=0 && y<m && t[x][y]=='#';
    }
bool f(){
    cin>>n>>m;
    int u,v;
    for(int i=0;i<n;i++)cin>>t[i];
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(t[i][j]=='#'){
                for(int k=0;k<4;k++){
                    u=i+dx[k];
                    v=j+dy[k];
                    if(isValid(u,v))t[u][v]=(k%3==0? '/':char(92));
                    else return false;
                    }
                }                        
            }
        }
    return true;
    }
void doit(){
    printf("Case #%d:\n",++caso);
    if(f())for(int i=0;i<n;i++)cout<<t[i]<<endl;
    else printf("Impossible\n");
    }
int main(){
    int C;
    caso=0;
    scanf("%d",&C);
    for(int i=0;i<C;i++)doit();
    }
