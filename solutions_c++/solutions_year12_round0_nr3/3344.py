#include <cstdlib>
#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstring>
#include<vector>
#include<sstream>

using namespace std;

long long int rsame(long long int n,long long int m){
 	string ns;
	string ms;
	stringstream out1;
	stringstream out2;
	out1<<n;
	ns=out1.str();
	out2<<m;
	ms=out2.str();
	int ln=ns.size();
	int lm=ms.size();
	for(int i=0;i<ln;i++){
		
		if((ms[0]!='0')&&ns.compare(ms)==0){
			return true;
			}
		else{
		char temp=ms[lm-1];
		for(int j=lm-2;j>=0;j--)ms[j+1]=ms[j];
		ms[0]=temp;
		}
	}
	return false;	
}

int main(int argc, char** argv) {
    ifstream filein("/home/rohit/Downloads/C-small-attempt0.in");
    ofstream fileop("/home/rohit/Downloads/C-small-attempt0.out");
    if(filein.good())cout<<"input file open"<<endl;
    if(fileop.good())cout<<"outputfile open"<<endl;
    int notc;
    
    filein>>notc;
    cout<<notc<<endl;
	
    for(int i=1;filein.good()&&i<=notc;i++){
	long long int a,b;
        filein>>a>>b;
	long long int count=0;
	for(long long int n=a;n<b;n++){
		for(long long int m=n+1;m<=b;m++){
			if(rsame(n,m))count++;
		}
       	}
        fileop<<"Case #"<<i<<": "<<count<<endl;
    
    }
    filein.close();
    fileop.close();
    
    return 0;
}

