#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;


int main (int argc, char * const argv[]) {
    
	string WELC="welcome to code jam";
	
	fstream INP("input.txt",fstream::in);
	fstream OUT("output.txt",fstream::out);
	fstream NUM("input.txt",fstream::in);
	int N;
	NUM>>N;
	NUM.close();

	char DIO;
	while(DIO!='\n')
		{
		INP.get(DIO);
		cout<<DIO;
		}
	cout<<endl;
	
	map<char, vector<int> > dove;
	
	for(char t='a';t<='z';t++)
		{
		for(int j=0;j<WELC.size();j++)
			if(WELC[j]==t)
				dove[t].push_back(j);
		
		}
	char t=' ';
		for(int j=0;j<WELC.size();j++)
			if(WELC[j]==t)
				dove[t].push_back(j);
				
	for(int c=0;c<N;c++)
		{
		string OUR="";
		char T='a';
		while(T!='\n')
			{
			INP.get(T);
			OUR+=T;
			}
		vector< vector<int> > matr(WELC.size(),vector<int>(500,0));
		
		cout<<OUR;
		
		for(int i=0;i<500;i++)
			{
			
			if(i!=0)
			{
			for(int j=0;j<WELC.size();j++)
				matr[j][i]=(matr[j][i]+matr[j][i-1])%1000;
			}
			
			
			if(OUR[i]=='w')
				{
				matr[0][i]++;
				continue;
				}
			if(i!=0)
			
				for(int j=0;j<dove[OUR[i]].size();j++)
					matr[ dove[OUR[i]][j] ][i]=(matr[ dove[OUR[i]][j] ][i]+ matr[ dove[OUR[i]][j] -1][i-1])%1000;
			
			
			
			
			}
			
			for(int i=0;i<WELC.size();i++)
				{
				
				for(int j=0;j<30;j++)
					cout<<matr[i][j]<<" ";
				
				cout<<endl;
				}
			cout<<endl;
			
			stringstream OS;
			OS<<matr[WELC.size()-1][OUR.size()-1]+10000;
			string m;
			OS>>m;
			
			OUT<<"Case #"<<c+1<<": "<<m[1]<<m[2]<<m[3]<<m[4]<<endl;
		
		}
		INP.close();
		OUT.close();
		
		
		
		
	
	
    return 0;
}
