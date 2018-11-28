#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <iomanip>
#include <cmath>

using namespace std;
typedef long long int64;

int main (int argc, char * const argv[]) {
	
	fstream INP("input.txt",fstream::in);
	fstream OUT("output.txt",fstream::out);
		
	int T;
	INP>>T;
	
	for(int c=0;c<T;c++)
		{
		
		int P,Q;
		INP>>P>>Q;
		vector<int> perm(Q,0);
		for(int i=0;i<Q;i++)
			perm[i]=i;
		
		vector<int> celle(P,1);
		vector<int> init(P,1);
		vector<int> assoc(Q,0);
		
		for(int i=0;i<Q;i++)
			INP>>assoc[i];
		
		for(int i=0;i<Q;i++)
			assoc[i]--;
		
		int cost=INT_MAX;
		
		do
		{
		celle=init;
		int partcost=0;
		
		for(int i=0;i<Q;i++)
			{
			celle[assoc[perm[i]]]=0;
			
			for(int j=assoc[perm[i]]+1;j<P;j++)
				{
				
				if(celle[j]==0)
					break;
				partcost++;
				}
			for(int j=assoc[perm[i]]-1; j>=0;j--)
				{
				if(celle[j]==0)
					break;
				partcost++;
				}
			
			}
			
		cost=min(cost,partcost);
		
		
		}while(next_permutation(perm.begin(),perm.end()));
		
		
		
		OUT<<"Case #"<<c+1<<": "<<cost<<endl;
		
		}
		
		
	
	
    return 0;
}
