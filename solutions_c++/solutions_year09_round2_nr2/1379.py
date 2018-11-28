

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

int N;
int D;
int L;

int getNext(int num){
int i,j,n;
vector<int>ab;
int pp=num;
string def;
stringstream defT;
while(pp)
{
	int sp = pp%10;
	pp=pp/10;
	if(sp!=0)
	ab.push_back(sp);
}

sort(ab.begin(),ab.end());
for(int k=0;k<ab.size();k++)
{
	defT<<ab[k];
}
defT>>def;





for(i=num+1;;i++)
{
    vector<int>tt;
    string cu;
    stringstream cuT;
    pp=i;
    while(pp)
	{
	int sp = pp%10;
	pp=pp/10;
	if(sp!=0)
	tt.push_back(sp);
	}
	
	sort(tt.begin(),tt.end());
	for(int k=0;k<tt.size();k++)
	{
	cuT<<tt[k];
	}
	cuT>>cu;
	
	if(cu==def)
	return i;
	
}
    
   
    



return num;
}


int main(){
    int i,j,n,k,np;
    
    outfile.open ("C:\\test\\out.txt");
    string line;
    ifstream myfile ("C:\\test\\B-small-attempt1.in");
    getline (myfile,line);
    stringstream iss;
    iss<<line;
    iss>>N;


	for(i=0;i<N;i++)
	{
		int curr =0;
		int ans =0;
		iss.clear();
		getline (myfile,line);
		
	    iss<<line;
	    iss>>curr;
	    
	    ans= getNext(curr);
	    
	    iss.clear();
	    iss<<ans;
     	string kk;
     	iss>>kk;
     	
	    iss.clear();
	    iss<<i+1;
	    string caseV;
	    iss>>caseV;

	    writeFile("Case #"+caseV+": "+kk);
	}

		
		

    myfile.close();
	outfile.close();

    cin>>i;
    return 0;
}
