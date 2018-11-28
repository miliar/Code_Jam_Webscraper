#include<iostream>
using namespace std;

int main(){
    int t;
    int i,j,k,l;
    char a[4][4];
    int count;
    int count1,count2,count3,count4,count5;
    cin>>t;
    for (l=1; l<=t; l++){
            int flag = 0;
            count = 0;
            count1 = 0;
            for (i=0; i<4; i++){
                for (j=0; j<4; j++){
                    cin>>a[i][j];
                    if (a[i][j]=='.'){
                        flag = 1;
                    }
                    }
                }
        int f1 = 0;
        int f2 = 0;
        int f3 = 0;
        int f4 = 0;
        int f5 = 0;
        int f  = 0;
    for (i=0; i<4; i++){
        for (j=0; j<4; j++){

              //  int p = 0;
                //int q = 0;
                count2 = 0;
                for (k=0; k<4; k++){
       // count1 = 0;
        //count2 = 0;
        //count3 = 0;
        //count4 = 0;
       // count5 = 0;
       // count  = 0;
                    if (a[i][k]=='X' || a[i][k]=='T'){
                        count2++;
                        if (count2 ==4){
                            f2 = 1;
                        }
                        //p=1;
                    }
                }
        }
    }
                     for (i=0; i<4; i++){
                        for (j=0; j<4; j++){
                                count3 = 0;
                                 for (k=0; k<4; k++){
                    if (a[i][k]=='O' || a[i][k]=='T'){
                        count3++;
                        if (count3 == 4){
                            f3 = 1;
                        }
                        //p=1;
                    }
                        }
                     }
                     }
                      for (i=0; i<4; i++){
        for (j=0; j<4; j++){
                count4 = 0;
                 for (k=0; k<4; k++){
                    if (a[k][j]=='X' || a[k][j]=='T'){
                        count4++;
                        if (count4 == 4){
                            f4 = 1;
                        }
                        //q=1;
                    }
        }
                      }
                      }
                       for (i=0; i<4; i++){
        for (j=0; j<4; j++){
            count5 = 0;
                 for (k=0; k<4; k++){
                    if (a[k][j]=='O' || a[k][j]=='T'){
                        count5++;
                        if (count5 == 4){
                            f5 =1;
                        }
                       // q=1;
                    }
        }
                       }
                }
        for (i=0; i<4; i++){
            for (j=0; j<4; j++){
                if (i==j){
                     if (a[i][j]=='X' || a[i][j]=='T'){
                    count++;
                    if (count == 4){
                        f = 1;
                    }
                }
                if (a[i][j]=='O' || a[i][j]=='T'){
                    count1++;
                    if(count1 == 4){
                        f1 = 1;
                    }
                }
                }
            }
        }
        int count8 = 0;
        int count9 = 0;
        int f8 = 0, f9 = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 3; j >= 0; j--) {
                if (i+j == 3) {
                    if (a[i][j] == 'X' || a[i][j] == 'T') {
                                count8++;
                                if (count8 == 4) {
                                    f8 = 1;
                                }
                    }if(a[i][j] == 'O' || a[i][j] == 'T'){
                        count9++;
                        if (count9 == 4) {
                            f9 = 1;
                        }
                }
            }
        }
        }
    //    cout<<f<<" "<<f1<<" "<<f2<<" "<<f3<<" "<<f4<<" "<<f5<<endl;
        if (f == 1 || f2 == 1 || f4 == 1 || f8 == 1){
            cout<<"Case #"<<l<<": "<<"X won"<<endl;
        }
        else if (f1 == 1 || f3 == 1 || f5 == 1 || f9 == 1){
            cout<<"Case #"<<l<<": "<<"O won"<<endl;
        }
        else if (((f != 1 && f2 != 1 && f4 != 1 && f8 != 1) || (f1 != 1 && f3 != 1 && f5 != 1 && f9 != 1) )){
                if (flag == 1) {
                        cout<<"Case #"<<l<<": "<<"Game has not completed"<<endl;
                }else {
                    cout<<"Case #"<<l<<": "<<"Draw"<<endl;
                }
        }
    }
    }

