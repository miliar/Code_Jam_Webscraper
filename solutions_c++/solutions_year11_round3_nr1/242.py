#include<iostream>
#include<vector>
using namespace std;


char pic[100][100];

int h,w;
void color(int i,int j){
    const char* cs = "/\\\\/";
    int k = 0 ;
    for(int x=i;x<i+2;x++){
        for(int y=j;y<j+2;y++){
            if(pic[x][y]!='#')throw "foo";
            pic[x][y]=cs[k++];
        }
    }
}


int main(){

    int cases;
    cin>>cases;
    for(int cas=1;cas<=cases;cas++){
        cin>>h>>w;
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                char k = ' ';
                while(isspace(k))
                    cin>>k;
                pic[i][j]=k;
                //cout<<k<<" ";
            }
            //cout<<"\n";
        }
        cout<<"Case #"<<cas<<":\n";
        try{
            for(int i=0;i<h;i++){
                for(int j=0;j<w;j++){
                    if(pic[i][j]=='#')
                        color(i,j);
                }
            }
            for(int i=0;i<h;i++){
                for(int j=0;j<w;j++){
                    cout<<pic[i][j];
                }
                cout<<"\n";
            }
        }catch(const char* foo){
            cout<<"Impossible\n";
            
        }
    }

    return 0;
}
