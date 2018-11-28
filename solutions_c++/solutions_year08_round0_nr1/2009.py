
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#include <stdlib.h>
#define SS 100
#define QQ 1000
#define charlo 100

int cantidadswitch  (char query[QQ][charlo],char engine [SS][charlo],int S, int Q,int suiche,int pos, FILE *fichero,int i)
{
	int j,k,w,f;

	int recorrido[SS]={-1,-1,-1,-1,-1};
	int equal=0;
	

		   cout<<"\n COMIENZA OTRA VEZ \n";
		   fprintf(stdout,"SUICHE: %i.. POS: %i",suiche,pos);

	if(!(pos>Q))
	{

	for(w=0;w<S;w++)
	{
		equal=0;
		for(j=pos;j<Q;j++)
		{

			if (strcmp(engine[w],query[j])==0)
			{
				equal=1;
				recorrido[w]=j;
				cout<<recorrido[w]<<"::"<<"w"<<endl;
				break;
			}
			
		}
		if(equal==0)
		break;
		
	}
	cout<<"EQUAL:"<<equal<<endl;

	for(w=0;w<S;w++)
	cout<<recorrido[w]<<' ';

	cout<<endl;
	cout<<endl;
	//myfile.close();
	if(equal==0)
	{	

		
		if( fichero )
			  printf( "creado (ABIERTO)\n" );
		   else
		   {
			  printf( "Error (NO ABIERTO)\n" );
			  return 1;
		   }

		   fprintf(fichero,"Case #%i: %i \n",i+1,suiche);
			return 0;

		}
		else
		{
			int mayor=-1;
			for(f=0;f<S;f++)
			{
			if(recorrido[f]>mayor)
				mayor=recorrido[f];
			cout<<"MAYOR:"<<mayor<<"RECORRIDO"<<recorrido[f]<<endl;
			}
			cout<<"MAYOR:"<<mayor<<endl;
			suiche+=1;
			pos=mayor;

			cantidadswitch(query,engine,S,Q,suiche,pos,fichero,i);

		}
	}
	else
	{
		cout<<"NUMSUICHE:"<<suiche<<endl;
		fprintf(fichero,"Case #%i: %i \n",i+1,suiche);
		return -1;
	}
	return suiche;
}




int main()
{
	string line;
//	int * esta;
	int N;
	int S;//su tamaño es N
	int Q;//su tamaño es N
	char query [QQ][100];
	char engine [SS][100];
	int i,k,j,f,w;
	FILE *fichero;
	char nombre[11] = "prueba.txt";
	fichero = fopen( nombre, "w" );

	 ifstream myfile ("inpout.in");
	//getline();

	if (myfile.is_open())
	{
		getline(myfile,line);
		N=atoi(&line[0]);
		
		for(i=0;i<N;i++)
		{
			getline(myfile,line);
			S=atoi(&line[0]);
			for(k=0;k<S;k++)
			{
				f=0;
				getline(myfile,line);
				while(line[f]!='\0' && line[f]!='0' && line[f]!='\n')
				{
					engine[k][f]=line[f];
					cout<<engine[k][f]<<" ";
					f++;
				}
				engine[k][f]='\0';
				cout<<endl;
			}
			cout<<endl;
			getline(myfile,line);

			Q=atoi(&line[0]);
			
			for(k=0;k<Q;k++)
			{
				f=0;
				getline(myfile,line);
				while(line[f]!='\0' && line[f]!='0' && line[f]!='\n')
				{
					query[k][f]=line[f];
					cout<<query[k][f]<<" ";
					f++;
				}
				query[k][f]='\0';
				cout<<endl;
			}
			cantidadswitch(query,engine,S,Q,0,0,fichero,i);

		}
		cout<<endl;

		
	}




//	isalpha(*current)

return 1;
}
