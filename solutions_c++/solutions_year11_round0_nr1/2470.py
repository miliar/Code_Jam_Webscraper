#include <cstdio>
#include <iostream>
#include <fstream>

#define MAX(a,b) ((a)>(b)?(a):(b))
#define DIFF(a,b) MAX((a)-(b),(b)-(a))

using namespace std;

int main(int argc,char **argv)
{   
    if (argc!=3)
    {
      printf("usage: program-name inputfile outputfile\n");
      exit(1);
    }
    
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    int T,Case;
    
    fin >> T;
    
    for (Case=1;Case<=T;Case++)
    {
        int N,time=0,ot=0,bt=0,op=1,bp=1,button;
        char c;
        fin >> N;
        for(int i=0;i<N;i++){
			fin >> c >> button;
			cout << c << button << endl;
			if(c=='O'){
				time=MAX(time+1,ot+DIFF(op,button)+1);
				ot=time;
				op=button;
			}else{
				time=MAX(time+1,bt+DIFF(bp,button)+1);
				bt=time;
				bp=button;
			}
		}
        
        fout << "Case #" << Case << ": " << time << "\n";
    }
	fin.close();
    fout.close();
}
