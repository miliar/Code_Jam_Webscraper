#include<iostream>
using namespace std;
bool rows(char arr[4][4],char user){
    int count = 0;
    for(int i = 0 ; i < 4 ; i++){
        count = 0;
        for(int j = 0 ; j < 4 ; j++){
            if (arr[i][j]==user || arr[i][j]=='T'){
               count++; 
            }
        }
        if (count == 4) return true;
    }
    return false;
}
bool columns(char arr[4][4],char user){
    int count = 0;
    for(int i = 0 ; i < 4 ; i++){
        count = 0;
        for(int j = 0 ; j < 4 ; j++){
            if (arr[j][i]==user || arr[j][i]=='T'){
               count++;
            }
        }
        if (count == 4) return true;
    }
    return false;
}
bool diaganol(char arr[4][4],char user){
    int count = 0;
    for(int i = 0, j = 0 ; i < 4 ; i++,j++){
        if (arr[i][j]==user || arr[i][j]=='T'){
            count++;
        }
    }
    if (count == 4) return true;
    count = 0;
    for(int i = 3, j = 0 ; i >=0 ; i--,j++){
        if (arr[i][j]==user || arr[i][j]=='T'){
            count++;
        }
    }
    if (count == 4) return true;
    return false;
}
bool check(char arr[4][4],int i,int j,char user){
    if(rows(arr,user)) return true;
    if(columns(arr,user)) return true;
    if(diaganol(arr,user)) return true;
    return false;
}
bool check_draw(char arr[4][4]){
    for(int i = 0 ; i < 4 ; i++){
        for(int j = 0 ; j < 4 ; j++){
            if(arr[i][j]=='.') return false;
        }
    }
    return true;
}
int main(){
    freopen ("A-large.in","r",stdin);
    freopen ("output_large.txt","w",stdout);
    int T;
    cin>>T;
    for(int k = 0 ; k < T ; k++){
        char arr[4][4];
        bool x_won = false;
        bool o_won = false;
        bool draw = false;
        bool not_completed = false;
        for(int i = 0 ; i < 4 ; i++){
            for(int j = 0 ; j < 4 ; j++){
                cin>>arr[i][j];
            }
        }
        for(int i = 0 ; i < 4 ; i++){
            for(int j = 0 ; j < 4 ; j++){
                x_won = check(arr,i,j,'X');
                if (x_won){
                    cout<<"Case #"<<k+1<<": X won"<<endl;
                    i = 5;
                    break;
                }
                o_won = check(arr,i,j,'O');
                if (o_won){
                    cout<<"Case #"<<k+1<<": O won"<<endl;
                    i = 5;
                    break;
                }
            }
        }
        if (!x_won && !o_won){
            draw = check_draw(arr);
            if (draw) cout<<"Case #"<<k+1<<": Draw"<<endl;
            else cout<<"Case #"<<k+1<<": Game has not completed"<<endl;
        }
    }
return 0;    
}
