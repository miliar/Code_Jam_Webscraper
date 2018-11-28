#include <cstdlib>
#include <iostream>
#include<vector>

using namespace std;

vector<long long int> next(vector<long long int> S)
{
	vector<long long int> S1;
	S1.clear();
	
	int n = (int)S.size();
	
	int carry = 1;
	
	for(int i =0;i<n;i++)
	{
		S[i] =	S[i] + carry;
		
		if(S[i] > 2)
		{
			S[i] = 0;
			carry = 1;
		}
		else
		{
			carry = 0;
			break;
		}
	}	
	
	if(carry)
	{
		return(S1);
	}
		
	return(S);

}

int check(long long int sum)
{
	if(sum%2 == 0 | sum %3 ==0 || sum%5 ==0 || sum%7 == 0)
		return(1);
	return(0);
			
	
}

int main(int argc, char *argv[])
{
	int nCases;
	cin>>nCases;

	int count = 0;
	while(count < nCases)
	{
		count++;
		char *str;
		str = new char [40];
		
		cin>> str;
		//cout<<str<<endl;
		
		char *ch;
		ch = str;
		
		vector<int> V;
		V.clear();
		
		while(*ch != '\0')
		{
			
			int temp;
			
			temp = (int)*ch - (int)'0';
			if(temp >=0 && temp <=9)
				V.push_back(temp);
			
			ch++;
			
		}		
		// input read 
		/*
		for(int i =0;i<(int)V.size();i++)
			cout<<V[i]<<" ";
		cout<<endl;
		*/
			
		vector<long long int> sign(V.size()-1,0);
		
		long long int CCC = 0;
		long long int total =0;

		while(true)
		{
			total++;
			long long int sum = 0; 
			long long int number = V[0];
			long long int lastSymbol = 0;
			
			//for(int k =0;k<(int)sign.size();k++)
			//	cout<<sign[k]<<" ";
			//cout<<endl;
			
			// generate numbers
			for(long long int i=1;i<(long long int)V.size();i++)
			{
				if(sign[i-1] == 0 || sign[i-1] == 1)
				{
					if(lastSymbol == 0)
							sum = sum + number;
					else if(lastSymbol == 1)
						sum = sum - number;
					
					lastSymbol = sign[i-1];
					number = V[i];					
				}			 
				else 
				{
					number = number*10 + V[i];
				}
			}
			

			if(lastSymbol == 0)
				sum = sum + number;
			else if(lastSymbol == 1)
				sum = sum - number;

		//	cout<<abs(sum)<<endl;
			if(sum < 0)
				sum = sum * -1;
			
			CCC += check(sum);		

			vector<long long int> sign1; 
			sign1.clear();
			
			sign1 = next(sign);

			if((long long int)sign1.size() == 0)
				break;
			sign = sign1;				
		}
		//cout<<total<<endl;
		cout<<"Case #"<<count<<": "<<CCC<<endl;
	}// end while
	
    
    return EXIT_SUCCESS;
}
