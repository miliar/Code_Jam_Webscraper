// welcome code jam problem 3.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;



int DP[1000][1000];
char welcome[]="welcome to code jam";
char inStr[500];

int wel(int ind1,int ind2,int inSize)
{
	if(ind1==19)
		return 1;
	else if(ind1>19 || ind2==inSize)
		return 0;

	int o1=0,o2=0;
	if(DP[ind1][ind2]!=-1)
		return DP[ind1][ind2];
	else{ 
		if(welcome[ind1]==inStr[ind2])
		{
			o1=wel(ind1+1,ind2+1,inSize);
			
		}
		o2=wel(ind1,ind2+1,inSize);
	
	DP[ind1][ind2]=o1+o2;//o1+o2
	}
	return DP[ind1][ind2];
}

int main()
{
	
	freopen("C-small-attempt0.in","r",stdin);  
	freopen("C-small.out","w",stdout);
	int testcases=0;
	cin>>testcases;
	for(int i=0; i<=testcases ;i++)
	{
		
		memset(DP,-1,sizeof(DP));
		
		cin.getline(inStr,500);
		
		if(i!=0){
		int size=strlen(inStr);
		
		int result=wel(0,0,size);//need accumulate the 1's
		stringstream ss(stringstream::in | stringstream::out);
		ss<<result;
		string str=ss.str();
		string subStr="0";
		if(str.size()>4)
			subStr=str.substr(str.size()-4,str.size());
		else
		{
			for(int k=0; k<3-str.size() ; k++)
				subStr+="0";
			subStr+=str;
		}
		
		cout<<"Case #"<<i<<": "<<subStr;
		if(i!=testcases)
			cout<<endl;
		}
		
	}
	
}