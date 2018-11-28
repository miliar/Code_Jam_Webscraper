#include <cstdio>
#include <iostream>
#include <fstream>
#include <map>
#include <string>

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
    
    fin >> skipws >> T;
    
    for (Case=1;Case<=T;Case++)
    {
		map<char,map<char,char> > combine;
		map<char,map<char,bool> > opposed;
		string elem;
		
		for(char c='A';c<='Z';c++)
			for(char d='A';d<='Z';d++){
				opposed[c][d]=false;
				combine[c][d]=0;
			}
		
		int C,N;
		fin >> C;
//		cout<<C;
		for(int i=0;i<C;i++){
			char c1,c2,c3;
			fin>>c1>>c2>>c3;
//			cout<<c1<<c2<<c3<<endl;
			combine[c1][c2]=c3;
			combine[c2][c1]=c3;
			
		}
		fin >> C;
		for(int i=0;i<C;i++){
			char c1,c2;
			fin>>c1>>c2;
//			cout<<c1<<c2<<endl;
			opposed[c1][c2]=true;
			opposed[c2][c1]=true;
		}
		fin >> N;
		for(int i=0;i<N;i++){
			char c,com;
			int l=elem.length();
			fin>>c;
			if(l==0){
				elem+=c;
			}else{
				if ((com=combine[elem[l-1]][c])!=0){
					elem[l-1]=com;
				}else{
					for(int j=0;j<l;j++){
					  	if (opposed[elem[j]][c]){
							elem.clear();
							break;
						}
					}
					if (elem.length()>0) elem+=c;
				}
			}
//			cout << elem << endl;
		}
			
        fout << "Case #" << Case << ": [";
		
		if (elem.length()==1){
			fout << elem[0];
		}else if (elem.length()>1){
			fout << elem[0];
			for(int i=1;i<elem.length();i++){
				fout << ", " << elem[i];
			}
		}
		
		fout << "]\n";
    }
	fin.close();
    fout.close();
}
