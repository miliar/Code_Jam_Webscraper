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
	ifstream input("C-large.in",ios::in);
	if(!input)
	{
		cerr<<"Cannot read target file"<<endl;
		exit(1);
	}

	ofstream output("C-large.out",ios::trunc);//out
	if(!output)
	{
		cerr<<"Cannot open output file"<<endl;
		exit(1);
	}
	int lines ;
	input>>lines;
	
	long count=0;
	int i =0;
	string str = "";
	vector<long> scores;
	long score;
	vector<long> scores_circle;
	int sign_circle = 0;

	string temp;
	long A = 0;
	long B = 0;

	for (i=0;i<lines;i++)
	{
		//Spell(i,line,input,output);

		scores.clear();
		count = 0;

		string out = "Case #";		
		char ch[10];
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
		}

		A = scores[0];
		B = scores[1];

		if(B <= 10)
		{
			char ch_1[20];
			sprintf(ch_1,"%d",count);

			out = out + ch_1 + "\n";
			output<<out;
			continue;
		}

		for(long j = (A>10?A:10); j <= B; j++)
		{
			scores.clear();
			scores_circle.clear();
			long k = j;
			while(k > 0)
			{
				double m = double(long(k)%10);
				scores.push_back(k%10);
				k = (k-k%10)/10;
			}
			
			for(vector<long>::size_type ix = 0; ix != (scores.size() - 1); ++ix)
			{
				vector<long>::size_type sign = ix;
				long temp_totle = 0;
				sign_circle = 0;
				for(vector<long>::size_type iy = 0;iy != scores.size(); ++iy)
				{	
					temp_totle = temp_totle * 10 + scores[sign];
					sign = (sign+scores.size()-1)%scores.size();
				}
				if(!scores_circle.empty())
				{
					for(vector<long>::size_type iz = 0; iz != scores_circle.size() ; ++iz)
						if(temp_totle == scores_circle[iz])
							sign_circle = 1;
				}
				if(0 == sign_circle && temp_totle > j && temp_totle <= B)
				{
					count++;
					scores_circle.push_back(temp_totle);
				}
			}
		}

		char ch_1[20];
		sprintf(ch_1,"%ld",count);

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