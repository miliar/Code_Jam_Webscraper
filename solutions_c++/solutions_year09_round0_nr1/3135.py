#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
ifstream fin;
ofstream fout;
fin.open("A-large.in");
fout.open("A-large-out.in");
int L,D,N;
fin >> L >> D >> N;
string words[D];
bool set[D];
string curr;
char inp;
char dic;
int count=0;
int result=0;
int off=0;
int temp=0;
// dictionary building
for (int i=0; i < D; i++)
{
	fin >> words[i];
}


// the real thing
for (int i=0; i < N; i++)
{
	
	off=0;
	temp=0;
	count=0;
 fin >> curr;
 	for (int k=0; k<L; k++)
 	{
 	inp = curr[k+off];
 		if(inp != '(')
 		{
	 		
	 		//fout << "entered " << k << endl;
	 		for(int j=0; j<D; j++)
	 		{
	 			if(set[j]!=0)
	 			{
	 				dic = words[j][k];
	 				if(inp!=dic)
	 				{
	 					set[j]=0;
	 					//fout << inp << "  " << dic << endl; 
	 				}	
	 			}
	 		}
 		}
 		else
 		{
 			//fout << "reentered " << k << endl;
 			inp=curr[k+off];
 			//fout << off << " " << inp << endl;
 			for(int j=0; j<D; j++)
 			{
 				if(set[j]!=0)
 				{
 					set[j]=0;
 					temp=0;
 					dic = words[j][k];
 					while(inp!=')')
 					{
 						temp++;
 						inp=curr[k+off+temp];
 						if(inp==dic)
 						{
 							set[j]=1;
 							break;
 						}
 					
 					}
 					//fout << endl;
 				}
 			inp=curr[k+off];
 			}
 			inp=curr[k+off];
 			while(inp!=')')
 			{
 				off++;
 				inp=curr[k+off];
 			}
 		}
 		
 	}
 	for (int j=0; j < D; j++)
	{	
		if(set[j]==1)
		{
			count++;
		}
		else
		{
			set[j]=1;
		}
	}
	fout << "Case #" << i+1 << ": " << count <<endl; 
	
}

}
