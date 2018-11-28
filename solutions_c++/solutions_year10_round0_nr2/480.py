#include "BigIntegerLibrary.hh"
#include <fstream>
#include <vector>
#include <string>
using namespace std;
int main(int argc,char* argv[])
{

    ifstream ifs(argv[1]);
    ofstream ofs(argv[2]);
    int C;
    ifs>>C;
    for(int i=0;i<C;i++)
    {
	    int N;
	    vector<BigUnsigned> vecBigUnsigned;
	    vector<BigUnsigned> vecBigUnsignedDiff;

	    ifs>>N;	   
	    
	    for(int j=0;j<N;j++)
	    {
		    string s;
		    ifs>>s;
		    vecBigUnsigned.push_back(stringToBigUnsigned(s));
	    }

	    for(int j=1;j<N;j++)
		    if(vecBigUnsigned[j]>vecBigUnsigned[j-1])
			    vecBigUnsignedDiff.push_back(vecBigUnsigned[j]-vecBigUnsigned[j-1]);
		    else
			    vecBigUnsignedDiff.push_back(vecBigUnsigned[j-1]-vecBigUnsigned[j]);

	    BigUnsigned gcdResult= vecBigUnsignedDiff[0];
	    for(int j=1;j<N-1;j++)
		    gcdResult=gcd(gcdResult,vecBigUnsignedDiff[j]);
	    BigUnsigned modResult=vecBigUnsigned[0]%gcdResult;
	    BigUnsigned Result;
	    if(modResult.isZero()) 
		    Result=modResult;
	    else
		    Result=gcdResult-modResult;
	    ofs<<"Case #"<<i+1<<": "<<Result<<endl;

    }
    ifs.close();
    ofs.close();
    
    
} 

