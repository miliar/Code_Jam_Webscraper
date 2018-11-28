#include <iostream>
#include <algorithm>
#include <string>
#include <stdio.h>
using namespace std;
int main()
{
 freopen("src.txt","r",stdin); 
 freopen("out.txt","w",stdout);
 int n;
 cin >> n;
 string s[4];
 
 for(int j = 1;j<=n;j++)
 {
     bool won = false;
         bool nogame = false;
        for(int i = 0;i<4;i++)
                cin >> s[i];
                int counter5 = 0;
                int counter6 = 0;
        for(int i = 0;i<4;i++)
        {
                int counter1 = 0;
                int counter2 = 0;
                int counter3 = 0;
                int counter4 = 0;
                for(int j = 0;j<4;j++)
                {
                        if(i == j && (s[i][j] == 'X' ||s[i][j] == 'T'))
                                counter5++;
                        if(i == j && (s[i][j] == 'O'||s[i][j] == 'T'))
                                counter6++;
                        if(s[i][j] =='X' || s[i][j] =='T')
                                counter1++;
                        if(s[i][j] =='O' || s[i][j] =='T')
                                counter2++;
                        if(s[j][i] =='X' || s[j][i] =='T')
                                counter3++;
                        if(s[j][i] =='O' || s[j][i] =='T')
                                counter4++;
                        if(s[j][i] =='.')
                                nogame = true;
                }
                if((counter1 == 4 || counter3 == 4 || counter5 == 4) && !won)
                {
                        cout << "Case #"<<j<<": X won \n";
                        won = true;
                }
                else if((counter2 == 4 || counter4 == 4 ||  counter6 == 4 ) && !won){
                        cout << "Case #"<<j<<": O won \n";
                        won = true;}
        }
 
        int counter1 = 0,counter2 = 0;
        if(s[0][3] == 'X' || s[0][3] == 'T')
                counter1++;
        if(s[0][3] == 'O' || s[0][3] == 'T')
                counter2++;
        if(s[1][2] == 'X' || s[1][2] == 'T')
                counter1++;
        if(s[1][2] == 'O' || s[1][2] == 'T')
                counter2++;
        if(s[2][1] == 'X' || s[2][1] == 'T')
                counter1++;
        if(s[2][1] == 'O' || s[2][1] == 'T')
                counter2++;
        if(s[3][0] == 'X' || s[3][0] == 'T')
                counter1++;
        if(s[3][0] == 'O' || s[3][0] == 'T')
                counter2++;
 
        if(counter1 == 4 && !won)
         {
              cout << "Case #"<<j<<": X won \n";
              won = true;
         }
        else if(counter2 == 4 && !won){
        cout << "Case #"<<j<<": O won \n";
        won = true;}
 
         if(won == false && !nogame )
                 cout << "Case #"<<j<<": Draw \n";
        else if(won == false && nogame)
                cout << "Case #"<<j<<": Game has not completed \n";
 }
return 0;
}