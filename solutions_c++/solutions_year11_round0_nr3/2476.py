#include <cstdio>
#include <iostream>
#include <fstream>
#include <climits>

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
		int sum=0,binsum=0,min=INT_MAX,N;
		fin >> N;
		for(int i=0;i<N;i++){
			int candy;
			fin >> candy;
			sum+=candy;
			binsum^=candy;
			if (candy<min) min=candy;
		}
		
        fout << "Case #" << Case << ": ";
		if(binsum==0){
			fout << (sum-min);
		}
		else
			fout << "NO";
		fout << "\n";
    }
	fin.close();
    fout.close();
}
