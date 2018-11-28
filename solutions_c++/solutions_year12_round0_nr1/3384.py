#include <algorithm> 
#include <iostream>
#include <string>
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;

#include<fstream>
//ifstream fin1("input1.txt");
ifstream fin("input.txt");
ofstream fout("output.txt");
//ofstream fout1("output1.txt");

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;  

FILE *fp1 = fopen("input1.txt", "r");
FILE *fp1out =  fopen("output1.txt", "r");

FILE *finC = fopen("input.txt", "r");
//FILE *fout = fopen("output.txt", "w");
char ARR_CODE[30] = {0};

void createDecoder()
{
      char ch, ch1;
      int z;
      while ((ch = getc(fp1)) != EOF)
      {
            z = int(ch);
            ch1 = getc (fp1out);

            if(z>=97 && z<=122)
              ARR_CODE[z - 97] =  ch1;

              ARR_CODE[16] = 'z';
              ARR_CODE[25] = 'q';

           // cout << "code : " <<ch <<"DECODE :"<< ARR_CODE[z - 97]<<endl;

            //cout <<"ch:" << ch <<" Z:" <<z << " ch1:"<< ch1<<endl;

        }

        //FORE(i,0,25)
         // cout << i <<" " << ARR_CODE[i]<<endl;


      return;

}

void run(int casenr) {
    fout << "Case #" << casenr <<": ";

    char ch, ch1;
      int z;

    while ((ch = getc(finC)) != '\n'&& ch != EOF)
     {
        z = int(ch);
        if(ch == ' ')
         fout << ch;
        else
        fout << ARR_CODE[z-97];
     }

    fout << endl;
}

int main() {
    if(NULL == fin)
    {
      cout<<"NO INPUT FILE"<<endl;
      return 0;
    }

    createDecoder();

    int n;  fin >> n;
    char ch;
     while ((ch = getc(finC)) != '\n');
    FORE(i,1,n) run(i);

    fclose(finC);
    fclose(fp1);
    fclose(fp1out);
   system("PAUSE");
	return 0;
}

