#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <limits.h>         //ULONG_MAX
//variaveis especificas do problema

unsigned long long int max_linhas      =  3000;  //----->> Numero de linhas do arquivo de entrada
unsigned long long int max_caract      =  500;  //----->> Numero de caracteres da maior linha do arquvio de entrada


//Variaveis Gerais

char lines[3000][500];  //fazer lines[max_linas][max_caract];
long int line_counter,caso;
long int num_casos;
char file_path_in[]="C:\\Inputs\\A-small-attempt2.in";
char file_path_out[]="C:\\Inputs\\A-small-solution2.txt";
void read_input();
void write_output();
char *divide(int n,char divisor = ' ',char frase[] = lines[line_counter]);

//Funções


//Variaveis Globais

char solucao[50][500];
char in1[100] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
char in2[100] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char in3[100] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
char out1[100] = "our language is impossible to understand";
char out2[100] = "there are twenty six factorial possibilities";
char out3[100] = "so it is okay if you want to just give up";
char traduzido[50]; 

void case_solve ()
{
     int i,j,k;
	 char in[500],out[500];

	 for(i=0;i<=499;i++) out[i] = '\0';
	 strcpy(&in[0],&lines[line_counter][0]);
	 line_counter++;
	 for(i=0;i<=strlen(&in[0]);i++)
	 {
		 if(in[i]==' ')
		 {
			 out[i]=' ';
			 continue;
		 }
		 j = in[i];
		 out[i] = traduzido[j-97];
	}
	strcpy(&solucao[caso][0],&out[0]);
}

void traduzir()
{
     int i,j; 

	 for(i=0;i<=strlen(&in1[0]);i++)
	 {
		 if(in1[i]==' ') continue;
         j = in1[i]-97;
		 traduzido[j] = out1[i];
	 }

	 for(i=0;i<=strlen(&in2[0]);i++)
	 {
		 if(in2[i]==' ') continue;
         j = in2[i]-97;
		 traduzido[j] = out2[i];
	 }

	 for(i=0;i<=strlen(&in3[0]);i++)
	 {
		 if(in3[i]==' ') continue;
         j = in3[i]-97;
		 traduzido[j] = out3[i];
	 }

	 j = 'q' - 97;
	 traduzido[j] = 'z';
	 j = 'z' - 97;
	 traduzido[j] = 'q';
}

int main()
{
    read_input();
	traduzir();
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
        printf(solucao[caso]); // acrescenta essa parte na resposta
		printf("\n");
        
        caso++;
    }  
    freopen(file_path_out, "w",stdout);
    caso=1;
    while(caso!=num_casos+1)
    {  
        //Configuração da linha de saída
        printf("Case #");
        printf("%d: ",caso);
        printf(solucao[caso]); // acrescenta essa parte na resposta
		printf("\n");
        
        caso++;
    } 
}
char *divide(int n,char divisor,char frase[])
	{
	static char retbuf[200];
	int i,j,k,div[100];

	j=1;
	div[0]=-1;
	k= strlen(frase);
	for(i=0;i <= strlen(frase)-1;i++) if(frase[i]==divisor)
	{
        if (j==100)
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




