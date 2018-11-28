#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include <windows.h>
using namespace std;

int main()
{
	long start = GetTickCount();
	ifstream input("C-small-attempt0.in",ios::in);
	if(!input)
	{
		cerr<<"Cannot read target file"<<endl;
		exit(1);
	}

	ofstream output("C-small-attempt0.out",ios::trunc);//out
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
		int start = 0;
		int end = 0;
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
					start =ivec[ix];
				if (ix == 1)				
					end =ivec[ix];				
			}
		//	start = 2020;end = 2020;
			for(int i = start;i<=end;i++)
			{
				char ctem[10];			
				sprintf(ctem, "%d", i);  
				string stem = ctem;

				for(int j=1;j<stem.length();j++)
				{
					string s1 = string(stem,0,j);
					string s2 = string(stem,j,stem.length());
					string s3 = s2 + s1;
				
				//	cout<<s1<<" "<<s2<<" "<<s3<<endl;	
					if (s3[0]=='0')
					{
						continue;
					}
					int ntem = atoi(s3.c_str());
					if (ntem>i&&ntem<=end)
					{
						outN++;
						//cout<<stem<<":"<<s3<<endl;
					}
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



