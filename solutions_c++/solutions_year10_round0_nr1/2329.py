#include <iostream.h>
#include <fstream.h>
#include <conio.h>
#include <stdio.h>
#include <math.h>
void main()
{
	int T;
	int N;
	long K,temp;
	bool on;
	char* infile="A-large.in";
	char* outfile="A-large.out";
	fstream fin;
	fstream	fout;
	fin.open(infile, ios::in);
	fout.open(outfile,ios::out);
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		fin>>N;
		fin>>K;
		on=false;
		if (	(N==1)	&&	((K%2)==1)	) {on=true;}
		else
		{
			temp=pow(2,N)-1;
			if (K==temp) on=true;
			if (	 (K>temp) && (  K%(temp+1) == temp	)	) on=true;
		}
		if(on) fout<<"Case #"<<i<<": ON";
		else fout<<"Case #"<<i<<": OFF";
		
		if(i<T) fout<<"\n";
	}
	
	fin.close();
	fout.close();

	
     
}
/*FILE *f1;
    f1=fopen("D:\\input.txt","rt");
                            
    if (f1!=NULL)
    {
         int ch=fgetc(f1); //lay ki tu cho vao ch
         while (! feof(f1))
         {
             cout<<"huhu";
			  break;                                                 
         }
         fclose(f1);
     }*/
    
