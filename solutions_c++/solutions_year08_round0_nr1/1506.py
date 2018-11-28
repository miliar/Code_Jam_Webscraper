#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;

int main ()
{

	ifstream myfile;
	ofstream outfile;
	myfile.open("sub1.in");
	outfile.open("output.txt");

	int i,j,k,l;

	string line;

	char engine[100][200],query[2000][200];

	int N,S,Q,flag[100],totflag,Y;

	myfile>>N;

	for(i=0;i<N;i++)
	{
		myfile>>S; getline(myfile,line);
		for(j=0;j<S;j++)
		{	
			getline(myfile,line);
			strcpy(engine[j],line.c_str());
		}
		myfile>>Q; getline(myfile,line);
		for(j=0;j<Q;j++)
		{	
			getline(myfile,line);
			strcpy(query[j],line.c_str());
		}


	
		for(j=0;j<S;j++)flag[j]=0;
		totflag=0;

		Y=0;

		for(j=0;j<Q;j++)
		{

			for(k=0;k<S;k++)
			{
				if((strcmp(query[j],engine[k])==0) && (flag[k]==0))
				{
					flag[k]=1;
					totflag++;
					break;
				}
			}

			
			if(totflag==S)
			{
				totflag=1;
				for(l=0;l<S;l++)flag[l]=0;
				flag[k]=1;
				Y++;
			}

			//cout<<j<<":"<<query[j]<<" -> "<<Y<<endl;

		}

		outfile<<"Case #"<<i+1<<": "<<Y<<endl;


  

	}



	//getch();




	myfile.close();
	outfile.close();
	
	return 0;

}