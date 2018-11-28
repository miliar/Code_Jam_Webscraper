#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <fstream>
#include <iostream>

using namespace std;

struct case_list
{
	long int N;
	long int K;
	bool Res;
	struct case_list *next;
} ;

int main(int argc, char* argv[])
{
	ifstream ifs(argv[1], ifstream::in);
	char nlc[7];
	ifs.getline(nlc,6);
	long int num_cases = strtol(nlc,NULL,0);
	int i=1;
	struct case_list *itr = NULL, *first = NULL;
	while(i<=num_cases)
	{
		string inp;
		bool flag = false;
		struct case_list *temp = (struct case_list*) malloc(sizeof(struct case_list));
		if(itr == NULL)
		{
			itr = temp;
			first = temp;
		}
		else
		{
			itr->next = temp;
			itr = temp;
		}
		itr->next = NULL;
		getline(ifs, inp,' ');
		temp->N = strtol(inp.c_str(), NULL, 0);

		getline(ifs,inp,'\n');
		temp->K = strtol(inp.c_str(),NULL,0);
		temp->Res = false;
		temp->next = NULL;
//		printf("case# %d: %d %d\n", i, temp->N, temp->K);
		i++;
	}
	itr = first;
	for(int j=1; j<=num_cases; j++)
	{
		long int N = itr->N;
		long int K = itr->K;
		for(i=1;;i++)
		{
			int val=(pow(2,N)*i) - 1;
			if(val == K)
			{
				itr->Res = true;
				break;
			}
			else if (val > K)
				break;
		}
		printf("Case #%d: %s\n", j, itr->Res ? "ON" : "OFF");
		itr = itr->next;
	}
	ifs.close();
}
