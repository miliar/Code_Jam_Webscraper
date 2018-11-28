#include <iostream>
#include <stack>

#define MAX 100

using namespace std;

void sink(int,int);

int map[MAX][MAX];
char  basins[MAX][MAX];
int H, W;
char curr;

stack< pair<int,int> > path;

int main(){
    int CASES,cases,i,j;
    cin >> CASES;
    cases = CASES;

    while(cases--){
        cin >> H >> W;
        
        for(i=0;i<H;++i){
            for(j=0;j<W;++j){
                cin >> map[i][j];
                basins[i][j] = 0;
            }
        }
                
        curr = 'a'-1;
        for(i=0;i<H;++i){
            for(j=0;j<W;++j){
                if(basins[i][j] == 0) sink(i,j);
            }
        }
            
        cout << "Case #" << CASES-cases << ":" << endl;
        curr = 'a'-1;
        for(i=0;i<H;++i){
            for(j=0;j<W;++j){
                cout << basins[i][j];
                if(j+1 < W) cout << " ";
            }
            cout << endl;
        }           
    }
    return 0;   
}

#define mff min.first.first
#define mfs min.first.second

void sink(int i, int j){
    pair<int,int> curp = make_pair(i,j);
    pair<pair<int,int>,char> min;
    while(true){
        path.push(make_pair(curp.first,curp.second));
        //cout << "curp = (" << curp.first << "," << curp.second << ") = " << map[curp.first][curp.second] << endl;
        //system("PAUSE");
        if(curp.first-1 >= 0 && curp.first-1 < H  && map[curp.first-1][curp.second] < map[curp.first][curp.second]) 
                     min = make_pair(make_pair(curp.first-1,curp.second),'n');        //NORTH
        else if(curp.second-1 >= 0 && curp.second-1 < W  && map[curp.first][curp.second-1] < map[curp.first][curp.second]) 
                           min = make_pair(make_pair(curp.first,curp.second-1),'w');   //WEST
        else if(curp.second+1 >= 0 && curp.second+1 < W  && map[curp.first][curp.second+1] < map[curp.first][curp.second]) 
                           min = make_pair(make_pair(curp.first,curp.second+1),'e');   //EAST
        else if(curp.first+1 >= 0 && curp.first+1 < H  && map[curp.first+1][curp.second] < map[curp.first][curp.second]) 
                          min = make_pair(make_pair(curp.first+1,curp.second),'s');   //SOUTH
        else break;
                          
        //cout << "min = (" << mff << "," << mfs << ")" << endl;
        switch(min.second){
        case 'n':
            // cout << "\tN" << endl;
             if(curp.second-1 >= 0 && curp.second-1 < W && map[curp.first][curp.second-1] < map[mff][mfs]) min = make_pair(make_pair(curp.first,curp.second-1),'w');
             //cout << "\t" << map[curp.first][curp.second-1] << "-" << map[mff][mfs] << endl;
        case 'w':
            // cout << "\tW" << endl;
             if(curp.second+1 >= 0 && curp.second+1 < W && map[curp.first][curp.second+1] < map[mff][mfs]) min = make_pair(make_pair(curp.first,curp.second+1),'e');
            // cout << "\t" << map[curp.first][curp.second+11] << "-" << map[mff][mfs] << endl;
        case 'e':
             //cout << "\tE" << endl;
             if(curp.first+1 >= 0 && curp.first+1 < H && map[curp.first+1][curp.second] < map[mff][mfs]) min = make_pair(make_pair(curp.first+1,curp.second),'s');
             //cout << "\t" << map[curp.first+1][curp.second] << "-" << map[mff][mfs] << endl;
        case 's':
             //cout << "\tS" << endl;
            curp = min.first;
            break;
        }
        
    }
    path.push(make_pair(curp.first,curp.second));
    char name;
    if(basins[curp.first][curp.second] != 0) name=basins[curp.first][curp.second];
    else name = ++curr;
    //cout << name << endl;
    while(!path.empty()){
        curp = path.top();
        path.pop();
        basins[curp.first][curp.second] = name;
    }
}
