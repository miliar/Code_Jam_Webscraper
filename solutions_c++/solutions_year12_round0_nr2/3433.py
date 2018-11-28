#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include <windows.h>
using namespace std;

int main()
{
	long start = GetTickCount();
	ifstream input("B-large.in",ios::in);
	if(!input)
	{
		cerr<<"Cannot read target file"<<endl;
		exit(1);
	}

	ofstream output("B-large.out",ios::trunc);//out
	if(!output)
	{
		cerr<<"Cannot open output file"<<endl;
		exit(1);
	}
	int lines ;
	input>>lines;



	int i =0;
	string str = "";
	for (i=0;i<lines;i++)
	{
		//Spell(i,line,input,output);
		int N = 0;
		int S = 0;
		int p = 0;
		int outN = 0;
		string out = "Case #";

		char ch[256];
		sprintf(ch,"%d",i+1);
		out = out + ch + ": ";
		getline(input,str);
		if(0 == i)
			getline(input,str);
		{

			const string delims(" "); 


			vector<int> ivec; // containter for int 
			//=============
			string::size_type begIdx, endIdx; 

			begIdx = str.find_first_not_of(delims); 

			while (begIdx != string::npos) { 
				endIdx = str.find_first_of(delims, begIdx); 
				if (endIdx == string::npos) { 
					endIdx = str.length(); 
				} 
				ivec.push_back(atoi(string(str, begIdx, endIdx-begIdx).c_str())); 

				begIdx = str.find_first_not_of(delims, endIdx); 
			} 

			for ( int ix = 0; ix < ivec.size(); ++ix ) 
			{	//cout << ivec[ ix ] << ' '; 
				if(ix == 0)
					N=ivec[ix];
				if (ix == 1)
				{
					S=ivec[ix];
				}
				if (ix == 2)
				{
					p=ivec[ix];
				}
		
			}
		//	cout<<endl;

			for ( int ix = 3; ix < N + 3; ++ix ) 
			{	
				int data = ivec[ ix ];
				if(p==0)
				{
					outN++;
					continue;
				}
				else if(p ==1 && data > 0){
					outN++;
					continue;
				}
				else if(data >= 3*p - 2&&3*p - 2>=0) 
				{
					outN++;	
				}
				else if(data >= 3*p -4&&3*p -4>=0 ) 
				{
					if(--S>=0)
					outN++;	
				}
			}
			//cout<<endl;
	

			//==============
		}
	 char cc[20];   
	 sprintf(cc, "%d", outN);  
		out = out + cc + "\n";
		output<<out;
	}

	input.close();
	output.close();
	long end = GetTickCount();
	cout<<"Time : "<<end - start<<" ms"<<endl;
	//system("pause");
	return 0;
}



