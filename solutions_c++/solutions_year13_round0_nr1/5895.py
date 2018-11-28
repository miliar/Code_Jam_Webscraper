#include <iostream>
#include <string>
#include <vector>

using namespace std;

char checkRow(char *s1, char *s2, char *s3, char *s4){
    if( (s1[0] == 'X' || s1[0] == 'T') && 
	(s1[1] == 'X' || s1[1] == 'T') && 
	(s1[2] == 'X' || s1[2] == 'T') && 
	(s1[3] == 'X' || s1[3] == 'T')) return 'X';

    if( (s1[0] == 'O' || s1[0] == 'T') && 
	(s1[1] == 'O' || s1[1] == 'T') && 
	(s1[2] == 'O' || s1[2] == 'T') && 
	(s1[3] == 'O' || s1[3] == 'T')) return 'O';


    if( (s2[0] == 'X' || s2[0] == 'T') && 
	(s2[1] == 'X' || s2[1] == 'T') && 
	(s2[2] == 'X' || s2[2] == 'T') && 
	(s2[3] == 'X' || s2[3] == 'T')) return 'X';

    if( (s2[0] == 'O' || s2[0] == 'T') && 
	(s2[1] == 'O' || s2[1] == 'T') && 
	(s2[2] == 'O' || s2[2] == 'T') && 
	(s2[3] == 'O' || s2[3] == 'T')) return 'O';


    if( (s3[0] == 'X' || s3[0] == 'T') && 
	(s3[1] == 'X' || s3[1] == 'T') && 
	(s3[2] == 'X' || s3[2] == 'T') && 
	(s3[3] == 'X' || s3[3] == 'T')) return 'X';

    if( (s3[0] == 'O' || s3[0] == 'T') && 
	(s3[1] == 'O' || s3[1] == 'T') && 
	(s3[2] == 'O' || s3[2] == 'T') && 
	(s3[3] == 'O' || s3[3] == 'T')) return 'O';

    if( (s4[0] == 'X' || s4[0] == 'T') && 
	(s4[1] == 'X' || s4[1] == 'T') && 
	(s4[2] == 'X' || s4[2] == 'T') && 
	(s4[3] == 'X' || s4[3] == 'T')) return 'X';

    if( (s4[0] == 'O' || s4[0] == 'T') && 
	(s4[1] == 'O' || s4[1] == 'T') && 
	(s4[2] == 'O' || s4[2] == 'T') && 
	(s4[3] == 'O' || s4[3] == 'T')) return 'O';

    return 'N';
}


char checkCol(char *s1, char *s2, char *s3, char *s4){

    if( (s1[0] == 'X' || s1[0] == 'T') && 
	(s2[0] == 'X' || s2[0] == 'T') && 
	(s3[0] == 'X' || s3[0] == 'T') && 
	(s4[0] == 'X' || s4[0] == 'T')) return 'X';

    if( (s1[0] == 'O' || s1[0] == 'T') && 
	(s2[0] == 'O' || s2[0] == 'T') && 
	(s3[0] == 'O' || s3[0] == 'T') && 
	(s4[0] == 'O' || s4[0] == 'T')) return 'O';

    if( (s1[1] == 'X' || s1[1] == 'T') && 
	(s2[1] == 'X' || s2[1] == 'T') && 
	(s3[1] == 'X' || s3[1] == 'T') && 
	(s4[1] == 'X' || s4[1] == 'T')) return 'X';

    if( (s1[1] == 'O' || s1[1] == 'T') && 
	(s2[1] == 'O' || s2[1] == 'T') && 
	(s3[1] == 'O' || s3[1] == 'T') && 
	(s4[1] == 'O' || s4[1] == 'T')) return 'O';

    if( (s1[2] == 'X' || s1[2] == 'T') && 
	(s2[2] == 'X' || s2[2] == 'T') && 
	(s3[2] == 'X' || s3[2] == 'T') && 
	(s4[2] == 'X' || s4[2] == 'T')) return 'X';

    if( (s1[2] == 'O' || s1[2] == 'T') && 
	(s2[2] == 'O' || s2[2] == 'T') && 
	(s3[2] == 'O' || s3[2] == 'T') && 
	(s4[2] == 'O' || s4[2] == 'T')) return 'O';

    if( (s1[3] == 'X' || s1[3] == 'T') && 
	(s2[3] == 'X' || s2[3] == 'T') && 
	(s3[3] == 'X' || s3[3] == 'T') && 
	(s4[3] == 'X' || s4[3] == 'T')) return 'X';

    if( (s1[3] == 'O' || s1[3] == 'T') && 
	(s2[3] == 'O' || s2[3] == 'T') && 
	(s3[3] == 'O' || s3[3] == 'T') && 
	(s4[3] == 'O' || s4[3] == 'T')) return 'O';

    return 'N';
}


char checkX(char *s1, char *s2, char *s3, char *s4){

    if( (s1[0] == 'X' || s1[0] == 'T') && 
	(s2[1] == 'X' || s2[1] == 'T') && 
	(s3[2] == 'X' || s3[2] == 'T') && 
	(s4[3] == 'X' || s4[3] == 'T')) return 'X';

    if( (s1[0] == 'O' || s1[0] == 'T') && 
	(s2[1] == 'O' || s2[1] == 'T') && 
	(s3[2] == 'O' || s3[2] == 'T') && 
	(s4[3] == 'O' || s4[3] == 'T')) return 'O';

    
    if( (s1[3] == 'X' || s1[3] == 'T') && 
	(s2[2] == 'X' || s2[2] == 'T') && 
	(s3[1] == 'X' || s3[1] == 'T') && 
	(s4[0] == 'X' || s4[0] == 'T')) return 'X';

    if( (s1[3] == 'O' || s1[3] == 'T') && 
	(s2[2] == 'O' || s2[2] == 'T') && 
	(s3[1] == 'O' || s3[1] == 'T') && 
	(s4[0] == 'O' || s4[0] == 'T')) return 'O';

    return 'N';
}

bool count (char *s1, char *s2, char *s3, char *s4){
    for(int i = 0; i<=3; i++){
	if(s1[i] == '.') return true;
	if(s2[i] == '.') return true;
	if(s3[i] == '.') return true;
	if(s4[i] == '.') return true;
    }
    return false;
}

char check(char *s1, char *s2, char *s3, char *s4){
    char x;
    x = checkRow(s1, s2, s3, s4);
    if(x != 'N') return x;

    x = checkCol(s1, s2, s3, s4);
    if(x != 'N') return x;

    x = checkX(s1, s2, s3, s4);
    if(x != 'N') return x;

    if(count(s1,s2,s3,s4)) return 'I';
    else return 'D';
}
vector<char> v;
vector<char> runGame(){
    string s1, s2, s3, s4;
    cin >> s1;
    cin >> s2;
    cin >> s3;
    cin >> s4;

    int length = s1.length() + 1;
    char *str1 = new char[length];
    char *str2 = new char[length];
    char *str3 = new char[length];
    char *str4 = new char[length];

    strcpy(str1, s1.c_str());
    strcpy(str2, s2.c_str());
    strcpy(str3, s3.c_str());
    strcpy(str4, s4.c_str());

//    cout << str1[0] << endl;
//    cout << checkRow(str1, str2, str3, str4) << endl;
//    cout << checkCol(str1, str2, str3, str4) << endl;
//    cout << checkX(str1, str2, str3, str4) << endl;

//    cout << check(str1, str2, str3, str4) << endl;    
    char x = check(str1, str2, str3, str4);
    v.push_back(x);

    

    delete [] str1;
    delete [] str2;
    delete [] str3;
    delete [] str4;
}

int main(){
    int caseNumber;
    cin >> caseNumber;


    for(int i = 1; i<= caseNumber ; i++){
	runGame();
    }
    for(int i = 0; i< v.size() ; i++){
	string s;
	if (v[i] == 'X') s = "X won";
	if (v[i] == 'O') s = "O won";
	if (v[i] == 'D') s = "Draw";
	if (v[i] == 'I') s ="Game has not completed";
	cout << "Case #" << i+1 << ": " << s << endl;
    }
    

    return 0;
}
