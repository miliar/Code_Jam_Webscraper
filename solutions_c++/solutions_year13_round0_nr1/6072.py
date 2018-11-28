#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
using namespace std;

bool diagonally(char tab[4][4], char ch){
    for(int i = 0; i < 4; ++i)
        if(tab[i][i] != ch && tab[i][i] != 'T') return false;
return true;    
}

bool subDiagonally(char tab[4][4], char ch){
    for(int i = 0; i < 4; ++i)
        if(tab[i][3-i] != ch && tab[i][3-i] != 'T') return false;
return true;    
}

bool checkCol(char tab[4][4], int j, char ch){
    for(int i = 0; i < 4; ++i){
        if(tab[i][j] != ch && tab[i][j] != 'T') return false;
    }
    return true;
}

bool checkRow(char tab[4][4], int j, char ch){
    for(int i = 0; i < 4; ++i){
        if(tab[j][i] != ch && tab[j][i] != 'T') return false;
    }
    return true;
}

int checkDiagonally(char tab[4][4]){
    for(int i = 0; i < 4; ++i)
        if(checkRow(tab, i, 'X') || checkCol(tab, i, 'X'))    return 1;
        
    for(int i = 0; i < 4; ++i)
        if(checkRow(tab, i, 'O') || checkCol(tab, i, 'O'))    return 2;
        
    return 0;        
}

bool checkDot(char tab[4][4]){
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; ++j)
            if(tab[i][j] == '.')    return true;
return false;            
}
void show(char tab[4][4]){
for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; ++j){
//                fin>>ch;   
                cout<<tab[i][j];
            }
    cout<<endl;}
}
int main() {
int T;    
char tab[4][4];
char ch;
char space;
int cases = 0;
    ifstream fin("A-large.in");   //input file
    ofstream fout("1.out");     //output file
    
    fin>>T;
    while(T--){
    memset(tab, '\0',sizeof(tab));
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; ++j){
                fin>>ch;   
                tab[i][j] = ch;
            }
//         fin>>space;
         //cout<<endl<<cases<<endl;
         //show(tab);   
        //diagonally    
        if(diagonally(tab,'X')) fout<<"Case #"<<++cases<<": "<<"X won"<<endl;
        else if(diagonally(tab,'O')) fout<<"Case #"<<++cases<<": "<<"O won"<<endl;
        
        //sub-diagonally
        else if(subDiagonally(tab,'X')) fout<<"Case #"<<++cases<<": "<<"X won"<<endl;        
        else if(subDiagonally(tab,'O')) fout<<"Case #"<<++cases<<": "<<"O won"<<endl;
        
        else if(checkDiagonally(tab) == 1)   fout<<"Case #"<<++cases<<": "<<"X won"<<endl;        
        else if(checkDiagonally(tab) == 2)   fout<<"Case #"<<++cases<<": "<<"O won"<<endl;        
        
        else if(checkDot(tab))   fout<<"Case #"<<++cases<<": "<<"Game has not completed"<<endl;        
        else    fout<<"Case #"<<++cases<<": "<<"Draw"<<endl;        
        
    }
return 0;
}
