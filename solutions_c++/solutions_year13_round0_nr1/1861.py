#include<vector>
#include<fstream>
#include<string>
#include<assert.h>
#include<utility>

using namespace std;

bool parseBoard(vector<vector<char> > &board, ifstream &infile){
    bool isFull = true;
    for(int i=0; i<4; ++i){
        vector<char> row;
        string s;
        infile >> s;
        assert(s.size()==4);
        for(int j=0; j<4; ++j){
            if(s[j]=='.')
                isFull = false;
            row.push_back(s[j]);
        }
        board.push_back(row);
    }
    return isFull;
}

char checkWin(const vector<char> &chars){
    char icon = '\0';
    for(int i=0; i<4; ++i){
        if(chars[i]=='.') return '\0';
        else if(chars[i]=='T') continue;
        else{
            if(icon == '\0') icon = chars[i];
            else if(icon != chars[i]) return '\0';
        }
    }
    assert(icon!='\0');
    return icon;
}

char scan_dia_right(vector<vector<char> > &board){
    vector<char> chars;
    int i=0, j=0;
    while(i<4 && j<4){
        chars.push_back(board[i++][j++]);
    }
    return checkWin(chars);
}

char scan_dia_left(vector<vector<char> > &board){
    vector<char> chars;
    int i=0, j=3;
    while(i<4 && j>=0){
        chars.push_back(board[i++][j--]);
    }
    return checkWin(chars);
}

char scan_down(vector<vector<char> > &board, int col){
    vector<char> chars;
    for(int i=0; i<4; ++i)
        chars.push_back(board[i][col]);
    return checkWin(chars);
}
char scan_right(vector<vector<char> > &board, int row){
    vector<char> chars;
    for(int j=0; j<4; ++j)
        chars.push_back(board[row][j]);
    return checkWin(chars);
}

pair<bool, char> solve(vector<vector<char> > &board){
    assert(board.size()==4 && board[0].size()==4);
    char res;
    // scan dia right
    res = scan_dia_right(board);
    if(res!='\0') return make_pair(true, res);
    // scan dia left
    res = scan_dia_left(board);
    if(res!='\0') return make_pair(true, res);
    //scan first row
    for(int j=0; j<4; ++j){
        res = scan_down(board, j);
        if(res!='\0') return make_pair(true, res);
    }
    // scan first col
    for(int i=0; i<4; ++i){
        res = scan_right(board, i);
        if(res!='\0') return make_pair(true, res);
    }
    return make_pair(false, '\0');
}

int main(){
    ifstream infile("A-large.in");
    ofstream outfile("A-large.out");
    //ifstream infile("A-small-attempt0.in");
    //ofstream outfile("A-small-attempt0.out");
    int N;
    infile >> N;
    vector<vector<char> > board;
    for(int i=0; i<N; ++i){
        bool isFull = parseBoard(board, infile);
        pair<bool, char> result = solve(board);
        outfile << "Case #" << i+1 << ": ";
        // Someone wins
        if(result.first == true){
            outfile << result.second << " won";
        }
        // nobody wins
        else{
            if(isFull)
                outfile << "Draw";
            else
                outfile << "Game has not completed";
        }
        outfile << endl;
        board.clear();
    }
    infile.close();
    outfile.close();
    return 0;
}
