#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <deque>


int main()
{

	char * inputsline=new char(50);
	char * linePathPresent=new char(25);
	char * LinePathToCreate=new char(25);

		
	std::fstream fileOp("A-large.in",std::ios::in);
	std::fstream output("A-large.out",std::ios::out);
	fileOp.getline(inputsline,50);
	int numofInputs=atoi(inputsline);

	for(int i=1;i<=numofInputs;i++)
	{
		memset(inputsline,0,49);
		fileOp.getline(inputsline,50);

		int numLines=atoi(inputsline);
		
			std::deque<int> VA1;
			std::deque<int> VB1;

		for(int j=0;j<numLines;j++)
		{
			memset(inputsline,0,49);
			fileOp.getline(inputsline,50);
			int len=strlen(inputsline);
			int nA1=0;
			int nB1=0;
			char * A1=new char(6);
			char * B1=new char(6);

			int ctr=0;
			while(ctr<len && *(inputsline+ctr) != ' ')
			{
				*(A1+ctr)=*(inputsline+ctr);
				ctr++;
			}

			int ctr1=0;
			while(ctr<len)
			{
				*(B1+ctr1)=*(inputsline+ctr);
				ctr++;
				ctr1++;
			}

			nA1=atoi(A1);
			nB1=atoi(B1);

			VA1.push_back(nA1);
			VB1.push_back(nB1);

		}

		//start calculating
		
		int tmpctr=VA1.size();
		int intrsction=0;
		while(tmpctr--)
			{
			int minIdx=0;

			for(unsigned int x=0;x<VA1.size();x++)
			{
				if(VA1[x]<VA1[minIdx])
					minIdx=x;
			}

			for(unsigned int x=0;x<VB1.size();x++)
			{
				if(VB1[x]<VB1[minIdx])
				{
					intrsction++;
				}
			}

			std::swap(VA1[minIdx],VA1[0]);
			std::swap(VB1[minIdx],VB1[0]);

			VA1.erase(VA1.begin());
			VB1.erase(VB1.begin());
		}
		output<<"Case #"<<i<<": "<<intrsction<<std::endl;
	}
	fileOp.close();
	output.close();
	system("PAUSE");
}