#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

char str[10][10];
int main()
{
   // freopen("Input.txt","r",stdin);
    //freopen("Output.txt","w",stdout);
    int T,k = 1;
    cin>>T;
    while(T--){
       for(int i = 0;i < 4;++i){
            cin>>str[i];
       }
       cout<<"Case #"<<k++<<": ";
       int countx = 0,counto = 0;
       bool flag = false;
       for(int j = 0;j < 4;++j){
            for(int i = 0;i < 4;++i){
                if(str[j][i] == 'O' || str[j][i] == 'T')
                counto++;
                if(str[j][i] == 'X' || str[j][i] == 'T')
                countx++;
                if(countx == 4){
                cout<<"X won"<<endl;
                flag = true;
                }
                if(counto == 4){
                cout<<"O won"<<endl;
                flag = true;
                }
                if(flag) break;
            }
            counto = countx = 0;
            if(flag) break;
       }
        countx = counto = 0;
        for(int i = 0;i < 4;++i){
            for(int j = 0;j < 4;++j){
                if(str[j][i] == 'O' || str[j][i] == 'T')
                counto++;
                if(str[j][i] == 'X' || str[j][i] == 'T')
                countx++;
                if(countx == 4){
                    cout<<"X won"<<endl;
                    flag = true;
                }
                if(counto == 4){
                    cout<<"O won"<<endl;
                    flag = true;
                }

            if(flag) break;
        }
         counto = countx = 0;
        if(flag) break;
       }
       countx = counto = 0;
       for(int i = 0;i < 4;++i){
        if(str[i][i] == 'T' || str[i][i] == 'O')
            counto++;
        if(str[i][i] == 'T' || str[i][i] == 'X')
            countx++;
       }
       if(countx == 4){
        cout<<"X won"<<endl;
        flag = true;
       }
       if(counto == 4){
        cout<<"O won"<<endl;
        flag = true;
       }
       countx = counto = 0;
       if(flag == false){
            for(int i = 0;i < 4;++i){
            if(str[i][3-i] == 'T' || str[i][3-i] == 'O')
                counto++;
            if(str[i][3-i] == 'T' || str[i][3-i] == 'X')
                countx++;
            }
            if(countx == 4){
                cout<<"X won"<<endl;
                flag = true;
            }
            if(counto == 4){
                cout<<"O won"<<endl;
                flag = true;
            }
       }
        if(!flag){
            for(int i = 0;i < 4;++i){
                for(int j = 0;j < 4;++j){
                    if(str[i][j] == '.'){
                        cout<<"Game has not completed"<<endl;
                        flag = true;
                        break;
                    }
                }
                if(flag) break;
            }
            if(!flag) cout<<"Draw"<<endl;
        }
    }
    return 0;
}
