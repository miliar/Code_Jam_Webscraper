#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

char buff[32768];
char permed_buff[32768];

typedef vector<int> t_ints;

void get_buff()
{
	buff[0]='\0';
	gets(buff);
	//printf("Got : %s\n",buff);
}

int get_num()
{
	get_buff();
	return atoi(buff);
}

int main(int argc, char* argv[])
{
	int T=get_num();

	for (int i=0 ; i<T ; ++i)
	{
		int k=get_num();
		t_ints perms;
		for (int j=0 ; j<k ; ++j)
            perms.push_back(j);

		get_buff();

		int min_res=INT_MAX;
		do {
			for (int j=0 ; buff[j*k]!=0 ; ++j)
				for (int l=0 ; l<k ; ++l)
					permed_buff[j*k+l]=buff[j*k+perms[l]];
			permed_buff[j*k]=0;
			char last=0;
			int res=0;
			for (int j=0 ; buff[j]!=0 ; ++j)
			{
				if (permed_buff[j]!=last)
				{
					++res;
					last=permed_buff[j];
				}
			}
			//printf("%s - %d\n",permed_buff,res);

			min_res=min(res,min_res);
		} while (next_permutation(perms.begin(),perms.end()));

		printf("Case #%d: %d\n",i+1,min_res);
	}

	return 0;
}

