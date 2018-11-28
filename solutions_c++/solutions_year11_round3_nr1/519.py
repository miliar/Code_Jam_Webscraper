#include<iostream>
#include<string>

using namespace std;

char mx[50][50];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc;
    string s;
    cin>>tc;
    for(int t=1;t<=tc;t++){
        int c,r;
        cin>>r>>c;
        for(int i=0;i<r;i++){
            cin>>s;
            for(int j=0;j<c;j++)
                mx[i][j]=s[j];
        }    
        bool is_possible=true;
        for(int i=0;i<r&&is_possible;i++)
            for(int j=0;j<c&&is_possible;j++)
                if(mx[i][j]=='#')
                    if(i+1<r&&j+1<c){
                        if(mx[i+1][j]=='#'&&mx[i][j+1]=='#'&&mx[i+1][j+1]=='#'){
                            mx[i][j]='/';
                            mx[i+1][j]='\\';
                            mx[i][j+1]='\\';
                            mx[i+1][j+1]='/';
                        }    
                        else
                            is_possible=false;
                    }
                    else
                        is_possible=false;
        printf("Case #%d:\n",t);
        if(is_possible)
            for(int i=0;i<r;i++,cout<<endl)
                for(int j=0;j<c;j++)
                    cout<<mx[i][j];
        else
            cout<<"Impossible"<<endl;
    }    
    return 0;
}    
