#include<iostream>
#include<math.h>
#include<algorithm>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
int main()
{
    ifstream istr;
    ofstream ef;
    ef.open("ans.txt");
    istr.open("1.txt");
    int t,i,j,k,test;
    bool flag;
    char arr[4][5];
    istr>>t;
    for(test=1;test<=t;test++){
                      flag=0;
                      ef<<"Case #"<<test<<": ";
            for(j=0;j<4;j++){
                             for(k=0;k<4;k++){
                                              istr>>arr[j][k];
                                              cout<<arr[j][k];
                              }
                              cout<<"\n";
            }
            for(i=0;i<4;i++){
                             if((arr[i][0]==arr[i][1] && arr[i][0]==arr[i][2] &&arr[i][0]==arr[i][3])||(arr[i][0]==arr[i][1]&&arr[i][0]==arr[i][2] && arr[i][3]=='T')||(arr[i][0]==arr[i][1]&& arr[i][0]==arr[i][3] && arr[i][2]=='T')||(arr[i][0]==arr[i][3]&& arr[i][0]==arr[i][2] && arr[i][1]=='T')||(arr[i][3]==arr[i][1]&&arr[i][3]==arr[i][2] && arr[i][0]=='T')){
                                                                                                               if(arr[i][0]=='T' &&arr[i][1]!='.'){
                                                                                                                                  ef<<arr[i][1]<<" won\n";
                                                                                                                                  flag=1;
                                                                                                                                  break;
                                                                                                               }
                                                                                                               else if(arr[i][0]!='.' && arr[i][1]!='.'){
                                                                                                                                  ef<<arr[i][0]<<" won\n";
                                                                                                               flag=1;
                                                                                                               break;
                                                                                                               }
                             }
                              if((arr[0][i]==arr[1][i]&&arr[0][i]==arr[2][i]&&arr[0][i]==arr[3][i])||(arr[0][i]==arr[1][i]&&arr[0][i]==arr[2][i] && arr[3][i]=='T')||(arr[0][i]==arr[1][i]&&arr[0][i]==arr[3][i] && arr[2][i]=='T')||(arr[0][i]==arr[3][i]&&arr[0][i]==arr[2][i] && arr[1][i]=='T')||(arr[3][i]==arr[1][i]&&arr[3][i]==arr[2][i] && arr[0][i]=='T')){
                                                                                                               if(arr[0][i]=='T' &&arr[1][i]!='.'){
                                                                                                                                  ef<<arr[1][i]<<" won\n";
                                                                                                                                  flag=1;
                                                                                                                                  break;
                                                                                                               }
                                                                                                               else if(arr[0][i]!='.' && arr[1][i]!='.'){
                                                                                                                                  ef<<arr[0][i]<<" won\n";
                                                                                                               flag=1;
                                                                                                               break;
                                                                                                               }
                             }
            }
            if(flag==0){
                         if((arr[0][0]==arr[1][1]&&arr[2][2]==arr[3][3]&&arr[0][0]==arr[2][2])||(arr[0][0]==arr[1][1]&&arr[0][0]==arr[2][2] && arr[3][3]=='T')||(arr[0][0]==arr[1][1]&&arr[0][0]==arr[3][3] && arr[2][2]=='T')||(arr[0][0]==arr[3][3]&&arr[0][0]==arr[2][2] && arr[1][1]=='T')||(arr[3][3]==arr[1][1]&&arr[3][3]==arr[2][2] && arr[0][0]=='T')){
                                                                                                               if(arr[0][0]=='T' && arr[1][1]!='.'){
                                                                                                                                  ef<<arr[1][1]<<" won\n";
                                                                                                                                  flag=1;
                                                                                                               }
                                                                                                               else if(arr[0][0]!='.' && arr[1][1]!='.'){
                                                                                                                                  ef<<arr[0][0]<<" won\n";
                                                                                                                                  flag=1;
                                                                                                               }
                             }
            }
            if(flag==0){
                              if((arr[0][3]==arr[1][2]&& arr[2][1]==arr[3][0]&&arr[0][3]==arr[3][0])||(arr[0][3]==arr[1][2]&&arr[1][2]==arr[2][1] && arr[3][0]=='T')||(arr[0][3]==arr[1][2]&&arr[1][2]==arr[3][0] && arr[2][1]=='T')||(arr[0][3]==arr[3][0]&&arr[3][0]==arr[2][1] && arr[1][2]=='T')||(arr[3][0]==arr[1][2]&&arr[3][0]==arr[2][1] && arr[0][3]=='T')){
                                                                                                               if(arr[0][3]=='T' && arr[1][2]!='.'){
                                                                                                                                  ef<<arr[1][2]<<" won\n";
                                                                                                                                  flag=1;
                                                                                                               }
                                                                                                               else if(arr[0][3]!='.' && arr[1][2]!='.'){
                                                                                                                                  ef<<arr[0][3]<<" won\n";
                                                                                                               flag=1;
                                                                                                               }
                             }
            }
            if(flag==0){
                        for(i=0;i<4;i++){
                                         for(j=0;j<4 && flag==0;j++){
                                                          if(arr[i][j]=='.'){
                                                                             ef<<"Game has not completed\n";
                                                                             flag=1;
                                                                             break;
                                                          }
                                         }
                        }
            }
            if(flag==0){
                        ef<<"Draw\n";
            }
    }
    istr.close();
    ef.close();
   system("pause");
   return 0;
}
