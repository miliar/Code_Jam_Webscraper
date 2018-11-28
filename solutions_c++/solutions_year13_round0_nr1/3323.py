#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
string s[4];
int checkwin(char ch){
    int i,j,flag;
    for (i = 0; i < 4; i++){
        flag = 1;
        for (j = 0; j < 4; j++) flag = flag&(s[i][j] == ch || s[i][j] == 'T');
        if (flag) return 1;
    }
    for (i = 0; i < 4; i++){
        flag = 1;
        for (j = 0; j < 4; j++) flag = flag&(s[j][i] == ch || s[j][i] == 'T');
        if (flag) return 1;
    }

    flag = 1;
    for (j = 0; j < 4; j++) flag = flag&(s[j][j] == ch || s[j][j] == 'T');
    if (flag) return 1;

    flag = 1;
    for (j = 0; j < 4; j++) flag = flag&(s[j][3-j] == ch || s[j][3-j] == 'T');
    if (flag) return 1;

    return 0;
}
int checktie(){
    int i,j;
    for (i = 0; i < 4; i++)
        for (j = 0; j < 4; j++)
            if (s[i][j] == '.') return 0;
    return 1;
}
int main()
{
   freopen("input2.txt","r",stdin);
   freopen("output2.txt","w",stdout);

    int T;
    cin>>T;
    for (int cas = 1; cas <=T; cas++){
        int i,j;
        for (i = 0; i < 4; i++) cin>>s[i];
        cout<<"Case #"<<cas<<": ";
        if (checkwin('X')){
            cout<<"X won"<<endl;
            continue;
        }
        if (checkwin('O')){
            cout<<"O won"<<endl;
            continue;
        }
        if (checktie()){
            cout<<"Draw"<<endl;
            continue;
        }
        cout<<"Game has not completed"<<endl;
    }
    return 0;
}

