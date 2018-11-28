#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

inline int rendiNum (char s)
{

return 1<<(int)(s-'a');

}

inline int rendiNum(const string& s)
{
int val=0;

for(int i=0;i<s.size();i++)
	val+=rendiNum((char)s[i]);
return val;
}


int main (int argc, char * const argv[]) {
    
	fstream INP("input.txt",fstream::in);
	fstream OUT("output.txt",fstream::out);
	
	int L,D,N;
	
	INP>>L>>D>>N;
	
	vector<vector<int> > words(D,vector<int>(L,0));
	
	for(int i=0;i<D;i++)
		{
		string aus;
		INP>>aus;
		for(int j=0;j<L;j++)
			words[i][j]=rendiNum((char)(aus[j]));
		}
	
	vector<vector< int> > patterns(N,vector<int>(L,0));
	
	for(int i=0;i<N;i++)
		{
		string grezzo;
		INP>>grezzo;
		vector<string> token(L,"");
		
		string riem="";
		bool inblock=0;
		int curs=0;
		
		for(int j=0;j<grezzo.size();j++)
			{
			if(grezzo[j]=='(')
				{
				inblock=1;
				continue;
				}
			if(grezzo[j]==')' and inblock)
				{
				inblock=0;
				curs++;
				continue;
				}
			
			token[curs]+=grezzo[j];
			if(!inblock)
				curs++;
			}
		
		if(token.size()!=L)
			cerr<<"ERRORE"<<endl;
		
		for(int j=0;j<L;j++)
			patterns[i][j]=rendiNum(token[j]);
		
		}
	
	for(int i=0;i<D;i++)
		{
		for(int j=0;j<L;j++)
			cout<<words[i][j]<<" ";
		cout<<endl;
		}
	cout<<endl<<endl;
	
	for(int i=0;i<N;i++)
		{
		for(int j=0;j<L;j++)
			cout<<patterns[i][j]<<" ";
		cout<<endl;
		}
	cout<<endl;
		
	
	
	for(int i=0;i<N;i++)
		{
			int cont=0;
			
			for(int m=0;m<D;m++)
			{
			for(int j=0;j<L;j++)
				if(!(words[m][j] & patterns[i][j]))
					goto here;
			cont++;
			here:;

			}
		
		
		
		OUT<<"Case #"<<i+1<<": "<<cont<<endl;
		}
	
    return 0;
}
