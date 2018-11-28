#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;


class Board{
    public:
    Board(){};
    string lines[4];
    void addLine(string s, int i){
        lines[i] = s;
    }
    string getCol(int i){
        //cout << "getCol" << endl;
        //string col;
        char tab[4];
        for (int j = 0; j < 4; j++){
            tab[j] = lines[j].at(i);
            //col.append(c);
          //  cout << col << endl;
        }
        //cout << "za forem" << endl;
        //cout << col << endl;
        string col(tab);
        return col;
    }
    string getDiag(int i){
        //string diag;
        char tab[4];
        if(i == 0){
            for (int j = 0; j < 4; j++){
                tab[j] = lines[j].at(j);
                //diag.append(c);
            }
        }else{
            for (int j = 0; j < 4; j++){
                tab[j] = lines[j].at(3-j);
            }
        }
        string diag(tab);
        return diag;
    }
    void printBoard (){
        for (int i = 0; i < 4; i++) cout << lines[i] << endl;
    }
    void clearBoard(){
        for (int i = 0; i < 4; i++){
            lines[i].clear();
        }
    }
    int hasDot(){
        for (int i = 0; i < 4; i++){
        //cout << i << endl;
            for (int j = 0; j < 4; j++){
                if (lines[i].at(j)=='.') return 1;
            }
        }
        return 0;
    }


};
string checkBoard(Board b);
int checkLine(string l);
int main()
{
    vector <string> outputStr;
    int T = 0;
    ifstream inFile;
    ofstream outFile;
    stringstream ss;
    string line;
    Board inputBoard;
    //stringstream ss;
    int temp;
    double dtemp;
    string output;

    inFile.open("A-large.in");
    if(!inFile.is_open())
    {
        printf("Input file is invalid\n");
    }
    getline(inFile, line);
    //std::istringstream ss(line);
    ss << line;

    ss >> T;
    ss.clear();
    //T = (int)line.at(0)-48;
    for (int i = 0; i < T; i++){
        //cout << i << endl;
        for (int j = 0; j < 4; j++){
            //cout << j << endl;
            getline(inFile, line);
            inputBoard.addLine(line,j);
        }
        inputBoard.printBoard();
        string res;
        string resLine("Case #");
        stringstream s2;
        s2 << i+1;
        //ss.str();
        resLine.append(s2.str()).append(": ");
        s2.clear();
        res = checkBoard(inputBoard);
        resLine.append(res).append("\n");
        outputStr.push_back(resLine);
        cout << resLine;
        cout << endl << endl;
        getline(inFile, line);

    }
    inFile.close();
    fstream plik( "output.in", ios::out );

    for (int i = 0; i < T; i++){
        plik << outputStr.at(i);
    }
    plik.close();
    cout << T << endl;
    return 0;
}
string checkBoard(Board b){
    char first;
    string owon("O won");
    string xwon("X won");
    string notcom("Game has not completed");
    string draw("Draw");

    //rows
    int result = 0;
    cout << "rows" << endl;
    for(int i = 0; i < 4; i++){
        //cout << b.lines[i] << endl;
        result = checkLine(b.lines[i]);
        if (result == -1) return owon;
        else if (result == 1) return xwon;
        //else if (result == 2) return notcom;
    }

    //cols
    cout << "cols" << endl;
    for(int i = 0; i < 4; i++){
        //string col = b.getCol(i);
        //cout << col << endl;
        result = checkLine(b.getCol(i));
        if (result == -1) return owon;
        else if (result == 1) return xwon;
        //else if (result == 2) return notcom;
    }
    //diag
    cout << "diag" << endl;
    for(int i = 0; i < 2; i++){
        //cout << b.getDiag(i) << endl;
        result = checkLine(b.getDiag(i));
        if (result == -1) return owon;
        else if (result == 1) return xwon;
        //else if (result == 2) return notcom;
    }
    if (b.hasDot()==1) return notcom;
    return draw;
}
int checkLine(string l){
  //  cout << "check line" << endl;
  //  cout << l << endl;
   char first = l[0];
   if (first == 'T') first = l[1];
   int counter = 0;

   for (int i = 1; i <=3; i++){
       if (first ==  l[i] || l[i]== 'T' ) counter++;
   }
   if (counter == 3){
       if (first == 'X') return 1;
       else if (first == 'O') return -1;
   }
   return 0;
}
