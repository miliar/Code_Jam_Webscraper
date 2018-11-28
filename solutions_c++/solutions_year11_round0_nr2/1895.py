#include <fstream>
#include <string>
using namespace std;
ifstream fin("large_case.in");
ofstream fout("large_case.out");
char combine[37][4];
char opposed[29][3];
char result;
bool combineChar(char cA,char cB)
{
	for (int i=0;i<37;i++)
	{
		if ((cA==combine[i][0]&&cB==combine[i][1])||(cB==combine[i][0]&&cA==combine[i][1]))
		{
			result=combine[i][2];
			return true;
		}
	}
	return false;
}
bool opposedChar2(char cA,char cB)
{
	for (int i=0;i<29;i++)
	{
		if ((cA==opposed[i][0]&&cB==opposed[i][1])||(cA==opposed[i][1]&&cB==opposed[i][0]))
		{
			result=' ';
			return true;
		}
	}
	return false;
}

int main()
{
	char inStr[100];
	char inChar;
	string inString;
	int total;
	int T,C,D,N;
	int i,j,k,m;
	fin>>T;
	for (i=0;i<T;i++)
	{
		fin>>C;
		for (j=0;j<C;j++)
		{
			for (m=0;m<3;m++)
			{
				fin>>combine[j][m];
			}
		}
		fin>>D;
		for (j=0;j<D;j++)
		{
			for (m=0;m<2;m++)
			{
				fin>>opposed[j][m];
			}
		}
		fin>>N;	
		total=0;
		fin>>inString;

		for (j=0;j<N;j++)
		{
			inChar=inString[j];
			if (total==0)
			{
				inStr[total]=inChar;
				total++;
			}
			else if (total==1)
			{
				if(combineChar(inStr[0],inChar))
				{
					total=0;
					inStr[total]=result;
					total++;
				}
				else if (opposedChar2(inStr[total-1],inChar))
				{
					total=0;
					inStr[total]=' ';
				}
				else
				{
					inStr[total]=inChar;
					total++;
				}
			}
			else if (total>1)
			{
				if (combineChar(inStr[total-1],inChar))
				{
					total--;
					inStr[total]=result;
					total++;
					inChar=result;
				}
				else
				{
					inStr[total]=inChar;
					total++;
				}
				for (k=0;k<total;k++)
				{
					  if (opposedChar2(inStr[k],inChar))
					  {
						  total=0;
						  break;
					  }			  
				}

			}

		}
		fout<<"Case #"<<i+1<<": [";
		for (k=0;k<total;k++)
		{

			fout<<inStr[k];
			if (k<total-1)
			{
				fout<<", ";
			}
		}
		fout<<"]"<<endl;
		for (j=0;j<C;j++)
		{
			for (m=0;m<3;m++)
			{
				combine[j][m]=' ';
			}
		}
		for (j=0;j<D;j++)
		{
			for (m=0;m<2;m++)
			{
				opposed[j][m]=' ';
			}
		}
	}
	return 0;
}

