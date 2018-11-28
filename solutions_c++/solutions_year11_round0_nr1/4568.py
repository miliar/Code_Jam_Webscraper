#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    /////////////////////////INPUT//////////////////////////////
    ifstream *pFileStream = 0;
    pFileStream = new ifstream("testcase1.in");
    if(pFileStream->bad()){
        cerr << "failed open file.\n";
        system("PAUSE");
        return 0;
    }
    ///////////////////////INIT OUTPUT///////////////////////////
    ofstream pOutFileStream("solve.txt");
    if(pOutFileStream.bad()){
        cerr << "error open write file\n";
        system("PAUSE");
        return 0;
    }
    
    int T,i,j,N,*O,*B;
    char *seq;
    
    (*pFileStream) >> T;
    for(i=0;i<T;i++){
        (*pFileStream) >> N;
        O = new int[N];
        B = new int[N];
        seq = new char[N];
        int Ocurpos=0,Bcurpos=0;
        for(j=0;j<N;j++){
            (*pFileStream) >> seq[j];
            if(seq[j]=='O'){
                (*pFileStream) >> O[Ocurpos];
                Ocurpos++;
            }else{
                (*pFileStream) >> B[Bcurpos];
                Bcurpos++;
            }
        }
        
        int runseq = 0,stop=0,Orunseq=0,Brunseq=0;
        int Opos = 1,Bpos = 1,step=0;
        while(!stop){
            if(seq[runseq]=='O'){
                if(O[Orunseq]==Opos){
                    runseq++;
                    if(runseq>=N){stop=1;}
                    Orunseq++;
                }else{
                    if(Opos<O[Orunseq]){
                        Opos++;
                    }else if(Opos>O[Orunseq]){
                        Opos--;
                    }
                }
                if(Bpos<B[Brunseq]){
                    Bpos++;
                }else if(Bpos>B[Brunseq]){
                    Bpos--;
                }
            }else{
                if(B[Brunseq]==Bpos){
                    runseq++;
                    if(runseq>=N){stop=1;}
                    Brunseq++;
                }else{
                    if(Bpos<B[Brunseq]){
                        Bpos++;
                    }else if(Bpos>B[Brunseq]){
                        Bpos--;
                    }
                }
                if(Opos<O[Orunseq]){
                    Opos++;
                }else if(Opos>O[Orunseq]){
                    Opos--;
                }
            }
            
            //cout << step << " >> " << Opos << "\t" << Bpos << " <> " << seq[runseq] << endl;
            step++;
        }
        cout << "Case #" << i+1 << ": " << step << endl;
        pOutFileStream << "Case #" << i+1 << ": " << step << endl;
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}

