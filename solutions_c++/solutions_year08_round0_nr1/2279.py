#include<stdio.h>
#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;


static sw=0;
void switching(int cases,char *query[],int q,char *engine[],int e)
{

		ofstream  t1;
	t1.open("D:\\googl\\output.txt",ifstream::app);


	/*cout<<"--------Noq---------"<<endl;
	for(int i=0;i<q;++i)
	{
		cout<<query[i]<<endl;

	}
	cout<<"--------Noe---------"<<endl;

	for( i=0;i<e;++i)
	{
		cout<<engine[i]<<endl;
	}
	*/
		int nos=0;//no of switch;
		int j=0;
		int temp=0,temp1=0;
		int nonend=0;

		int *eng=new int[e];
		int y=0;
	
		cout<<"------------------------"<<endl;
		cout<<"iteratin start"<<endl;
		cout<<"------------------------"<<endl;
		sw=0;

		for(int p=0;p<q;++p)
		{
			
			cout<<"y="<<y<<endl;

		for(int i=0;i<e;++i)
		{
			eng[i]=-1;
			for(int j=y;j<q;++j)
			{
				if(strcmp(engine[i],query[j])==0)
				{
					eng[i]=j-y;
				//	cout<<"intermediate measure"<<eng[i]<<endl;
					break;


				}
			}
		}

		cout<<"measures";
		for(i=0;i<e;++i)
		{
			cout<<"  "<<eng[i] <<"\t";
		}
		cout<<endl;


		    for(int h=0;h<e;++h)
			{
				if(eng[h]==-1)
				{
					nonend=0;
					break;
				}
				else
				{
					nonend=1;
					
				}

			}



			temp1=eng[0];


			
			for(int k=1;k<e;++k)
			{ 
				if(temp1<eng[k])
				{
					temp1=eng[k];
				}
			}
			
			
			cout<<"nonend"<<nonend<<endl;
			if(nonend==1)
			{
				sw++;
			//	cout<<"switchiug"<<sw<<endl;
			}
			else
			{
				break;
			}
		//	cout<<"maximum"<<temp<<endl;
			y+=temp1;
			

		}
			
		

		//cout<<"switching"<<sw<<endl;
		cout<<"Case #" <<cases<<": " <<sw<<endl;
		t1<<"Case #" <<cases<<": " <<sw<<endl;
		t1.close();
		/*
		for(int i=0;i<e;++i)
		{
			eng[i]=0;
			for(int j=0;j<q;++j)
			{
				if(strcmp(query[j],engine[i])==0)
				{
					eng[i]+=1;
				}
			}
		}

		for(i=0;i<e;++i)
		{
			cout<<"engine no  "<<i<<"  " <<eng[i] <<endl;
		}*/


		/*
		int count=eng[0];

		for(i=1;i<e;++i)
		{
			if(count>eng[i])
			{
				count=eng[i];
			}
		}

			if(count>0)
			{
			cout<<"Case #" <<cases<<": " <<count-1<<endl;
			t1<<"Case #" <<cases<<": " <<count-1<<endl;
			}
			else
			{
				cout<<"Case #" <<cases<<": " <<count<<endl;
			t1<<"Case #" <<cases<<": " <<count<<endl;
			}
			*/

			
	
		
		/*	
		for(int i=0;i<q;++i)
		{
			if(strcmp(query[i],engine[j])==0)
			{
				++nos;++j;
				//break;
				
			}
		}*/
		//cout<<"nos"<<nos<<endl;

}
void main()
{
	char red[1000];
	char *engine[1000];
	char *query[1000];
	ifstream  t;
	t.open("D:\\googl\\file.txt",ifstream::in);
	
	int nor,noe,noq;


	if(t!=NULL)
	{
			t.getline(red,100,'\n');
			nor=atoi(red);
			cout<<"no records"<<nor<<endl;

			


			for(int j=0;j<nor;++j)
			{

				t.getline(red,100,'\n');
				noe=atoi(red);
				cout<<"no of engine"<<noe<<endl;

				for(int i=0;i<noe;++i)
				{
					t.getline(red,100,'\n');
					engine[i]=new char[100];
					strcpy(engine[i],red);
					cout<<engine[i]<<endl;
				}
				
				
				t.getline(red,100,'\n');
				noq=atoi(red);
				cout<<"no of query"<<noq<<endl;


				for( i=0;i<noq;++i)
				{
					t.getline(red,100,'\n');
					query[i]=new char[100];
					strcpy(query[i],red);
					cout<<query[i]<<endl;
				}

					switching(j+1,query,noq,engine,noe);

				
			//	getch();		
		
			}




			/*
			
			for(int j=0;j<nor;++j)
			{
				
				cout<<"No of engines  " <<noe <<endl;
				for(int i=0;i<noe;++i)
				{
					t.getline(red,100,'\n');
					engine[i]=new char[100];
					strcpy(engine[i],red);
					cout<<engine[i]<<endl;
				}

				t.getline(red,100,'\n');
				int noq=atoi(red);
				cout<<endl<<"no of query"<<noq<<endl;

			//	cout<<"No of queries"<<endl;
				for( i=0;i<noq;++i)
				{
					t.getline(red,100,'\n');
					query[i]=new char[100];
					strcpy(query[i],red);
					cout<<query[i]<<endl;
				}

				
				cout<<"Noe"<<endl;
				for(i=0;i<noe;++i)
				{
					cout<<engine[i]<<endl;
				}
				cout<<endl;
				cout<<"Noq"<<endl;
				for(i=0;i<noq;++i)
				{
					cout<<query[i]<<endl;
				}

				switching(j,query,noq,engine,noe);

				cout<<endl;
				t.getline(red,100,'\n');
				int noe=atoi(red);
				

			}
*/
			


						
	
	
	
	}
	else
	{
		cout<<"file not found";
	}
	t.close();

}