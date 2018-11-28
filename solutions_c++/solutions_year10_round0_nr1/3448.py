/*The code is in C++*/

#include<iostream.h>
#include<fstream.h>
#include<stdlib.h>


#define FILE_IN "A-small-attempt0.in"
const char *FILENAME = "myfile.txt";


main()
{
int a=0;
int f=0,q=0;
int N,K;

ifstream input;
ofstream fout(FILENAME);
input.open(FILE_IN,ios::in|ios::nocreate);

	if(!input)
	{
		cout<<endl<<"The file couldn't be found";
		exit(1);
	}

	
	input>>q;
	
	for(int i=1;i<=q;++i)
	{
		
		input>>N>>K;
		
        a=1<<N;
        if(K==(a-1))
        f=1;
        else if((K>a) && ((K%a)==(a-1)))
        f=1;
        if(f==1)
        fout<<"Case #"<<i<<":"<<" ON\n";
        else
        fout<<"Case #"<<i<<":"<<" OFF\n";
		f=0;
    }
	input.close();
	fout.close();
 return 0;
}  
