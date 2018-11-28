#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <sstream>
 
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
	
	int count=0;
	int i =0;
	string str = "";
	vector<int> scores;
	int score;

	string temp;
	int num_G = 0;
	int num_S = 0;
	int num_S_real = 0;  //Êµ¼ÊµÄsurprise
	int P = 11;

	for (i=0;i<lines;i++)
	{
		//Spell(i,line,input,output);

		count=0;
		num_G = 0;
		num_S = 0;
		num_S_real = 0;
		P = 11;
		scores.clear();

		string out = "Case #";		
		char ch[256];
		sprintf(ch,"%d",i+1);
		out = out + ch + ": ";
		
		

		getline(input,str);
		if(0 == i)
			getline(input,str);
		istringstream stream(str);
		while(stream>>temp)
		{
			score = atoi(temp.c_str());
			scores.push_back(score);
			//cout<<temp.c_str()<<endl;
		}
		num_G = scores[0];
		num_S = scores[1];
		P = scores[2];

		int rmd = -1;
		int qut = 0;
		for(vector<int>::size_type ix = 0; ix != num_G; ++ix)
		{
			if(0 == P)
			{
				count = num_G;
				break;
			}
			if(scores[ix+3] > 0)
			{
				rmd = scores[ix+3]%3;
				qut = scores[ix+3]/3;
				if(qut >= P)
					count++;
				else
				{
					if((0 == rmd) && (qut+1) >= P)
						num_S_real++;
					else if((1 == rmd) && (qut+1) >= P)
						count++;
					else if(2 == rmd)
					{
						if((qut+1) >= P)
							count++;
						else if((qut+2) >= P)
							num_S_real++;
					}

				}
			}
		}
		if(num_S_real <= num_S)
			count += num_S_real;
		else count += num_S;

		char ch_1[128];
		sprintf(ch_1,"%d",count);

		out = out + ch_1 + "\n";
		output<<out;
	}

	input.close();
	output.close();
	long end = GetTickCount();
	cout<<"Time : "<<end - start<<" ms"<<endl;
	system("pause");
	return 0;
}