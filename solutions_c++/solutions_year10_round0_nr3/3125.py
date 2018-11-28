// google code jam 2010 qualification round, #3
// author Zhong Wang, clock.w@gmail.com

#include<iostream>
#include<stdio.h>
#include<fstream>
#include<queue>

using namespace std;

int main(){
    int T;
    long R, k, N;
    
	

    ifstream fin("C-small-attempt0.in");
    fin>>T;
    
    ofstream fout;
    fout.open("C-small.out");
    
    for(int i=1;i<=T;++i)
    {
		fin>>R>>k>>N;
    
		queue<long> Q, C;
		long revenue=0;
	
		for(long j=1;j<=N;++j)
		{
			long a;
			fin>>a;
			Q.push(a);
	
		}	
	
		
	
		for(long j=1;j<=R;++j)
		{
			while(!C.empty())
			{
				Q.push(C.front());
				C.pop();
	
			}
			
			long remain=k;
			
			while((remain >= Q.front())&&(!Q.empty()))
			{
			remain -= Q.front();
			revenue += Q.front();
			C.push(Q.front());
			Q.pop();
			}
	
		
	
		}
	
	fout<<"Case #"<<i<<": "<<revenue;
	if(i!=T) fout<<endl;        
    
	}
            
    fout.close();

    return 0;
}
