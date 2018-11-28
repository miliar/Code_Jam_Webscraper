#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<sstream>
#include<map>
#include<set>

using namespace std;

char game[4][8];

bool check(char w){
    for(int i=0;i<4;i++){
        bool win=true;

        for(int j=0;j<4;j++){
            if(game[i][j]!=w && game[i][j]!='T'){
                win=false;break;
            }
        }

        if(win) return true;
    }

    for(int i=0;i<4;i++){
        bool win=true;

        for(int j=0;j<4;j++){
            if(game[j][i]!=w && game[j][i]!='T'){
                win=false;break;
            }
        }

        if(win) return true;
    }

    bool win=true;
    for(int k=0;k<4;k++)
        if(game[k][k]!=w && game[k][k]!='T'){
            win=false;break;
        }

    if(win) return true;

    win=true;
    for(int k=0;k<4;k++)
        if(game[3-k][k]!=w && game[3-k][k]!='T'){
            win=false;break;
        }

    return win;
}


int main(int argc, char* argv[])
{
    if(argc != 2){
        cout<<argv[0]<<" input_file"<<endl;
        return 0;
    }

    fstream file(argv[1]);

    char line[64];
    file.getline(line, 64);

    int T = atoi(line);

    for(int t=0;t<T;t++){
        memset(game, 0x0, sizeof(game));

        file.getline(line, 64);
        strncpy(game[0], line, 4);
        file.getline(line, 64);
        strncpy(game[1], line, 4);
        file.getline(line, 64);
        strncpy(game[2], line, 4);
        file.getline(line, 64);
        strncpy(game[3], line, 4);
        file.getline(line, 64);
#if 0
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++)
                cout<<game[i][j];
            cout<<endl;
        }
#endif

        //check 'X win'
        if(check('X')){
            cout<<"Case #"<<t+1<<": "<<"X won"<<endl;
            continue;
        }

        //check 'O win'
        if(check('O')){
            cout<<"Case #"<<t+1<<": "<<"O won"<<endl;
            continue;
        }


        //check 'complete'
        bool finish = true;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(game[i][j]=='.'){
                    finish=false;break;
                }

        if(!finish){
            cout<<"Case #"<<t+1<<": "<<"Game has not completed"<<endl;
            continue;
        }


        cout<<"Case #"<<t+1<<": "<<"Draw"<<endl;
    }

}
