#include <iostream>
#include <string>
using namespace std;

string s;

int accept(char a, int i, int stride){
    for (int j=0; j<4; j++,i+=stride)
        if (s[i]!=a && s[i]!='T') return 0;
    return 1;
}

int main(){
    int t,u,i,j;
    string str;
    cin>>t;
    int loc[][10]={
        {0,4,8,12,0,1,2,3,0,3},
        {1,1,1, 1,4,4,4,4,5,3}
    };
    for (u=0; u<t; u++){
        cout<<"Case #"<<(u+1)<<": ";
        s="";
        for (i=0; i<4; i++){ cin>>str; s+=str; }
        for (i=0; i<10; i++) if(accept('X',loc[0][i],loc[1][i])) break; 
        if (i<10){ cout<<"X won"<<endl; continue; }
        for (i=0; i<10; i++) if(accept('O',loc[0][i],loc[1][i])) break; 
        if (i<10){ cout<<"O won"<<endl; continue; }
        if (s.find('.')!=string::npos){ cout<<"Game has not completed"<<endl; continue; }
        cout<<"Draw"<<endl;
    }
    return 0;
}
        
