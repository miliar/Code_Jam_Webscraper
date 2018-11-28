/* Program A : Alien Language
 * Programmer : Kumar Harsh
 * Date : 03 - September - 2009
 * Debugging and check commands are commented
 */

#include<iostream.h>
#include<fstream.h>
#include<ctype.h>
#include<string.h>
/*void sort(char**,int,int);*/
int find(char**,char**,int,int,int);
int main()
{
	ifstream fin ("A.in");
	ofstream fout ("A.out");
	int L,D,N;
	int i;
	char** lib, arg[4];
	fin>>arg;	L=atoi(arg);		// Number of letters = L
	fin>>arg;	D=atoi(arg);		// Number of lines   = D
	fin>>arg;	N=atoi(arg);		// Number of cases   = N
	cout<<L<<"\t"<<D<<"\t"<<N<<"\n";
	fin.read(arg,1);				// To get past the newline character

/* building a library of words */
	lib = new char*[D];
	for(i=0;i<D;i++)
	{
		lib[i]=new char[L+1];
		fin.getline(lib[i],L+1);
	}
	for(i=0;i<D;i++)
		cout<<lib[i]<<"\n";
/* build complete */

/* now build the test cases */
	char **set, *testcase,*key;
	int pos,elem,matches;

	set=new char*[L];
	testcase=new char[L*D];

	for(i=0;i<N;i++)
	{
		fin.getline(testcase,L*D);
		printf("\nTestcase %d : %s\n",i+1,testcase);
		pos=0;
		for(int j=0;j<strlen(testcase);j++)
		{
			elem=0;
			set[pos]=new char[L*D];
			 if(testcase[j]=='(')
			 {
				j++;
				do
				{
					set[pos][elem++]=testcase[j++];
				}while(testcase[j]!=')');
				set[pos][elem]='\0';
			 }
			 else
			 {
				set[pos][0]=testcase[j];
				set[pos][1]='\0';
			 }
			 cout<<set[pos]<<'\n';
			 pos++;
		}
		matches=find(lib,set,L,D,N);
		cout<<"Case #"<<i+1<<": "<<matches<<"\n";
		fout<<"Case #"<<i+1<<": "<<matches<<"\n";
	}
/* the indexing is done */

return 0;
}


int find(char** lib,char** set, int L,int D,int N)
{
	int found, match;
	int word, pos, elem;
	for(int word=0;word<D;word++)
	{
		match=0;
		for(pos=0;pos<L;pos++)
		{
			for(elem=0;elem<strlen(set[pos]);elem++)
			{
				if(lib[word][pos]==set[pos][elem])
				{
					match++;
					break;
				}
			}
		}
		if(match==L)
			found++;
	}
	return found;
}


/*void sort(char** lib,int d,int l)
{
	char* temp;
	temp=new char[l];
	for(int i=0;i<d;i++)
		for(int j=i;j<d-i-1;j++)
		{
			if(strcmp(lib[j],lib[j+1])==1)
			{
				strcpy(temp,lib[j]);
				strcpy(lib[j],lib[j+1]);
				strcpy(lib[j+1],temp);
			}
		}
}*/

