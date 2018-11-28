#include <iostream>
#include <vector>
using namespace std;

const int MAX_C=40;
const int MAX_D=30;

string command;
vector<char> list;
int C,D;

int map[30];
char comp[8][8];
bool oppos[8][8];

void reset(){
    list.clear();
    command.clear();
    for (int i=0;i<8;i++)
        for (int j=0;j<8;j++)
        comp[i][j]=oppos[i][j]=0;
    cin >> C;
    for (int i=0;i<C;i++){
        char x,y,z; cin >> x >> y >> z; x-='A'; y-='A'; z-='A';
        comp[map[x]][map[y]]=comp[map[y]][map[x]]=z;
    }
    cin >> D;
    for (int i=0;i<D;i++){
        char x,y; cin >> x >> y; x-='A'; y-='A';
        oppos[map[x]][map[y]]=oppos[map[y]][map[x]]=1;
    }
    int temp; cin >> temp;
    cin >> command;
}

void proc(char x){
    
    x-='A';
    if (list.size() && map[list.back()]!=-1 && comp[map[list.back()]][map[x]]){
        
        list.back()=comp[map[list.back()]][map[x]];
        
        return;
    }
    for (int i=0;i<(int)list.size();i++)
        if (map[list[i]]!=-1 && oppos[map[list[i]]][map[x]]){
         
            list.clear();
            return;
        }
    
    list.push_back(x);
}


int Main(){
    for (int i=0;i<30;i++)
        map[i]=-1;
    map['Q'-'A']=0; map['W'-'A']=1; map['E'-'A']=2; map['R'-'A']=3; map['A'-'A']=4;
    map['S'-'A']=5; map['D'-'A']=6; map['F'-'A']=7;
    int T;
    cin >> T;
    for (int test=1;test<=T;test++){
        reset();
        for (int i=0;i<(int)command.length();i++){
            proc(command[i]);
        }
        cout << "Case #" << test << ": [";
        for (int i=0;i<(int)list.size();i++){
            if (i)
                cout << ", ";
            cout << char(list[i]+'A');
        }
        cout << "]\n";

    }
    return 0;
}

int main(){
    return Main();
}
