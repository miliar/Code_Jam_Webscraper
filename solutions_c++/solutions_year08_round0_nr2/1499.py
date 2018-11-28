#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;

int main ()
{

	ifstream myfile;
	ofstream outfile;
	myfile.open("sample.txt");
	outfile.open("output.txt");

	int i,j,k,l,t1,t2,t3,t4,tot;

	char Time[10];
	
	int N,T,NA,NB;

	int listA[200],listB[200],na,nb,valA[200],valB[200],ta,tb;


	myfile>>N;

	for(i=0;i<N;i++)
	{
		myfile>>T;
		myfile>>NA>>NB;
		
		for(j=0;j<NA;j++)
		{
			myfile>>Time;
			t1=Time[0]; t2=Time[1];
			t3=Time[3]; t4=Time[4];

			t1-=48; t2-=48; t3-=48; t4-=48;
			
			listA[j]= 60*(10*t1 + t2) + (10*t3 + t4);
			valA[j]=-1;

			myfile>>Time;
			t1=Time[0]; t2=Time[1];
			t3=Time[3]; t4=Time[4];

			t1-=48; t2-=48; t3-=48; t4-=48;
			
			listB[j]= 60*(10*t1 + t2) + (10*t3 + t4) + T;
			valB[j]=1;
		}


		for(j=0;j<NB;j++)
		{
			k=j+NA;

			myfile>>Time;
			t1=Time[0]; t2=Time[1];
			t3=Time[3]; t4=Time[4];

			t1-=48; t2-=48; t3-=48; t4-=48;
			
			listB[k]= 60*(10*t1 + t2) + (10*t3 + t4);
			valB[k]=-1;

			myfile>>Time;
			t1=Time[0]; t2=Time[1];
			t3=Time[3]; t4=Time[4];

			t1-=48; t2-=48; t3-=48; t4-=48;
			
			listA[k]= 60*(10*t1 + t2) + (10*t3 + t4) + T;
			valA[k]=1;
		}
	
	
		tot=NA+NB;

		
		for(j=tot;j>1;j--)
		{
			l=0;
			for(k=1;k<j;k++)if((listA[k]>listA[l]) ||( (listA[k]==listA[l]) && (valA[k]<valA[l])) )l=k;
			
			t1=listA[l]; t2=valA[l];
			listA[l]=listA[j-1]; valA[l]=valA[j-1];
			listA[j-1]=t1; valA[j-1]=t2;
		}


		for(j=tot;j>1;j--)
		{
			l=0;
			for(k=1;k<j;k++)if((listB[k]>listB[l]) ||( (listB[k]==listB[l]) && (valB[k]<valB[l])) )l=k;
			
			t1=listB[l]; t2=valB[l];
			listB[l]=listB[j-1]; valB[l]=valB[j-1];
			listB[j-1]=t1; valB[j-1]=t2;
		}
		

		na=0; nb=0;
		ta=0; tb=0;


		for(j=0;j<tot;j++)
		{
			na+=valA[j]; nb+=valB[j];

			if(na==-1)
			{
				na=0; ta++;
			}


			if(nb==-1)
			{
				nb=0; tb++;
			}
		}




	outfile<<"Case #"<<i+1<<": "<<ta<<" "<<tb<<endl;









	}

	//for(l=0;l<tot;l++)
	//cout<<listA[l]<<"\t"<<valA[l]<<endl;


	//getch();




	myfile.close();
	outfile.close();
	
	return 0;

}