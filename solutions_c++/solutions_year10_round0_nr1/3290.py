#include <iostream>
#include <fstream>
#include <cstring>

int min_clicks(unsigned int N)
{
	unsigned int min_click=0;
	while(N>1)
	{
		return min_click += (min_clicks(N-1)*2)+1;
	}
	return 1;
}

bool snapper(unsigned int N /*No of snapper devices */, unsigned int K /*Number of snaps by hand*/)
{
	bool result=false;
	unsigned int K_min=0; //Min Number of clicks required to turn on light

	K_min=min_clicks(N);//(N*2)-1;

	if (K<K_min)
		result=false;
	else if(K==K_min)
		result=true;
	else if (K>K_min)
	{
		unsigned int temp=K-K_min;
		if((temp%(K_min+1))==0)
			result=true;
		else
			result=false;
	}

	return result;
}

int main()
{
	char * line=new char(50);
	char * line_part1=new char(25);
	char * line_part2=new char(25);
		
	std::fstream fileOp("A-large.in",std::ios::in);
	std::fstream output("A-large.out",std::ios::out);
	fileOp.getline(line,100);
	int numofInputs=atoi(line);

	for(int i=1;i<=numofInputs;i++)
	{
		memset(line,0,49);
		fileOp.getline(line,100);
		int ctr=0;
		int len=strlen(line);
				
		memset(line_part1,0,24);

		while(*(line+ctr) != ' ')
		{
			*(line_part1+ctr)=*(line+ctr);
			ctr++;
		}

		ctr++;
		int ctr1=0;

		memset(line_part2,0,24);
		while(ctr<len)
		{
			*(line_part2+ctr1)=*(line+ctr);
			ctr++;
			ctr1++;
		}

		unsigned int N=atoi(line_part1);
		unsigned int K=atoi(line_part2);

		bool result=snapper(N,K);
		std::string str;

		char *res=(result)?"ON":"OFF";

		output<<"Case #"<<i<<": "<<res<<'\n';

	}
	fileOp.close();
	output.close();
	system("PAUSE");
}