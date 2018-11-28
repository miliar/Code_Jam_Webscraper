#include<iostream>
#include<vector>
#include<fstream>
#include<stdexcept>
#include<string>
using namespace std;
int who_won(string board);
string test_for(vector<string>board){
bool open_spaces=0;
for(int i =0;i<4;i++){
    for(int x=0;x<4;x++){
        if(board[i][x]=='.'){
            open_spaces =1;
        }
    }
}
vector<string>slices;
string temp = "";
//horizontal slices
for(int i =0;i<4;i++){
        temp ="";
    for(int j=0;j<4;j++){
            temp+= board[i][j];
    }
    slices.push_back(temp);
}
//vertical slices
for(int i =0;i<4;i++){
        temp="";
    for(int j=0;j<4;j++){
        temp+=board[j][i];
    }
    slices.push_back(temp);
}
//cross slices
temp="";
temp=temp+board[0][0]+board[1][1]+board[2][2]+board[3][3];
slices.push_back(temp);
//cout<<"TEMP SLICE 1: " << temp <<endl;
temp="";
temp=temp+board[0][3]+board[1][2]+board[2][1]+board[3][0];
//cout<<"TEMP SLICE 2: " <<temp <<endl;
slices.push_back(temp);
int win;
bool no_win;
for(int i =0;i<10;i++){
        win=who_won(slices[i]);
        cout<<slices[i]<<endl;
        if(win==1){
            cout<< "X won"<<endl;
            return "X won";
        }
        else if(win ==2){
                 cout<< "O won"<<endl;
            return "O won";
        }
        else {
             no_win =true;
        }

        }

    if(no_win && open_spaces){
        return "Game has not completed";
    }
    else
        return "Draw";
}



int who_won(string board){
int who_da_winner;// 1 = x, 2=O, 3=neither
if((board[0]=='X' || board[0] == 'T') &&
   (board[1]=='X' || board[1] == 'T') &&
   (board[2]=='X' || board[2] == 'T') &&
   (board[3]=='X' || board[3] == 'T')){
    who_da_winner =1;
}
else  if((board[0]=='O' || board[0] == 'T') &&
   (board[1]=='O' || board[1] == 'T') &&
   (board[2]=='O' || board[2] == 'T') &&
   (board[3]=='O' || board[3] == 'T')){
   who_da_winner = 2;
   }
else
{
    who_da_winner=3;
}
return who_da_winner;
}

int main(){
int n;
ifstream file;
try{
file.open("A-Large.in", ios::in);
//cout<<"file opened success!" <<endl;
}
catch(exception e){
cout<<e.what();
}
file>>n;

cout<<n<<endl;
vector<string> board;
/*={
    "OXOX",
    "XXOO",
    "XXXO",
    "OTXO"
}  ;
cout<<test_for(board)<<endl;
*/
string temp;
vector<string> cases;

for(int i =0;i<n;i++){//how many boards to input.
//cout<<"inputting boards"<<endl;
    board.clear();
    for(int x =0;x<4;x++){

       file>>temp;
       board.push_back(temp);
      // cout<<temp<<endl;
    }

    cases.push_back(test_for(board));
}
file.close();
try
{
    ofstream outputfile ("A-Large-Out.txt", ios::out);
    for(int i=0;i<n;i++)
        {
            outputfile<<"Case #"<<(i+1)<<": " <<cases[i]<<endl;
            cout<<"Case #"<<(i+1)<<": " <<cases[i]<<endl;
        }
    outputfile.close();
}catch(domain_error e)
    {
        cout<<e.what();
    }


return 0;
}
