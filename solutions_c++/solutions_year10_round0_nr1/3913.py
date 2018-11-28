#include <cstdlib>
#include <iostream>
#include <map>
#include <sstream>

using namespace std;

int power(int b)
{
     int c=2;
     for (int n=b; n>1; n--) c*=2;
     return c;
}

string convertint(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

int main(int argc, char *argv[])
{FILE *ulaz;
int i=0;
FILE *izlazna;
char red[10];
double casenum,prvinum,druginum,prvinumpotenc;
string prvi,drugi,ispis;
size_t found;
string linija;


ulaz = fopen("A-large.in", "r");               
izlazna = fopen("izlazna.txt", "w+");


fgets(red, 100, ulaz);
linija = (string) red;
casenum=atoi(linija.c_str());


int provjera=0;
int brojcitanje=0;

for(i=1;i<=casenum;i++) {



fgets(red,100,ulaz);
linija=(string)red;
found=linija.find_first_of(" ");
prvi=linija.substr(0,found+1);

prvinum=atoi(prvi.c_str());
drugi=linija.substr(found, linija.size()-found);
druginum=atoi(drugi.c_str());

prvinumpotenc=power(prvinum)-1;
if(prvinumpotenc==druginum){
provjera=1;
ispis="Case #"+convertint(i)+": "+"ON\n";
                      }
                      
else if(druginum>prvinumpotenc) {
while(druginum>prvinumpotenc){
druginum=druginum-(prvinumpotenc+1);
if(druginum==prvinumpotenc){
provjera =1;
 ispis="Case #"+convertint(i)+": "+"ON\n";       
 break;                 
                            }
                        }
 
                     }
if(provjera==0) {
 
ispis="Case #"+convertint(i)+": "+"OFF\n";            
     }
fputs(ispis.c_str(),izlazna);
       provjera=0;         
                        }

    system("PAUSE");
    return EXIT_SUCCESS;
}
