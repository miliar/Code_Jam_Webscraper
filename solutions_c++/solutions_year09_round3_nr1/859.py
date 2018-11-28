#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main (int argc, char * const argv[]) {
    // insert code here...
	
	ifstream myfile("/Users/Ashkan/Documents/Programming/Input/A-large.in.txt");
	ofstream output("/Users/Ashkan/Documents/Programming/Output/A-large.out");
	
	int i,j,T,k,flag;
	long long int num,newdig;
	string V;
	int digit[100];
	if (myfile.is_open())
	{
		myfile >> T;
		for(i=1;i<=T;i++)
		{
			myfile >> V;
			for(j=0;j<100;j++)
				digit[j]=0;
			newdig=0;
			digit[0]=1;
			for(j=1;j<V.size();j++)
			{
				flag=0;
				for(k=0;k<j;k++)
				{
					if(V[k]==V[j])
					{
						digit[j]=digit[k];
						flag=1;
					}
				}
				if(flag==0)
				{
					digit[j]=newdig;
					if(newdig==0)
						newdig=2;
					else
						newdig++;
				}
//				output << digit[j];
//				output.flush();
			}
//			output <<endl;
			num=0;
			if (newdig<2)
				newdig=2;
			for(j=0;j<V.size();j++)
				num=num*newdig+digit[j];
			output <<"Case #"<<i<<": "<< num<<endl;
		}
		myfile.close();
		output.close();
	}		
	
	else cout << "Unable to open file"; 	
    return 0;
}
