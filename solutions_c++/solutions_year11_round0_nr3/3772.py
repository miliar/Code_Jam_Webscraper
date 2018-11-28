#include <iostream>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <cstring>
#include<bitset>
using namespace std;

string numToBinary(int a)
{
	
	string mystring="";

	bitset<20> mybits = a;
	//cout<<"fn called"<<endl;
	mystring += mybits.to_string<char,char_traits<char>,allocator<char> >();
	//cout<<"fn done"<<endl;
	return mystring;
}

	int binaryToInt(string s)											//converts a binary string to integer
	{
		int converted=0;
		int multiplier=1;
		for(int i=s.length()-1; i>=0 ; i-- )
		{
			if(s[i] == '1')
			{
				converted += multiplier;
			}
			multiplier = multiplier *2 ;
		}
		return converted;
	}

	string addTwoBinary(string s1,string s2)
	{
		char* result;
		result=new char[20];
		for(int i=0;i<20;i++)
		{
			if((s1[i]=='0' && s2[i]=='0') || (s1[i]=='1'&& s2[i]=='1'))
			result[i]='0';
			else
			result[i]='1';
		}
		string str(result);
		str=str.substr(0,20);
		//cout<<endl<<"result is : "<<str<<"   "<<endl;
		return str;
	}
	
main()
{
	
	int n;
	ifstream inp;
	inp.open("C-large.in");
	ofstream out("C-large.out");
	int numInp;
	int *inputs;
	string *strInp;
	string res="00000000000000000000";
	inp>>n;
	int sum=0;
	
	
	for(int i=0;i<n;i++)
	{
		inp>>numInp;
		inputs=new int[numInp];
		strInp=new string[numInp];
		int min=999999;
		//cout<<"inside loop"<<endl;
		for(int j=0;j<numInp;j++)
		{
			//cout<<"scon loop"<<endl;
			
			inp>>inputs[j];
			string temp;
			temp=numToBinary(inputs[j]);
			
			//cout<<"string is : "<<temp<<endl;
			strInp[j]=temp;
			//cout<<"scon loop 2"<<endl;
			sum=sum+inputs[j];
			res=addTwoBinary(res,strInp[j]);
			//cout<<"sum is: "<<res<<endl;
			if(min>inputs[j])
			min=inputs[j];
		}
		if(res=="00000000000000000000")
		{
			out<<"Case #"<<i+1<<": "<<sum-min<<endl;
		}
		else
		out<<"Case #"<<i+1<<": NO"<<endl;
		
		res="00000000000000000000";
		sum=0;
		min=0;
	
	}
	
	
}