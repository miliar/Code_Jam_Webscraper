

#include <string>
#include <vector>
#include<iostream>
#include<map>
#include<sstream>
#include<set>
#include<cctype>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<functional>
#include<cmath>
#include<cstdlib>
#include <fstream>


using namespace std;
ofstream outfile;
void writeFile(string a){

    outfile<<a<<"\n";

}
vector<string> words;
int N;
int D;
int L;


int main(){
    int i,j,n,k,np;
    
    outfile.open ("C:\\test\\out.txt");
    string line;
    ifstream myfile ("C:\\test\\A-large.in");
    getline (myfile,line);
    stringstream iss;
    iss<<line;
    iss>>L;
    iss>>D;
    iss>>N;

    for(i=0;i<D;i++)
    {
        getline (myfile,line);
        words.push_back(line);
	}
	
	for(i=0;i<N;i++)
	{
		int curr =0;
		getline (myfile,line);
		map<int,string> letter;
		int cL=0;
		bool chal = true;
		for(int op=0;op<line.size();op++){
			if(line[op]=='(')
			{
				chal = false;
			}
			else if(line[op]==')')
			{
				chal = true;

			} else letter[cL]+=line[op];
			
			if(chal)
			cL++;
		}
		
		
		for( j=0; j <D;j++)
		{   bool check = true;
		    string word = words[j];
		    
			for(k=0;k<L;k++)
			{
				char tt = word[k];
				string currentL = letter[k];
				for(np=0;np<currentL.size();np++){
					if(tt==currentL[np])
					break;
				}
				if(np==currentL.size())
				{
					check=false;
					break;
				}


			}
			
			if(check)
			curr++;
		}
		stringstream kss;
		string caseV;
		string acV;
		
		kss<<i+1;
		kss>>caseV;
		
		kss.clear();
		kss<<curr;
		kss>>acV;
		
		writeFile("Case #"+caseV+": "+acV);
	}

    myfile.close();
	outfile.close();

    cin>>i;
    return 0;
}
