#include <iostream>
#include <vector>
using namespace std;

typedef vector<char> VC;
typedef vector<VC> VVC;

int main(){
    int num;
    cin>>num;
    for(int cas=1;cas<=num;++cas){
        cout<<"Case #"<<cas<<": ";
    int n,k;
    cin>>n>>k;
    VVC map(n,VC(n));
    for(int i=0;i<n;++i)
        for(int j=0;j<n;++j)
            cin>>map[i][j];
    for(int i=0;i<n;++i)
        for(int j=n-1;j>=0;--j){
            if(map[i][j]!='.'){
               int move = j;
               while(move+1<n and map[i][move+1]=='.')++move;
               if(move!=j){
                   map[i][move]=map[i][j];
                   map[i][j]='.';
               }
            }
        }
    
    bool b=0,r=0;
    int cont;
    for(int i=0;i<n and cont<k;++i){
        cont =0;
        for(int j=0;j<n and cont<k;++j){
            if(map[i][j]!='B')cont=0;
            else ++cont;
        }
    }
    if(cont==k)b=true;
    cont=0;
    for(int i=0;i<n and cont<k;++i){
        cont =0;
        for(int j=0;j<n and cont<k;++j){
            if(map[i][j]!='R')cont=0;
            else ++cont;
        }
    }
    if(cont==k){r=true;}
    cont=0;
    for(int i=0;i<n and cont<k;++i){
        cont =0;
        for(int j=0;j<n and cont<k;++j){
            if(map[j][i]!='B')cont=0;
            else ++cont;
        }
    }
    if(cont==k)b=true;
    cont=0;
    for(int i=0;i<n and cont<k;++i){
        cont =0;
        for(int j=0;j<n and cont<k;++j){
            if(map[j][i]!='R')cont=0;
            else ++cont;
        }
    }
    if(cont==k){r=true;}
    cont=0;
    for(int i=-n+1;i<n and cont<k;++i){
        cont =0;
        int m= max(0,-i);
        for(int j=m;j<n and i+j<n and cont<k;++j){
            if(map[j][i+j]!='B')cont=0;
            else ++cont;
        }
    }
    if(cont==k)b=true;
    cont=0;
    
    for(int i=-n+1;i<n and cont<k;++i){
        cont =0;
        int m=max(0,-i);
        for(int j=m;j<n and i+j<n and cont<k;++j){
            if(map[j][i+j]!='R')cont=0;
            else ++cont;
        }
    }
    if(cont==k)r=true;
    cont=0;
    
    for(int i=0;i<2*n and cont<k;++i){
        cont =0;
        int m=max(0,i-n+1);
        for(int j=m;j<n and i-j>=0 and cont<k;++j){
            if(map[j][i-j]!='B')cont=0;
            else ++cont;
        }
    }
    if(cont==k)b=true;
    cont=0;
    for(int i=0;i<2*n and cont<k;++i){
        cont =0;
        int m=max(0,i-n+1);
        for(int j=m;j<n and i-j>=0 and cont<k;++j){
            if(map[j][i-j]!='R')cont=0;
            else ++cont;
        }
    }
    if(cont==k)r=true;
    cont=0;
            
    if(!b and !r)cout<<"Neither"<<endl;
    else if(b and !r)cout<<"Blue"<<endl;
    else if(r and !b)cout<<"Red"<<endl;
    else if(r and b)cout<<"Both"<<endl;
    }
            
}
