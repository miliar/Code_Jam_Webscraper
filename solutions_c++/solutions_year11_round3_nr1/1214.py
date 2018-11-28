#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("FLARGE.txt","w",stdout);
int T,R,C;
scanf("%d",&T);
for(int I=1;I<=T;I++){
scanf("%d%d",&R,&C);
char inp[R][C+1];
for(int i=0;i<R;i++) scanf("%s",inp[i]);
bool con=true;
for(int i=0;i<R-1 && con;i++){
for(int j=0;j<C-1 && con;j++){
if(inp[i][j]=='#'){
if(inp[i+1][j]!='#' || inp[i+1][j+1]!='#' || inp[i][j+1]!='#') con=false;
else{
inp[i][j]='/';
inp[i+1][j]='\\';
inp[i+1][j+1]='/';
inp[i][j+1]='\\';
}
}
}
}
for(int i=0;i<R;i++) if(inp[i][C-1]=='#') con=false;
for(int i=0;i<C;i++) if(inp[R-1][i]=='#') con=false;
printf("Case #%d:\n",I);
if(!con) printf("Impossible\n");
else{
for(int i=0;i<R;i++) printf("%s\n",inp[i]);
}
}
return 0;
}
