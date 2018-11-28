#include<iostream>
#include<fstream>

using namespace std;
int main(){
     freopen("ag.in","r",stdin);
    freopen("ag.out","w",stdout);
        int testcases,t=0;
        cin>>testcases;
la:
        while(testcases--){

                t++;
                char ch[55][55];
                int row,col;
                cin>>row>>col;
                cout<<"Case #"<<t<<":"<<endl;
                for(int i=0;i<row;i++){
                                for(int j=0;j<col;j++){
                                        cin>>ch[i][j];
                                }
                }
                for(int i=0;i<row;i++){
                                for(int j=0;j<col;j++){
                                if((ch[i][j]=='#'&&ch[i][j+1]=='#'))
                                        if((ch[i+1][j]=='#'&&ch[i+1][j+1]=='#'))
                                                {ch[i][j]='/';ch[i][j+1]='\\';ch[i+1][j]='\\';ch[i+1][j+1]='/';}

                                }
                }
for(int i=0;i<row;i++){
                                for(int j=0;j<col;j++){
                                if(ch[i][j]=='#'){
                                        cout<<"Impossible"<<endl;
                                        goto la;}
                                }
}


                for(int i=0;i<row;i++){
                                for(int j=0;j<col;j++){
                                        cout<<ch[i][j];
                                }
                                cout<<endl;
                }
}
                return 0;
}
