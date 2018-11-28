#include <iostream>
#include <fstream>

#define cin fin
#define cout fout

using namespace std;

ifstream fin("input.in");
ofstream fout("output");

bool checkVertical(string* grid,char& player,bool& goon){
    bool found=true;
    char current='T';
    for(int i=0;i<4;i++){
        found=true;
        current ='N';
        for(int j=0;j<4;j++){
            if(grid[i][j]=='.'){
                goon=true;
                found=false;
                break;
            }
            if(grid[i][j]!='T')
                if(current=='N')
                    current=grid[i][j];
                else if(grid[i][j]!=current){
                    found=false;
                    break;
                }
        }
        if(found){
            player=current;
            return true;
        }
    }
    return false;
}

bool checkHorizontal(string* grid,char& player){
    bool found=true;
    char current='N';
    for(int j=0;j<4;j++){
        found=true;
        current ='N';
        for(int i=0;i<4;i++){
            if(grid[i][j]=='.'){
                found=false;
                break;
            }
            if(grid[i][j]!='T')
                if(current=='N')
                    current=grid[i][j];
                else if(grid[i][j]!=current){
                    found=false;
                    break;
                }
        }
        if(found){
            player=current;
            return true;
        }
    }
    return false;
}
bool checkD1(string* grid,char& player){
    bool found=true;
    char current='N';
    for(int i=0;i<4;i++){
        int j=i;
            if(grid[i][j]=='.'){
                found=false;
                break;
            }
            if(grid[i][j]!='T')
                if(current=='N')
                    current=grid[i][j];
                else if(grid[i][j]!=current){
                    found=false;
                    break;
                }
    }
        if(found){
            player=current;
            return true;
        }
    return false;
}
bool checkD2(string* grid,char& player){
    bool found=true;
    char current='N';
    for(int i=0;i<4;i++){
        int j=3-i;
            if(grid[i][j]=='.'){
                found=false;
                break;
            }
            if(grid[i][j]!='T')
                if(current=='N')
                    current=grid[i][j];
                else if(grid[i][j]!=current){
                    found=false;
                    break;
                }
    }
    if(found){
        player=current;
        return true;
    }
    return false;
}

int main()
{
    int T;
    string* grid=new string[4];
    cin >> T;
    for(int c=1;c<=T;c++){
        for(int i=0;i<4;i++)
        cin >> grid[i];
        char current;

        bool found,won=false,goon=false;
        found=checkVertical(grid,current,goon);

        if(found){
            cout << "Case #"<< c << ": "<<current <<" won" << endl;
            won=true;
        }else{
            found=checkHorizontal(grid,current);
            if(found){
                cout << "Case #"<< c << ": "<<current <<" won" << endl;
                won=true;
            }else{
                found=checkHorizontal(grid,current);
                if(found){
                    cout << "Case #"<< c << ": "<<current <<" won" << endl;
                    won=true;
                }else{
                    found=checkD1(grid,current);
                    if(found){
                        cout << "Case #"<< c << ": "<<current <<" won" << endl;
                        won=true;
                    }else{
                        found=checkD2(grid,current);
                        if(found){
                            cout << "Case #"<< c << ": "<<current <<" won" << endl;
                            won=true;
                        }
                    }

                }
            }
        }
        if(!goon && !won){
            cout << "Case #"<< c << ": Draw" << endl;
        }
        if(goon && !won){
            cout << "Case #"<< c << ": Game has not completed" << endl;
        }
    }
    return 0;
}
