#include <iostream>
#include <vector>
#include <set>
using namespace std;

set<char> winner;
set<pair<int,int> > X,O,dot;

void checkCol(int col){
    int counter=0;
    for(int i=0; i<4; ++i){
	if(X.find(make_pair(col,i))!=X.end())
	    counter++;
    }
    if(counter==4) winner.insert('X');
    counter = 0;
    for(int i=0; i<4; ++i){
	if(O.find(make_pair(col,i))!=O.end())
	    counter++;
    }
    if(counter==4) winner.insert('O');
}

void checkRow(int row){
    int counter=0;
    for(int i=0; i<4; ++i){
	if(X.find(make_pair(i,row))!=X.end())
	    counter++;
    }
    if(counter==4) winner.insert('X');
    counter = 0;
    for(int i=0; i<4; ++i){
	if(O.find(make_pair(i,row))!=O.end())
	    counter++;
    }
    if(counter==4) winner.insert('O');
}

void checkDia(void){
    int counter =0;
    for(int i=0; i<4; ++i){
	if(X.find(make_pair(i,i))!=X.end())
	    counter++;
    }
    if(counter==4) winner.insert('X');
    counter = 0;
    for(int i=0; i<4; ++i){
	if(O.find(make_pair(i,i))!=O.end())
	    counter++;
    }
    if(counter==4) winner.insert('O');
    counter = 0;
    for(int i=0; i<4; ++i){
	if(X.find(make_pair(i,3-i))!=X.end())
	    counter++;
    }
    if(counter==4) winner.insert('X');
    counter = 0;
    for(int i=0; i<4; ++i){
	if(O.find(make_pair(i,3-i))!=O.end())
	    counter++;
    }
    if(counter==4) winner.insert('O');
}


int main(void){
    int N;
    char board[4][4];

    cin >> N;
    for(int i=0; i<N; ++i){
	for(int j=0; j<4; ++j){
	    for(int k=0; k<4; ++k){
		cin >> board[j][k];
		if(board[j][k]=='X')
		    X.insert(make_pair(j,k));
		else if(board[j][k]=='O')
		    O.insert(make_pair(j,k));
		else if(board[j][k]=='T'){
		    X.insert(make_pair(j,k));
		    O.insert(make_pair(j,k));
		}
		else
		    dot.insert(make_pair(j,k));
	    }
	}
	for(int j=0; j<4; ++j){
	    checkCol(j);
	    checkRow(j);
	}
	checkDia();
	cout << "Case #" << i+1 << ": ";
	if(winner.empty() && dot.size() > 0) cout << "Game has not completed" << endl;
	else if(winner.size()==2 || (winner.empty() && dot.empty())) cout << "Draw" << endl;
	else if(winner.size()==1 && *winner.begin()=='X')
	    cout << "X won" << endl;
	else if(winner.size()==1 && *winner.begin()=='O')
	    cout << "O won" << endl;
    
        X.clear(); O.clear(); dot.clear();
	winner.clear();
    }
}

	
       
