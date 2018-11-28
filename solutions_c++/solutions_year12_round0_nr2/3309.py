#include <cstdlib>
#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    ifstream filein("/home/rohit/Downloads/B-large.in");
    ofstream fileop("/home/rohit/Downloads/B-large.out");
    if(filein.good())cout<<"input file open"<<endl;
    if(fileop.good())cout<<"outputfile open"<<endl;
    int notc;


    
    filein>>notc;
    cout<<notc<<endl;
	
    for(int i=1;filein.good()&&i<=notc;i++){
	int nod,s,p;
        filein>>nod>>s>>p;
	//filein.flush();
        int withouts=0,withs=0,nsp=0;
	for(int j=0;j<nod;j++){
		int score;
		filein>>score;
		if(p-1+p-1+p<=score)withouts++;
		else if(p==1)nsp++;
		else if(p-2+p-2+p<=score)withs++;
		else nsp++;
       	}
	cout<<withouts+withs+nsp<<" "<<nod<<endl;     
        fileop<<"Case #"<<i<<": "<<withouts+min(s,withs)<<endl;
    
    }
    filein.close();
    fileop.close();
    
    return 0;
}

