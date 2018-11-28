#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;
fstream fin,fout;

int n,k;
bool ok = 1;

void wrk(int tst){
    ok = (k%2);
    for(int i=0;i<n;i++){
      ok&= (k%2);
      //fout << k%2;
      k/=2;
      }
    
    //fout << endl;
    
    fout <<"Case #"<<tst<<": ";
    if(ok)
      fout << "ON";else
      fout << "OFF";
    fout << endl;
    }

int main(void){
    fin.open ("./input.txt", fstream::in);
    fout.open("./output.txt",fstream::out);
    
    int test;
    fin >> test;
    for(int i=0;i<test;++i){
      fin >> n >> k;
      wrk(i+1);
      }
    
    fin.close();
    fout.close();
    return 0;
    }













