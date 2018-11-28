// google code jam 2010 round1B, #2
// author Zhong Wang, clock.w@gmail.com

#include<iostream>
#include<stdio.h>
#include<fstream>

using namespace std;



int main(){
    int T;
	long N;
	
    ifstream fin("A-small-attempt1.in");
    fin>>T;
    
    ofstream fout;
    fout.open("A-small-attempt1.out");
    
    for(int t=1;t<=T;++t)
    {fin>>N;
    int posA[1001],posB[1001];
	long counter=0;
	
	for(int i=1;i<=N;++i)
	fin>>posA[i]>>posB[i];
	
	for(int i=1;i<=N;++i)
		for(int j=i+1;j<=N;++j)
		{if((posA[i]-posA[j])*(posB[i]-posB[j])<0)
		counter++;
		
		}
	
	
	
	fout<<"Case #"<<t<<": "<<counter;
	//cout<<"Case #"<<c<<": "<<exchanges<<endl;
	if(t!=T)  fout<<endl; 
    }
            
    fout.close();

    return 0;
}
