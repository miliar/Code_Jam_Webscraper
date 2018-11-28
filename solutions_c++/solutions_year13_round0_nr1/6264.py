#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int Tin, i, j, testcase;

    in>>Tin;

    for(testcase = 1 ; testcase <= Tin ; testcase++){
        int ans = -1;
        int X=-10, O=10, T=0;
        int temp[4][4]={0,};
        int check[10]={0,};
        int dot = 0;

        char arr[4][4]={0,};
        for(i = 0 ; i < 4 ; i++)
            for(j = 0 ; j < 4 ; j++)
                in>>arr[i][j];

        out<<"Case #"<<testcase<<": ";


        for(i = 0 ; i < 4 ; i++){
            for(j = 0 ; j < 4 ; j++){
                    if(arr[i][j] == 'X') temp[i][j] = -1;
                    else if(arr[i][j] == 'O') temp[i][j] = 1;
                    else if(arr[i][j] == 'T') temp[i][j] = 50;
                    else if(arr[i][j] == '.'){
                        temp[i][j] = 0;
                        dot++;
                    }
            }
        }

        check[0] = temp[0][0] + temp[0][1] + temp[0][2] + temp[0][3];
        check[1] = temp[1][0] + temp[1][1] + temp[1][2] + temp[1][3];
        check[2] = temp[2][0] + temp[2][1] + temp[2][2] + temp[2][3];
        check[3] = temp[3][0] + temp[3][1] + temp[3][2] + temp[3][3];
        check[4] = temp[0][0] + temp[1][0] + temp[2][0] + temp[3][0];
        check[5] = temp[0][1] + temp[1][1] + temp[2][1] + temp[3][1];
        check[6] = temp[0][2] + temp[1][2] + temp[2][2] + temp[3][2];
        check[7] = temp[0][3] + temp[1][3] + temp[2][3] + temp[3][3];
        check[8] = temp[0][0] + temp[1][1] + temp[2][2] + temp[3][3];
        check[9] = temp[0][3] + temp[1][2] + temp[2][1] + temp[3][0];

        for(i = 0 ; i < 10 ; i++){
            if(check[i] == 4 || check[i] == 53){
                ans = 0;
                break;
            }else if(check[i] == -4 || check[i] == 47){
                ans = 1;
                break;
            }else if(dot == 0) ans = 2;
        }

        if(dot != 0 && ans != 0 && ans != 1) ans = 3;

        if(ans == 0) out<<"O won"; //O is win
        else if(ans == 1) out<<"X won"; //X is win
        else if(ans == 2) out<<"Draw";
        else if(ans == 3) out<<"Game has not completed";

        out<<endl;
    }

    in.close();
    out.close();
    return 0;

}

