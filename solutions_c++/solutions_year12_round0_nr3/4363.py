#include <iostream>
#include <fstream>
#include <stdio.h>
#include <math.h>
using namespace std;
int main()
{
	int cases;
	int t=1;
	FILE *fp;
    ifstream inFile;
	inFile.open("G:\\TopCoder\\2\\3\\C-small-attempt0.in");
	fp=fopen("g:\\out.out","w");
	inFile>>cases;
	while(cases--)
	{
		int i;
		int start,end;
		int count=0;
		char s1[]="Case #";
		fputs(s1,fp);
		fprintf(fp,   "%d",   t);
		fputc(':',fp);
		fputc(' ',fp);
		 inFile>>start>>end;
		cout<<"Case #"<<t<<": ";
	    int bit=0;
		int le=start;
		while(le)
		{
			le=le/10;
			bit++;
		}
		int j;
		for(i=start;i<=end;++i)
		{
			int key=i;
			int x=1;
		for(j=1;j<=bit-1;++j)
			{
               x=pow(10,j);
			   int y=key%x*pow(10,bit-j);
			   key=key/x;
			   y=key+y;
			   if(y>=start&&y<=end&&y>i)
			   {
				   count++;
			   }
			   key=i;
			}
			
			
		}
		cout<<endl;
		fprintf(fp,   "%d",  count);
		fputc('\n',fp);
		cout<<count<<endl;
		t++;
		
	}
	inFile.close();
	return 0;
}