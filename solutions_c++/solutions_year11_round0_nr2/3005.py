#include <stdio.h>
#include <string>

#define REP(i, n) for(i=0; i < n ; i++)

using namespace std;

unsigned int findoppose(char c1, int from, string target, int size, string oppose[])
{
	int i=0;
	REP(i, size)
	{
		if(oppose[i][0] == c1)
			return target.substr(0, from).find(oppose[i][1]);
		if(oppose[i][1] == c1)
			return target.substr(0, from).find(oppose[i][0]);
	}
	return string::npos;
};

char combinefc(char c1, char c2, int size, string combine[])
{
	int i = 0;
	REP(i , size)
	{
		if(combine[i][0] == c1)
			if(combine[i][1] == c2)
				return combine[i][2];
		if(combine[i][1] == c1)
			if(combine[i][0] == c2)
				return combine[i][2];
	}
	return 0;
}


int main()
{
	int T, C, D, N, i, j;
	string str;
	FILE *iFile, *oFile;
	iFile = fopen("B-small-attempt0.in", "r+");
	oFile = fopen("output.out", "w+");
	fscanf(iFile, "%d", &T);
	REP(i, T)
	{
		string combine[37], oppose[29], list="";
		fscanf(iFile, "%d", &C);
		REP(j, C)
		{
			char temp[4];
			fscanf(iFile, "%s", temp);
			combine[j] = temp;
		}
		fscanf(iFile, "%d", &D);
		REP(j, D)
		{
			char temp[3];
			fscanf(iFile, "%s", temp);
			oppose[j] = temp;
		}
		fscanf(iFile, "%d", &N);
		char temp[N];
		fscanf(iFile, "%s", temp);
		str = temp;
		j=0;
		for(j=0; j < N; j++)
		{
			if(str.length() == 1) 
			{
				list = str;
				break;
			}
			if(findoppose(str[j], j+1, list, D, oppose) != string::npos)
			{
				list.clear();
				continue;
			}
			if(combinefc(str[j], str[j+1], C, combine))
			{
				list.append(1, combinefc(str[j], str[j+1], C, combine));
				j++;
			}
			else
			{
				list.append(1, str[j]);
			}
		}
		fprintf(oFile, "Case #%d: [", i+1);
		if(list.length() > 0)
		{
			int k;
			REP(k, list.length())
			{
				fprintf(oFile, "%c", list[k]);
				if(k != list.length()-1)
				{
					fprintf(oFile, ", ");
				}
			}
		}
		fprintf(oFile, "]\n");
	}
	return 0;  
}