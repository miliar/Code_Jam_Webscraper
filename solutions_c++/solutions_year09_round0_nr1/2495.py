#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int similar(string word,string pattern, int L)
{
	int X=1;
	int i,p,flag;
	p=0;
	i=0;
	while((X==1) && (i<L))
	{
		if(pattern[p]=='(')
			{
				flag=0;
				p++;
				while(pattern[p]!=')')
				{
					if(pattern[p]==word[i])
						flag=1;
					p++;
				}
				p++;
				if(flag==0)
					X=0;
			}
		else
			if (pattern[p]!=word[i])
					X=0;
			else
				p++;
		i++;
	}
	return X;
}
int main (int argc, char * const argv[]) {
    // insert code here...
	string words[5500],inputword;
	int i,N,L,D,X,j;
	
	ifstream myfile("/Users/Ashkan/Documents/Programming/Input/A-small-attempt0.in");
	ofstream output("/Users/Ashkan/Documents/Programming/Output/A-small-attempt0.out");
	
	if (myfile.is_open())
	{
		myfile >> L;
		myfile >> D;
		myfile >> N;
		for(i=0;i<D;i++)
		{
			myfile >> words[i];
		}
		
		for(i=1;i<=N;i++)
		{
			myfile >> inputword;
			X=0;
			for(j=0;j<D;j++)
				if (similar(words[j],inputword,L)==1)
					X++;
			
			output <<"Case #"<<i<<": "<<X<<endl;
		}
		
		
/*		
		for(i=1;i<=N;i++)
		{
			myfile >> alien_number;
			myfile >> source_lang;
			myfile >> target_lang;
			
			source=source_lang.size();
			target=target_lang.size();
			
			number=0;
			
			for(j=0;j<alien_number.size();j++)
			{
				digit=0;
				for(k=0;k<source_lang.size();k++)
					if(alien_number[j]==source_lang[k])
						digit=k;
				
				number=number*source+digit;
			}
			
			//			cout << number<<": ";
			
			target_alien_number="";
			
			do
			{
				digit= number % target;
				number /= target;
				target_alien_number= target_lang[digit]+target_alien_number;
			}
			while(number!=0);
			
			
			
			//			cout << target_alien_number <<endl;
			output <<"Case #"<<i<<": "+target_alien_number<<endl;
			//			cout << alien_number <<" " << source_lang+" "+ target_lang<<endl;
		}
 */
		myfile.close();
		output.close();
	}		
	
	else cout << "Unable to open file"; 	
    return 0;
}
