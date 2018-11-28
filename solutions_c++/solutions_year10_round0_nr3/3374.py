
#include <conio.h>
#include <iostream>
#include <queue>

#define INPUTF "C-small-attempt0.in"
#define OUTPUTF "C-small-attempt0.out"

using namespace std;


#define INPUTF "C-small-attempt1.in"
#define OUTPUTF "C-small-attempt1.out"


using namespace std;


__int64 Profit(__int64 times, __int64 capacity, __int64 ngroups, vector<__int64> &groups)
{
	__int64 prof = 0;
	__int64 j = 0;

	for(int i=0;i<times;i++)
	{
		__int64 cap = capacity;
		__int64 gr = 0;

		while((cap>0)&&(gr<ngroups))
		{
			cap-=groups[j];
			if(cap<0)
				break;
				
			prof+=groups[j];
			j = (++j)%ngroups;
			gr++;
		}
	}
	
	return prof;
}


int _tmain(int argc, _TCHAR* argv[])
{
	__int64 T;

	FILE *Input,*Output,*Output2;
	Input = fopen(INPUTF, "r");
	Output = fopen(OUTPUTF, "w");
//	Output2 = fopen(OUTPUTF2, "w");

	__int64 res, res2;
	vector<__int64> groups;

	fscanf(Input,"%lld",&T);

	for (int i=0;i<T;i++)
	{
		__int64 R = 1;
		__int64 k = 1;
		__int64 N = 1;

		fscanf(Input,"%lld%lld%lld",&R,&k,&N);
		
		for (int i=0;i<N;i++)
		{
			__int64 g = 0;
			fscanf(Input,"%lld%",&g);
			groups.push_back(g);
		}

		res = Profit(R,k,N,groups);
		groups.clear();

		if (i!=(T-1))
		{
			fprintf(Output,"Case #%d: %lld\n",i+1,res);
//			fprintf(Output2,"Case #%d: %s\n",i+1,res2.c_str());
		}
		else
		{
			fprintf(Output,"Case #%d: %lld\n",i+1,res);
//			fprintf(Output2,"Case #%d: %s",i+1,res2.c_str());
		}
	}

	fclose (Input);
	fclose (Output);
//	fclose (Output2);
	return 0;
}