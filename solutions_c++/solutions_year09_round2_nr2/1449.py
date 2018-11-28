#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;


int main (int argc, char * const argv[]) {
    
	string WELC="welcome to code jam";
	
	fstream INP("input.txt",fstream::in);
	fstream OUT("output.txt",fstream::out);
		
	int T;
	INP>>T;
	
	for(int c=0;c<T;c++)
		{
		string N;
		INP>>N;
		
		vector<int> Num(N.size(),0);
		for(int j=0;j<N.size();j++)
			Num[j]=N[j]-'0';
		
		vector<int> save(Num);
		
		sort(save.begin(),save.end());
		
		next_permutation(Num.begin(),Num.end());
		
		if(Num==save)
			{
			Num.push_back(0);
			sort(Num.begin(),Num.end());
			while(Num[0]==0)
				next_permutation(Num.begin(),Num.end());
			}
		
		
		
		
		OUT<<"Case #"<<c+1<<": ";
		
		
		for(int i=0;i<Num.size();i++)
			OUT<<Num[i];
		OUT<<endl;
		
		
		}
		
		
	
	
    return 0;
}
