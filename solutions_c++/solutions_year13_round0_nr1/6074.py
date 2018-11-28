#include<iostream>
#include<string>
#include<cstring>
#include<fstream>
using namespace std;

bool resCo(char dic[4][4], int j, char c){
    for(int i = 0; i < 4; ++i){
        if(dic[i][j] != c && dic[i][j] != 'T') return false;
    }
    return true;
}

bool resRo(char dic[4][4], int j, char c){
    for(int i = 0; i < 4; ++i){
        if(dic[j][i] != c && dic[j][i] != 'T') return false;
    }
    return true;
}

int result(char dic[4][4]){
    for(int i = 0; i < 4; ++i)
        if(resRo(dic, i, 'X') || resCo(dic, i, 'X'))    return 1;
        
    for(int i = 0; i < 4; ++i)
        if(resRo(dic, i, 'O') || resCo(dic, i, 'O'))    return 2;
        
    return 0;        
}

bool dia(char dic[4][4], char c){
    for(int i = 0; i < 4; ++i)
        if(dic[i][i] != c && dic[i][i] != 'T') return false;
return true;    
}

bool minDia(char dic[4][4], char c){
    for(int i = 0; i < 4; ++i)
        if(dic[i][3-i] != c && dic[i][3-i] != 'T') return false;
return true;    
}

bool checkDot(char dic[4][4]){
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; ++j)
            if(dic[i][j] == '.')    return true;
return false;            
}

int main() {
int t;    
char dic[4][4];
char c;

int Casesno = 0;
    ifstream fi("A-large.in");   
    ofstream fo("x.out"); 
    
    fi>>t;
    while(t--){
    memset(dic, '\0',sizeof(dic));
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; ++j){
                fi>>c;   
                dic[i][j] = c;
            }
   
        if(dia(dic,'X')) fo<<"Case #"<<++Casesno<<": "<<"X won"<<endl;
        else if(dia(dic,'O')) fo<<"Case #"<<++Casesno<<": "<<"O won"<<endl;
        
        else if(minDia(dic,'X')) fo<<"Case #"<<++Casesno<<": "<<"X won"<<endl;        
        else if(minDia(dic,'O')) fo<<"Case #"<<++Casesno<<": "<<"O won"<<endl;
        
        else if(result(dic) == 1)   fo<<"Case #"<<++Casesno<<": "<<"X won"<<endl;        
        else if(result(dic) == 2)   fo<<"Case #"<<++Casesno<<": "<<"O won"<<endl;        
        
        else if(checkDot(dic))   fo<<"Case #"<<++Casesno<<": "<<"Game has not completed"<<endl;        
        else    fo<<"Case #"<<++Casesno<<": "<<"Draw"<<endl;        
        
    }
return 0;
}
