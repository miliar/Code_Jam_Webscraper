#include <iostream>
#include <string>
#include <sstream>
#include <list>
using namespace std;
static const int MAX = 26;
static const int EMPTY = -1;
int toi(char c){
    return c - 'A';
}

void init( int eye[MAX]){
    for( int i=0; i < MAX; i++){
        eye[i] = 0;
    }
}
void init(int combine[MAX][MAX]){
    for( int i = 0; i < MAX; i++){
        for( int j=0; j < MAX; j++){
            combine[i][j] = EMPTY;
        }
    }
}
void init( list<int> opposed[MAX]){
    for( int i = 0; i < MAX;i++){
        opposed[i].clear();
    }
}
void processLine( string line, int test ){
    int combine[MAX][MAX];
    int eye[MAX]; // que letras aparecieron
    list<int> opposed [MAX];
    list<int> result;

    init(eye);
    init(combine);
    init(opposed);
    result.clear();
    std::istringstream stream(line);

    int C;
    stream >> C;
    for( int i = 0; i < C; i++){
        char c1,c2,c3;
        stream>>c1;
        stream>>c2;
        stream>>c3;
        combine[toi(c1)][toi(c2)]=toi(c3);
        combine[toi(c2)][toi(c1)]=toi(c3);
    }

    int D;
    stream >> D;
    for( int i = 0 ;  i < D; i++){
        char c1,c2;
        stream >>c1;
        stream >>c2;
        opposed[toi(c1)].push_back(toi(c2));
        opposed[toi(c2)].push_back(toi(c1));
    }

    int N;
    stream >> N;
    int prev = EMPTY;
    for( int i = 0; i < N; i++){
        char c;
        stream >>c;
        int x = toi(c);
        if( prev != EMPTY && combine[prev][x] != EMPTY){
            //intentar combinar
            eye[result.back()]--;
            result.pop_back();
            result.push_back(combine[prev][x]);
            prev = combine[prev][x];
        }else{
            //No se combina.. explotara?
            int clean = false;
            if( !result.empty() && !opposed[x].empty() ){
                list<int>::iterator it = opposed[x].begin();
                while( it != opposed[x].end()){
                    if( eye[*it] ){
                        //boom
                        clean = true;
                        break;
                    }
                    it++;
                }
            }
            if( clean ){
                prev = EMPTY;
                result.clear();
                init(eye);
            }else{
                //no se combina, no explota...
                eye[x]++;
                result.push_back(x);
                prev = x;
            }
        }
    }

    list<int>::iterator it = result.begin();
    cout << "Case #" << test << ": [";
    while( it != result.end()){
        if( it != result.begin()){
            cout << ", ";
        }
        char c = 'A' + *it;
        cout <<c;
        it++;
    }
    cout << "]"<< endl;
}

int main(int argc, char *argv[])
{

    int NTest;
    std::cin >> NTest;
    int test;
    std::string line;
    std::getline(std::cin, line);
    for ( test = 1 ; test <= NTest; test++){
        std::getline(std::cin, line);
        processLine(line, test);
    }


    return 1;
}
