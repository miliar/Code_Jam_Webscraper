#include <iostream>

using namespace std;

int main (){
    char tictac[4][4];
    int n,counter=0,MX[4][4],MO[4][4],WinX,WinO;
    cin>>n;
    while(counter<n){
        cin>>tictac[0]>>tictac[1]>>tictac[2]>>tictac[3];
        //cout<<tictac[1]<<endl;//<<tictac[1]<<endl<<tictac[2]<<endl<<tictac[3];

        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(tictac[i][j]=='X'){
                        MX[i][j]=1;
                        MO[i][j]=1;
                }
                if(tictac[i][j]=='O'){
                        MX[i][j]=2;
                        MO[i][j]=2;
                }
                if(tictac[i][j]=='T'){
                        MX[i][j]=1;
                        MO[i][j]=2;
                }
                if(tictac[i][j]=='.'){
                        MX[i][j]=0;
                        MO[i][j]=0;
                }
            }
        }
        WinX=WinO=0;
        // Verifica linha e coluna.
        for(int i=0;i<4;i++){
            if(MX[i][0]==1 && MX[i][1]==1 && MX[i][2]==1 && MX[i][3]==1) WinX=1; //Linha
            if(MX[0][i]==1 && MX[1][i]==1 && MX[2][i]==1 && MX[3][i]==1) WinX=1; //Coluna

            if(MO[i][0]==2 && MO[i][1]==2 && MO[i][2]==2 && MO[i][3]==2) WinO=2;
            if(MO[0][i]==2 && MO[1][i]==2 && MO[2][i]==2 && MO[3][i]==2) WinO=2; //Coluna
        }
            if(MX[0][0]==1 && MX[1][1]==1 && MX[2][2]==1 && MX[3][3]==1) WinX=1; //Diagonal 1
            if(MX[0][3]==1 && MX[1][2]==1 && MX[2][1]==1 && MX[3][0]==1) WinX=1; //Diagonal 2

            if(MO[0][0]==2 && MO[1][1]==2 && MO[2][2]==2 && MO[3][3]==2) WinO=2; //Diagonal 1
            if(MO[0][3]==2 && MO[1][2]==2 && MO[2][1]==2 && MO[3][0]==2) WinO=2; //Diagonal 2

            if(WinX==0 && WinO==0){
                for(int i=0;i<4;i++){
                    for(int j=0;j<4;j++){
                       if(MX[i][j]==0) WinX=-1;
                    }
                }
            }
            if(WinX==1 && WinO==0) cout<<"Case #"<<counter+1<<": X won"<<endl;
            if(WinX==0 && WinO==2) cout<<"Case #"<<counter+1<<": O won"<<endl;
            if(WinX==1 && WinO==2) cout<<"Case #"<<counter+1<<": Draw"<<endl;
            if(WinX==0 && WinO==0) cout<<"Case #"<<counter+1<<": Draw"<<endl;
            if(WinX==-1 && WinO==0) cout<<"Case #"<<counter+1<<": Game has not completed"<<endl;



        counter++;
    }


    return 0;
}
