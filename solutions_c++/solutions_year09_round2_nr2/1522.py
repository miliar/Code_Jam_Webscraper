#include<fstream.h>

int isNew(char k, char n[], int count)
{
	for(int i=0; i<count; i++)
		if(k==n[i])
		 return 0;

	return 1;
}

void sort(char d[], digcount)
{
	 for(int i=0; i<digcount; i++)
	 { for(int j=0; j< digcount-1; j++)
		{ if(d[j]>d[j+1])
		  { char temp = d[j];
			 d[j]= d[j+1];
			 d[j+1] = temp;
		  }
		}
	 }
}

int findRep(char n[], int index)
{  char curr = n[index];
	int repindex =-1;
	int minreplace = 100;
	for(int i=index+1; i<ncount; i++)
	{
		if(n[i]>curr && n[i]<minreplace)
			repindex = i;
	}
	return repindex;
}

void revrswithzero(char n[], int ncount)
{
	char * rev = new char[ncount+1];

	rev[0] = n[ncount-1];
	rev[1] = 0+'0';

	for(int i=2; i<=ncount; i++)
		rev[i] = n[ncount-i-1];

	rev[i]='\0';

	i=0;
	do
	{ n[i] = rev[i];
	  i++;
	}while(rev[i]!='\0');
   n[i]='\0';
}

void evaluate(char n[], int ncount)
{  /*
	char *digits = new int[9];
	int digcount=0;
	for(int i=0; i<ncount; i++)
	{ char k = n[i];
	  if(isNew(k, digits, digcount))
		digits[digcount++] = k;

	}


	sort(digits, digcount);
	*/
	int repindex;
	char temp;
	for(i =ncount-2; i>=0; i--)
	{
		repindex = findRep(n, i, ncount);
		if(repindex!= -1)
		{
		temp = n[i];
		n[i] = n[repindex];
		n[repindex] = temp;
		break;
		}
	}
	if(i<0)
		revrswithzero(n, ncount);

	// digits;
}

void main()
{
	int T;
	char N[22];
	ifstream fin("C:\\Users\\Sau\\Desktop\\codejam\\inpnum.txt");
	ofstream fout("C:\\Users\\Sau\\Desktop\\codejam\\oupnum.txt");

	fin>>T;
	fin.getline(N,5);

	for(int i=0; i<T; i++)
	{
		fin.getline(N,21);
		int dig = fin.gcount()-1;
		evaluate(N, next, dig);
		fout<<"Case #"<<(i+1)<<": "<<N<<"\n";
	}
}