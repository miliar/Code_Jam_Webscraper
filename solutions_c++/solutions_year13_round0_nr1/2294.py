#include<iostream>
#include<cstring>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
using namespace std;
int main(){
    
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    
    int tc;
    cin>>tc;
    
    for(int caso=1;caso<=tc;caso++){
        vector<string>v(4,"");
        
        for(int i=0;i<4;i++)cin>>v[i];
        int win=-1;
        
        ////////////////
        for(int i=0;i<4;i++){
            int cont=0;
            for(int j=0;j<4;j++)
                if(v[i][j]=='X' || v[i][j]=='T')cont++;
            if(cont==4)win=1;
        }
        
        for(int i=0;i<4;i++){
            int cont=0;
            for(int j=0;j<4;j++)
                if(v[i][j]=='O' || v[i][j]=='T')cont++;
            if(cont==4)win=2;
        }
        /////////////////
        
        for(int i=0;i<4;i++){
            int cont=0;
            for(int j=0;j<4;j++)
                if(v[j][i]=='X' || v[j][i]=='T')cont++;
            if(cont==4)win=1;
        }
        
        for(int i=0;i<4;i++){
            int cont=0;
            for(int j=0;j<4;j++)
                if(v[j][i]=='O' || v[j][i]=='T')cont++;
            if(cont==4)win=2;
        }
        
        ///////////////
        
        int cont=0;
        for(int i=0;i<4;i++)
            if(v[i][i]=='O' || v[i][i]=='T')cont++;
            
        if(cont==4)win=2;
        
        cont=0;
        
        for(int i=0;i<4;i++)
            if(v[i][i]=='X' || v[i][i]=='T')cont++;
            
        if(cont==4)win=1;
        
        /////////////////
        cont=0;
        
        for(int i=0;i<4;i++)
            if(v[i][3-i]=='O' || v[i][3-i]=='T')cont++;
            
        if(cont==4)win=2;
        
        cont=0;
        
        for(int i=0;i<4;i++)
            if(v[i][3-i]=='X'|| v[i][3-i]=='T')cont++;
            
        if(cont==4)win=1;
        ////////////////////////
        
        cout<<"Case #"<<caso<<": ";
        if(win==1)
            cout<<"X won"<<endl;        
        
        if(win==2)
            cout<<"O won"<<endl;        
        
        if(win==-1){
            int puntito=-1;
            for(int i=0;i<4;i++)
                for(int j=0;j<4;j++)
                    if(v[i][j]=='.')
                        puntito=1;
                
            if(puntito==-1){
                cout<<"Draw"<<endl;    
            }else{
                cout<<"Game has not completed"<<endl;        
            }
        }
        
    }
    
    return 0;
}
