
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



#define DATAINPUT_TEST  "..\\resource\\magicka_test.in"
#define DATAINPUT_SMALL  "..\\resource\\magicka_small.in"
#define DATAINPUT_LARGE  "..\\resource\\magicka_large.in"
#define DATAOUTPUT_TEST "..\\resource\\magicka_test.out"
#define DATAOUTPUT_SMALL "..\\resource\\magicka_small.out"
#define DATAOUTPUT_LARGE "..\\resource\\magicka_large.out"

#define DATAINPUT  DATAINPUT_SMALL
#define DATAOUTPUT DATAOUTPUT_SMALL



typedef struct 
{
  char c[26][26];
} eCombine_t;

typedef struct 
{
  int  n;
  char o[26];
} eOpposed_t;




int main()
{
  FILE  *input,             // Ponteiro para arquivo de entrada de dados
        *output;            // Ponteiro para arquivo de saida do resultado
  
  char    *tokenContext,      // Contexto de identificacao de tokens por delimitador
          inputBuffer[1024];   // Buffer de leitura linha a linha
  
  int   casesInput,         // Numero de casos especificado pelo problema
        casesCounter;       // Numero do caso em analise



  // Tela de Apresentacao 
  printf("Code Jam - Qualification Round 2011\n");
  printf("B. Magicka\n\n");

  // Abrir o arquivo de entrada de dados
  if(fopen_s(&input, DATAINPUT, "r") != 0)
  {
    printf("Falha ao abrir o Arquivo de Input:\n\'%s\'\n\nImpossivel continuar.\n\n", DATAINPUT);
    getchar();
    return 1;
  }

  // Testa a leitura no arquivo de entrada de dados e, caso tenha sucesso, recolhe a quantidade de casos disponiveis no arquivo
  if(fgets(inputBuffer, (int) sizeof(inputBuffer), input) == NULL)
  {
    printf("Falha ao ler a Primeira linha do Arquivo de Entrada de Dados:\n\'%s\'\n\nImpossivel continuar.\n\n", DATAINPUT);
    getchar();
    return 1;
  }
  casesInput = atoi(inputBuffer);
  casesCounter = 0;

  // Cria o arquivo de saida do resultado
  if(fopen_s(&output, DATAOUTPUT, "w") != 0)
  {
    printf("Falha ao criar o Arquivo de Saida do Resultado:\n\'%s\'\n\nImpossivel continuar.\n\n", DATAOUTPUT);
    getchar();
    return 1;
  }
  fclose(output);

  // Abre o arquivo de saida do resultado para apppend
  if(fopen_s(&output, DATAOUTPUT, "a") != 0)
  {
    printf("Falha ao gravar o Caso #%d no Arquivo de Saida do Resultado:\n\'%s\'\n\nProcesso abortado.\n\n", casesCounter, DATAOUTPUT);
    fclose(input);
    getchar();
    return 1;
  }



  int  C;    // Numero de elementos que combinam
  char Ci[128];
  int  Cx;
  char eCombine[26][26];


  int D;
  char Di[128];
  int  Dx;
  char eOpposed[26][26];
 
  int N;
  int Ne[26];
  char Ni[128];
  char No[128];
  char Np;
  char Nn;
  int Nx;
  int Ny;
  int Nc;
  int Na;

  for(casesCounter = 1; fgets(inputBuffer, (int) sizeof(inputBuffer), input) != NULL; casesCounter++)
  {
    // Limpa lista de combinacoes
    for(C=0; C < 26; C++)
    {
      for(Cx=0; Cx < 26; Cx++)
        eCombine[C][Cx] = 0;
    }

    // Limpa lista de opostos
    for(D=0; D < 26; D++)
    {
      for(Dx=0; Dx < 26; Dx++)
        eOpposed[D][Dx] = 0;
    }


    // Limpa array de elementos presentes
    for(N=0; N < 26; N++)
      Ne[N] = 0;
   

    // Polula array combinacoes
     if((C  = atoi(strtok_s(inputBuffer, " ", &(tokenContext = NULL)))) > 0)
      strcpy_s(Ci, strtok_s(NULL, " ", &(tokenContext)));
    else
      strcpy_s(Ci, "");
    for(Cx = 0; Cx < C; Cx++)
    {
      eCombine[Ci[(Cx * 3)] - 65][Ci[(Cx * 3) + 1] - 65] = Ci[(Cx * 3) + 2];
      eCombine[Ci[(Cx * 3) + 1] - 65][Ci[(Cx * 3)] - 65] = Ci[(Cx * 3) + 2];
    }


    // Popula array de opostos
    if((D  = atoi(strtok_s(NULL, " ", &(tokenContext)))) > 0)
      strcpy_s(Di, strtok_s(NULL, " ", &(tokenContext)));
    else
      strcpy_s(Di, "");
    for(Dx = 0; Dx < D; Dx++)
    {
      eOpposed[Di[(Dx * 2)] - 65][Di[(Dx * 2) + 1] - 65] = 1;
      eOpposed[Di[(Dx * 2) + 1] - 65][Di[(Dx * 2)] - 65] = 1;
    }


    // Captura lista de entrada de elementos
    if((N  = atoi(strtok_s(NULL, " \n", &(tokenContext)))) > 0)
      strcpy_s(Ni, strtok_s(NULL, " \n", &(tokenContext)));
    else
      strcpy_s(Ni, "");

    
    Ny = 0;
    Np = 0;

    // Fire, Water, Arcane, Lightning, Arcane, Lightning! HELL YEAH!
    for(Nx = 0; Nx < N; Nx++)
    {
      Na = 0;
      if(Np == 0)
      {
        // Lista de elementos vazia. apenas adicione
        Nn = Ni[Nx];
        Ne[Ni[Nx] - 65]++;

        No[Np++] = Nn;
      }
      else
      {
        // Checa por combinacao
        Nc = Ni[Nx];
        for(Ny = Np-1; Ny >= 0; Ny--)
        {
          if((Nn = eCombine[No[Np - 1] - 65][Nc - 65]) == 0)
            break;
          
          Na = 1;

          Ne[No[Ny] - 65]--;
          Ne[Nn - 65]++;

          No[Ny] = Nn;
          Np = Ny+1;
        }

        if(Na==0)
        {
          Ne[Nc - 65]++;
          No[Np++] = Nc;

          for(Dx=0; Dx < 26; Dx++)
            if(eOpposed[Nc - 65][Dx] == 1)
              if(Ne[Dx] > 0)
              {
                Np = 0;
                for(Dx=0; Dx < 26; Dx++)
                  Ne[Dx] = 0;
                break;
              }
        }
        else
        {
          for(Dx=0; Dx < 26; Dx++)
            if(eOpposed[Nn - 65][Dx] == 1)
              if(Ne[Dx] > 0)
              {
                Np = 0;
                for(Dx=0; Dx < 26; Dx++)
                  Ne[Dx] = 0;
                break;

              }
        }
      }



    }


    // Resultado
    No[Np] = 0;

    fprintf(output, "Case #%d: [", casesCounter);
    for(Nx = 0; Nx < Np; Nx++)
      if(Nx == 0)
        fprintf(output, "%c", No[Nx]);
      else
        fprintf(output, ", %c", No[Nx]); 
    fprintf(output, "]\n");

  }

  // Salva e fecha o arquivo de output e fecha o arquivo de entrada de dados
  fclose(output);
  fclose(input);

  // Verifica se todos os casos foram analisados e apresenta a resposta
  if(casesInput == casesCounter - 1)
    printf("Finalizado.\n%d Casos processados.\nArquivo \'%s\' criado com sucesso.\n\n", casesCounter - 1, DATAOUTPUT);
  else
    printf("%d Casos processados, mas o Arquivo de entrada de dados informou haver %d.\nO Arquivo \'%s\' nao esta correto.\n\n", casesCounter - 1, casesInput, DATAOUTPUT);
  
	getchar();
	return 0;
  }
