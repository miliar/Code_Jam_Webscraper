
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
#include <ctype.h>
#include <stdio.h>
#define sizen 100

void imprimir(long int vector[sizen][2],int size);

void ordenar (long int vector[sizen][2], int size)
{
	long int aux[1][2];
	int i,j;
	for(i=0;i<size;i++)
	{
		for(j=0;j<size;j++)
		{
			if(vector[j][0]>vector[i][0])
			{
				aux[0][0]=vector[j][0];
				aux[0][1]=vector[j][1];
				vector[j][0]=vector[i][0];
				vector[j][1]=vector[i][1];
				vector[i][0]=aux[0][0];
				vector[i][1]=aux[0][1];
			}
		}
		
	}
	cout<<"IMPRESION EN ORDENAR:\n";
		imprimir(vector,size);

}

void imprimir(long int vector[sizen][2], int size)
{
	int i,j;
	for(i=0;i<size;i++)
	{
		cout<<"|";
		for(j=0;j<2;j++)
		{
			cout<<((vector[i][j])/6)*10<<" ";
		}
		cout<<"|"<<endl;
	}
	cout<<endl;
}


void main()
{
	
	string line;
	long int NB[sizen][2], NA [sizen][2];
	int N, T,na,nb,isablea[sizen],isableb[sizen];
	int i,j,k,f,w,trena,trenb,flag,contador,contaux;
	FILE *fichero;
	char nombre[11] = "prueba.txt";
	fichero = fopen( nombre, "w" );


	ifstream myfile ("input.in");
	if (myfile.is_open())
	{
		getline(myfile,line);
		N=atoi(&line[0]);
		cout<<N<<endl;
		for(i=0;i<N;i++)
		{
			cout<<"OEEEEEE";
			getline(myfile,line);
			T=atoi(&line[0]);
			cout<<T<<endl;
			getline(myfile,line);
			na=atoi(&line[0]);
			cout<<na<<" ";
			nb=atoi(&line[2]);
			cout<<nb<<endl;
			for(f=0;f<na;f++)
				isablea[f]=1;
			for(f=0;f<nb;f++)
				isableb[f]=1;

			for(f=0;f<na;f++)
			{
		//		cout<<"ENTRE AL FOR QUE HACE NA";
				j=0;
				getline(myfile,line);
				w=0;
				if(isspace(line[w]))
				w++;
				for(k=0;k<2;k++)
				{

	/*				do
					{
			//			cout<<"estoy en while a ver si es digit";
						 w++;
						 if(w>9)
						 {
							 getline(myfile,line);
							 w=-1;
							 f++;
							cout<<"REINICIO DE K";

						 }
						 cout<<"que mierda NA";
					}while(!isdigit(line[w]));*/
				//	cout<<"el valor de w es:"<<w<<endl;
				//	cout<<line[w]<<" "<<line[w+1]<<" "<<line[w+2]<<" "<<line[w+3]<<" "<<line[w+4]<<" "<<line[w+5]<<endl;
					NA[f][k]= atoi(&line[w])*60+atoi(&line[w+3]);
					w=w+6;
					//cout<<NA[f][k]<<" ";
				}
				cout<<endl;
			}
			for(f=0;f<nb;f++)
			{
				
				getline(myfile,line);
				w=0;
				if(isspace(line[w]))
				w++;

				for(k=0;k<2;k++)
				{

				/*	do
					{
						 w++;
						 if(w>9)
						 {
							 getline(myfile,line);
							 w=-1;
							 f++;

							cout<<"que mierda";
						 }
					}while(!isdigit(line[w]));*/
			//		cout<<"el valor de w es:"<<w<<endl;
			//		cout<<line[w]<<" "<<line[w+1]<<" "<<line[w+2]<<" "<<line[w+3]<<" "<<line[w+4]<<" "<<line[w+5]<<endl;

					NB[f][k]= atoi(&line[w])*60+atoi(&line[w+3]);
					//cout<<NB[f][k]<<" ";
					w=w+6;;
				}
				cout<<endl;
			}
			ordenar(NA,na);
			ordenar(NB,nb);
			trena=0;
			trenb=0;
			contador=0;
			contaux=10;
			for(j=0;j<na;j++)
			{
				flag=0;
				for(k=0;k<nb;k++)
				{
					if(contador==contaux)
					{
						if(NA[j][0]<(NB[k][0]))
							break;
						else contaux+=10;
					}
					if(NA[j][0]>=(NB[k][1]+T) && isableb[k])
					{
						flag=1;
						isableb[k]=0;
						break;
					}
					contador++;

				}
				if(!flag)
					trena+=1;
			}
			for(j=0;j<nb;j++)
			{
				flag=0;
				for(k=0;k<na;k++)
				{
					if(contador==contaux)
					{
						if(NB[j][0]<(NA[k][0]))
							break;
						else contaux+=10;
					}
					if(NB[j][0]>=(NA[k][1]+T) && isablea[k])
					{
						flag=1;
						isablea[k]=0;
						break;
					}
					contador++;

				}
				if(!flag)
					trenb+=1;
			}
			cout<<"Case #"<<i+1<<": "<<trena<<" "<<trenb<<endl;
			if( fichero )
			  printf( "creado (ABIERTO)\n" );
		   else
		   {
			  printf( "Error (NO ABIERTO)\n" );
		   }
			imprimir(NA,na);
			imprimir(NB,nb);
		   fprintf(fichero,"Case #%i: %i %i \n",i+1,trena,trenb);

		}
	}

}