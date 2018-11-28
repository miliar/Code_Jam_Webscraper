#include <iostream>
#include<conio.h>
#include<stdio.h>

using namespace std;

int main()
{

    freopen("C:/stream/A-large.in", "r", stdin);
	freopen("C:/stream/Out.txt", "w+", stdout);

    int testi[1000], board[4][4];
    char x[4];

    cin>>testi[0];

    int T = testi[0];

    for(int m = 0; m < T; m++){

        for(int j=0; j<4;j++){

           // cout<<T<<"\n INSIDE INSIDE before \n";

            cin>>x;
           // cout<<x<<endl;
            // cout<<T<<"\n INSIDE INSIDE \n";

            for(int k=0; k<4;k++){

               // cout<<x[k]<<" ";
                if(x[k] == 'X'){

                    board[j][k] = 2;

                    }
                else if(x[k] == 'O'){

                    board[j][k] = 1;

                    }

                else if(x[k] == 'T'){

                    board[j][k] = -1;

                    }
                else if(x[k] == '.'){

                    board[j][k] = 0;

                    }



                }



            }

        //  cout<<endl<<test<<" ENTER 2"<<endl;

       // cin>>x;

        int temp1 = 0;
        int temp2 = 0;
        int flag = 0;
        int possible[4];

        for(int i=0; i<4; i++){

            temp1 = board[i][0]*board[i][1]*board[i][2]*board[i][3];
            temp2 = board[0][i]*board[1][i]*board[2][i]*board[3][i];

            possible[i] = temp1;

            //cout<<board[i][0]<<" "<<board[i][1]<<" "<<board[i][2]<<" "<<board[i][3]<<endl;

            if(temp1 == 0 && temp2 == 0){

                continue;
            }
            else if(temp1 == -1 || temp1 == 1 || temp2 == -1 || temp2 == 1){

                testi[m]=0;
                flag = 1;
                break;

            }
            else if(temp1 == 16 || temp1 == -8 || temp2 == -8 || temp2 == 16){

                testi[m]=1;
                flag = 1;
                break;

            }

            }

        temp1 = board[0][0]*board[1][1]*board[2][2]*board[3][3];
        temp2 = board[0][3]*board[1][2]*board[2][1]*board[3][0];

        if(!flag){
            if(temp1 == 16 || temp1 == -8 || temp2 == -8 || temp2 == 16){

                testi[m]=1;;
                flag = 1;

                }
            else if(temp1 == -1 || temp1 == 1 || temp2 == -1 || temp2 == 1){

                testi[m]=0;
                flag = 1;

                }
        }


        if(!flag){

            int over = possible[0]*possible[1]*possible[2]*possible[3];
            if(!over){
                testi[m] = 2;
            }
            else testi[m] = 3;

            }


        }



for(int m=0; m< T; m++){

    switch(testi[m]){

    case 0: cout<<"Case #"<<m+1<<": O won"<<endl;
    break;
    case 1: cout<<"Case #"<<m+1<<": X won"<<endl;
    break;
    case 2: cout<<"Case #"<<m+1<<": Game has not completed"<<endl;
    break;
    case 3: cout<<"Case #"<<m+1<<": Draw"<<endl;
    break;

        }
    }

}
