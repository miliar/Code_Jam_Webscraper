#include <iostream>
#include <set>
#include <cstdio>
using namespace std;

struct node{

    string cecha;
    
    double waga;
    
    int prawda, falsz;

};

node T[200];
int L;

int licznik = 0;

bool isLetter(char a){
    if (a >= 'a' && a <= 'z') return true;
    return false;
}

set<string> zwierzak;

char buf[100];

void readtree(int ff, bool ssn){
int ja = licznik;
licznik++; 
    char op = ' ';
    while(op != '('){
        scanf("%c", &op);
    }
    
    double ww = 2.0; scanf("%lf", &ww);
    
    op = ' ';
    
    string opis = "+++_mib"; // + char ill.
    
    while(op != ')'){
        scanf("%c", &op);
        if ( isLetter(op) ){
            opis = " ";
            opis[0] = op;
            
            while(true){
                scanf("%c", &op);
                if ( isLetter(op) ){
                    opis.push_back(op);
                } else break;
            }
            
            

               //  cout << "prawda" << endl;
            readtree(ja, true);
               // cout << "falsz" << endl;
            readtree(ja, false);
               // cout << "wychodze" << endl;

    
        }
    }
    
 //   cout << "dodaje " << ja << ' ' << " op [" << opis << "] w " << ww << endl;
    
    
    T[ja].cecha = opis;
    T[ja].waga = ww;
    
    if ( ssn ) T[ff].prawda = ja; else T[ff].falsz = ja;
 
    
    
 
}

void drzewko(){
scanf("%d", &L);
for(int i=0; i<200; ++i) T[i].prawda = T[i].falsz = -1;
readtree( 0, true );
}

double laz(int n){
    if ( T[n].prawda < 0 ) return T[n].waga;
    if ( zwierzak.find( T[n].cecha ) != zwierzak.end() ) return T[n].waga * laz( T[n].prawda ); else return T[n].waga * laz( T[n].falsz ); 
}

void testcase(int numer){
licznik = 1;
drzewko();

int n; scanf("%d", &n);

for(int i=0; i<n; ++i){

    zwierzak.clear();

    scanf("%s", buf);    
    int m; scanf("%d", &m);

    for (int j=0; j<m; ++j){
        scanf("%s", buf);
        string cecha  = buf;
        zwierzak.insert(cecha);
    }

    double p = laz( 1 );

    printf("%lf\n", p);
}

}

int main(){
int cases; scanf("%d", &cases);

for(int i=1; i<=cases; ++i){
    printf("Case #%d:\n", i);
    testcase(i);
}

return 0;
}

