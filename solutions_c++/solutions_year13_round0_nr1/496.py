#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int N;
    char B[16];
    string S;
    
    cin >> N;
    for (int n=0; n<N;n++){
    getline (cin,S);
    for (int j=0; j<4; j++) {
    for (int i=0; i< 4;i++) cin >> B[j*4+i];   
    getline (cin,S);
    }
    
    int O=0,X=0;
    int completed =0;
    int T=0;
    
    for (int a=0; a<4; a++) {
        O=0;X=0;
        for (int b=0; b<4 ; b++) {
            if ((B[a*4+b] == 'X') || (B[a*4+b] == 'T')){ X ++;}
            if ((B[a*4+b] == 'O') || (B[a*4+b] == 'T')) {O ++;}
        }
        if (O ==4) {
              cout << "Case #" << (n+1) << ": O won" << endl;
              a = 4;
              completed=1;
        }
        if (X ==4) {
              cout << "Case #" << (n+1) << ": X won" << endl;
              a = 4;
              completed=1;
        }
    
    }

    if (completed==0) {
    for (int a=0; a<4; a++) {
        O=0;X=0;
        for (int b=0; b<4 ; b++) {
            if ((B[a+b*4] == 'X') || (B[a+b*4] == 'T')) {X ++;}
            if ((B[a+b*4] == 'O') || (B[a+b*4] == 'T')) {O ++;}
            if ((B[a+b*4] == 'O') || (B[a+b*4] == 'X') || (B[a+b*4] == 'T')) {T ++;}
        }
        if (O ==4) {
              cout << "Case #" << (n+1) << ": O won" << endl;
              a = 4;
              completed=1;
        }
        if (X ==4) {
              cout << "Case #" << (n+1) << ": X won" << endl;
              a = 4;
              completed=1;
        }
    
    }
    }

    if (completed==0) {
    O=0;X=0;
    for (int a=0; a<4; a++) {
        if ((B[a+a*4] == 'X') || (B[a+a*4] == 'T')) X ++;
        if ((B[a+a*4] == 'O') || (B[a+a*4] == 'T')) O ++;
        if (O ==4) {
              cout << "Case #" << (n+1) << ": O won" << endl;
              a = 4;
              completed=1;
        }
        if (X ==4) {
              cout << "Case #" << (n+1) << ": X won" << endl;
              a = 4;
              completed=1;
        }
    }    
    }

    if (completed==0) {
    O=0;X=0;
    for (int a=0; a<4; a++) {
        if ((B[(3-a)+a*4] == 'X') || (B[(3-a)+a*4] == 'T')) X ++;
        if ((B[(3-a)+a*4] == 'O') || (B[(3-a)+a*4] == 'T')) O ++;
        if (O ==4) {
              cout << "Case #" << (n+1) << ": O won" << endl;
              a = 4;
              completed=1;
        }
        if (X ==4) {
              cout << "Case #" << (n+1) << ": X won" << endl;
              a = 4;
              completed=1;
        }
    }
    }

    if (completed==0){
                      if (T == 16)    cout << "Case #" << (n+1) << ": Draw" << endl;
                      else    cout << "Case #" << (n+1) << ": Game has not completed" << endl;
                       }
                       
    }
    
    return EXIT_SUCCESS;
}
