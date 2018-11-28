#include<fstream.h>

char** known;
int* possible;

int evaluate(char* str, int L, int D)
{

	int arrindex;
	int checkarr=0;
	int letterno=0;
	char c;
	char knownc;

	for(int index=0; str[index]!='\0'; index++)
	{
		char* arr;
		if(str[index]=='(')
		{ arrindex=0;
		  arr = new char[50]; //to hold possiible characters within brackets
		  checkarr=1;
		  while(str[++index]!=')')
		  { arr[arrindex++]=str[index];
		  }
		  arr[arrindex]='\0';

		}
		else
		{	c=str[index];
			checkarr=0;
		}

		for(int i=0; i<D; i++)
		{  if(!possible[i])
				continue;
			knownc=known[i][letterno];
			if(checkarr)
			{
			  for(int j=0; j<arrindex; j++)
			  { if(knownc == arr[j])
				 {	break;
				 }
			  }
			  if(j==arrindex)
				possible[i]=0;
			}
			else
			{  if(knownc!=c)
					possible[i]=0;
			}

		}
		if(checkarr)
			delete arr;

		for(int g=0; g<D; g++)    //all possible values are set to 0
			if(possible[g]==1)     //no point checking for other letters
				break;
		if(g==D)
			return 0;


		letterno++;
	}



	if(letterno<L)
		return 0;

	int possresult=0;
	for(int k=0; k<D; k++)
		if(possible[k])
			possresult++;

	return possresult;
}


void main()
{
	ifstream fin("C:\\Users\\Sau\\Desktop\\codejam\\input2.in");
	ofstream fout("C:\\Users\\Sau\\Desktop\\codejam\\output.txt");

	int L,D,N;
	fin>>L>>D>>N;

	//intialization of known strings

	known = new char*[D];
	possible = new int[D];    //will store indices of possible strings

	for(int i=0;i<D;i++)
		known[i]=new char[L];


	for(i=0; i<D; i++)
	{
		fin>>known[i];
	}


	char* str;

	int k=0;

	int cases;
	for(cases=0;cases<N;cases++)
	{  str=new char[500];
		fin>>str;

		for(i=0; i<D; i++)
		possible[i]=1; 		//intiallly all are possible

		k=evaluate(str,L,D);
		fout<<"Case #"<<(cases+1)<<": "<<k<<"\n";
		delete str;
	}


	fin.close();
	fout.close();
}