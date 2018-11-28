#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <limits.h>         //ULONG_MAX
#define  REP(a,b,c) for(a=b;a<=c;a++)
//variaveis especificas do problema

unsigned long long int max_linhas      =  3000;  //----->> Numero de linhas do arquivo de entrada
unsigned long long int max_caract      =  1100;  //----->> Numero de caracteres da maior linha do arquvio de entrada


//Variaveis Gerais

char lines[3000][1100];  //fazer lines[max_linas][max_caract];
long int line_counter,caso;
long int num_casos;
char file_path_in[]="C:\\Inputs\\B-large.in";
char file_path_out[]="C:\\Inputs\\B-large-solution.txt";
void read_input();
void write_output();
char *divide(int n,char divisor = ' ',char frase[] = lines[line_counter]);

//Funções
int maior_diff(int a, int b, int c);
int maior     (int a, int b, int c);
void construir();
//Variaveis Globais

int solucao[200];
int mcss[31];
int msss[31];

void case_solve ()
{
     int i,j,k,N,S,p,sol;
	 int in[200];

	 N = atoi(divide(1));
	 S = atoi(divide(2));
	 p = atoi(divide(3));
	 for(i=1;i<=N;i++) in[i] = atoi(divide(i+3));
	 line_counter++;
	 
	 sol = 0;
	 for(i=1;i<=N;i++)
	 {
		 if(msss[in[i]]>=p) sol++;
	 }
	 for(i=1;i<=N;i++)
	 {
		 if(S==0) break;
		 if(  (mcss[in[i]]>=p) && (msss[in[i]]<p)  ) 
		 {
			 sol++;
			 S--;
		 }
	 }

	 solucao[caso] = sol;
}

int maior_diff(int a, int b, int c)
{
		int ret,x;
		ret = 0;
		if(a>b)   x = a-b;
		else      x = b-a;
		if(x>ret) ret = x;
		if(a>c)   x = a-c;
		else      x = c-a;
		if(x>ret) ret = x;
		if(c>b)   x = c-b;
		else      x = b-c;
		if(x>ret) ret = x;

		return ret;
}

int maior     (int a, int b, int c)
{
    int ret;
	ret = a;
	if(b>ret) ret = b;
	if(c>ret) ret = c;
	return ret;
}
void construir()
{
   int i,j,k,soma,aux,aux2;

   for(i=0;i<=30;i++) mcss[i] = 0;
   for(i=0;i<=30;i++) msss[i] = 0;
   for(i=0;i<=10;i++)
   {
	   for(j=0;j<=10;j++)
	   {
		   for(k=0;k<=10;k++)
		   {
			   aux = maior_diff(i,j,k);
			   if(aux>2) continue;
			   aux2 = maior(i,j,k);
			   if(aux>1)
			   {
				  if(aux2 > mcss[i+j+k])    mcss[i+j+k] = aux2;
				  continue;
			   }
			   if   (aux2 > msss[i+j+k])    msss[i+j+k] = aux2;
		   }
	   }
   }
}
int main()
{
    construir();
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
char *divide(int n,char divisor,char frase[])
	{
	static char retbuf[200];
	int i,j,k,div[1000];

	j=1;
	div[0]=-1;
	k= strlen(frase);
	for(i=0;i <= strlen(frase)-1;i++) if(frase[i]==divisor)
	{
        if (j==1000)
		{
           printf("\n\n Na funcao DIVIDE --> vetor div muito pequeno. \n\n");
		   while(true);
		}
		div[j]=i;
		j++;
	}
	div[j]=strlen(frase);
	if(n>j)
	{
       printf("\n\n Na funcao DIVIDE --> valor de n muito grande. \n\n");
	   while(true);
	}
    for(i=0;i<=199;i++) retbuf[i]='\0';
    j=div[n-1]+1;
	k=div[n]-1;
	if((k-j+1)>200) 
	{
       printf("\n\n Na funcao DIVIDE --> vetor retbuf muito pequeno. \n\n");
	   while(true);
	}
	for(i=j;i<=k;i++) retbuf[i-j] = frase[i];
	return retbuf;
	}




