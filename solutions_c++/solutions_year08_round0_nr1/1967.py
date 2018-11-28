#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
	
	fstream f;
  	f.open(argv[1], fstream::in);
	
	string junk;	
	int nC;
	f>>nC;
	for(int i=0; i<nC; i++)
 	{
		int nS,nQ,j;
		int nSW=0;
		map<string, int> nSQ;
		
		f>>nS;
		getline(f, junk);
		for(j=0; j<nS; j++)
		{
			string s;
			getline(f, s);
			nSQ[s]=0;
		}
		
		f>>nQ;
		getline(f, junk);
		
		for(j=0; j<nQ; j++)
		{
			string q;
			getline(f, q);
			map<string, int>::iterator obj = nSQ.find(q);
			if(obj != nSQ.end())
			{
				int allF = 1;
				(*obj).second = 1;
				for(map<string, int>::iterator ii=nSQ.begin(); ii!=nSQ.end(); ++ii)
				{
					allF = allF&((*ii).second);
				}
				if(allF)
				{
					nSW +=1;
					//cout<<(*obj).first<<endl;
					for(map<string, int>::iterator ii=nSQ.begin(); ii!=nSQ.end(); ++ii)
					{
						(*ii).second =0;
					}
					(*obj).second=1;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<nSW<<endl; 
	}
	f.close();
}

