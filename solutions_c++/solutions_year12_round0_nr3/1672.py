#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <limits.h>         //ULONG_MAX
//variaveis especificas do problema

unsigned long long int max_linhas      =  3000;  //----->> Numero de linhas do arquivo de entrada
unsigned long long int max_caract      =  110;  //----->> Numero de caracteres da maior linha do arquvio de entrada


//Variaveis Gerais

char lines[3000][110];  //fazer lines[max_linas][max_caract];
long int line_counter,caso;
long int num_casos;
char file_path_in[]="C:\\Inputs\\C-large.in";
char file_path_out[]="C:\\Inputs\\C-large-solution.txt";
void read_input();
void write_output();
char *divide(int n,char divisor = ' ',char frase[] = lines[line_counter]);

//Funções
void analise(int in);

//Variaveis Globais

int solucao[200];
int rec[6];

void case_solve ()
{
     int i,j,k,A,B,sol;
	 char *aux;

	 aux = strtok(lines[line_counter]," ");
	 A = atoi(aux);
	 aux = strtok(NULL," ");
	 B = atoi(aux);
	 line_counter++;

	 sol = 0;
	 for(i=A;i<=B;i++)
	 {
		 if(i<10) continue;
		 analise(i);
		 for(j=0;j<=5;j++)
		 {
			 if(rec[j]==0) continue;
			 k = rec[j];
			 if(  (k > i)  &&  (k <= B)  ) sol++;
		 }
	 }

	 solucao[caso] = sol;		
}

void analise(int in)
{
	int i,j,k,n,aux[7],out[7];

	for(i=0;i<=6;i++) aux[i] = 0;
	for(i=0;i<=6;i++)
	{
		aux[i] = in % 10;
		in -= aux[i];
		in /= 10;
	}
	for(i=6;i>=0;i--) 
	{
		if(aux[i]!=0)
		{
			n = i+1; // number of digits
			break;
		}
	}
	for(i=0;i<=5;i++) rec[i] = 0;
	for(i=0;i<=n-2;i++)
	{
		for(j=0;j<=6;j++) out[j] = 0;
		k = 0;
		for(j=i+1;j<=n-1;j++)
		{
            out[k] = aux[j];
			k++;
		}
		for(j=0;j<=i;j++)
		{
			out[k] = aux[j];
			k++;
		}
		k=1;
		for(j=0;j<=6;j++)
		{
			rec[i] += out[j] * k;
			k *= 10;
		}
	}
	for(i=0;i<=4;i++)
	{
		for(j=i+1;j<=5;j++)
		{
			if(rec[i]==rec[j]) rec[j] = 0;
		}
	}
}

int  main()
{
	read_input();
    caso=1;
    line_counter=2;
    num_casos=atol(lines[1]);
    while(true)
    {
           case_solve();
           printf("Caso %d   --->   OK ! \n\n",caso);
           caso++;
           if(caso==num_casos+1) break;   
    }
    write_output();
    getchar();
}

void read_input()
{
     // Quebra o arquivo em um vetor de strings, um string para cada linha.
     FILE *arq;
     unsigned long long int a,i; 
     
     
     printf("LENDO\n");
     arq=fopen(file_path_in,"r");
     a=1;
     if(arq)
     {
            while(true)
            {
                fgets(lines[a],max_caract,arq);
                //printf(lines[a]);
                //getchar();
                i=0;
                while(true)
                {
                   if((lines[a][i]=='\n')||(lines[a][i]=='\0')) break;
                   i++;
                   if(i==max_caract-3)
                   {
                      printf("\n\n Verificar maximo de caracteres \n\n");
                      while(true);                 
                   }        
                }
                if(feof(arq)) break;
                a++;
                if(a==max_linhas)
                {
                   printf("\n\n Verificar maximo de linhas \n\n");
                   while(true);                 
                }
            }
     }
}
void write_output()
{
    printf("ESCREVENDO\n\n");   
    caso=1;
    while(caso!=num_casos+1)
    {  
        //Configuração da linha de saída
        printf("Case #");
        printf("%d: ",caso);
        printf("%d \n",solucao[caso]); // acrescenta essa parte na resposta
        
        caso++;
    }  
    freopen(file_path_out, "w",stdout);
    caso=1;
    while(caso!=num_casos+1)
    {  
        //Configuração da linha de saída
        printf("Case #");
        printf("%d: ",caso);
        printf("%d \n",solucao[caso]); // acrescenta essa parte na resposta
        
        caso++;
    } 
}
