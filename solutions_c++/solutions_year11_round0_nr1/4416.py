
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



#define DATAINPUT_TEST  "..\\resource\\botTrust_test.in"
#define DATAINPUT_SMALL  "..\\resource\\botTrust_small.in"
#define DATAINPUT_LARGE  "..\\resource\\botTrust_large.in"
#define DATAOUTPUT_TEST "..\\resource\\botTrust_test.out"
#define DATAOUTPUT_SMALL "..\\resource\\botTrust_small.out"
#define DATAOUTPUT_LARGE "..\\resource\\botTrust_large.out"

#define DATAINPUT  DATAINPUT_LARGE
#define DATAOUTPUT DATAOUTPUT_LARGE

int main()
{
  FILE  *input,             // Ponteiro para arquivo de entrada de dados
        *output;            // Ponteiro para arquivo de saida do resultado
  
    char  *tokenContext,      // Contexto de identificacao de tokens por delimitador
          inputBuffer[1024];   // Buffer de leitura linha a linha
  
  int   casesInput,         // Numero de casos especificado pelo problema
        casesCounter,       // Numero do caso em analise
        N,                  // Quantidade de Snappers ligados em serie
        Nt,
        K;                  // Quantidade de snaps

  int     O[100],
          B[100];
  char    S[100];


  int   P;
//  int  R;

  int Op;
  int Bp;
  int Sp;

  int Oy,
      By;

  int Ot,
      Bt;

  char t[2];
  long long time;

//  N = K = P = 0 ;

  // Tela de Apresentacao 
  printf("Code Jam - Qualification Round 2011\n");
  printf("A. Bot Trust\n\n");

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

  for(casesCounter = 1; fgets(inputBuffer, (int) sizeof(inputBuffer), input) != NULL; casesCounter++)
  {

    // Popula Array de interacoes     
Op = 0;
Bp = 0;
Sp = 0;
N = atoi(strtok_s(inputBuffer, " ", &(tokenContext = NULL)));

    for(Nt = N; Nt > 0;Nt--)
      if((S[Sp++] = *strtok_s(NULL, " ", &(tokenContext))) == 'O')
        O[Op++] = atoi(strtok_s(NULL, " ", &(tokenContext)));
      else
        B[Bp++] = atoi(strtok_s(NULL, " ", &(tokenContext)));

    O[Op] = 0; B[Bp] = 0; S[Sp] = 0;
    
    Op = Bp = Sp = 0;
    Ot = Bt = 0;
    Oy = By = 1;
    time = 0;

    Oy = 1;
    By = 1;
    while(S[Sp] != 0)
    {
      if(S[Sp] == 'O')
      {
        Oy += (Ot = O[Op] - Oy);
        if(Ot < 0) Ot *= -1;
        time += (Ot + 1);

        if((Bt = B[Bp] - By) < 0) Bt *= -1;
        if(Bt < (Ot + 1))
          By += B[Bp] - By;
        else
          if((Bt = B[Bp] - By) != 0)
            if(Bt < 0)
              By += ((Ot + 1) * -1);
            else
              By += Ot + 1;

        Op++;
      }
      else
      {
        By += (Bt = B[Bp] - By);
        if(Bt < 0) Bt *= -1;
        time += (Bt + 1);

        if((Ot = O[Op] - Oy) < 0) Ot *= -1;
        if(Ot < (Bt + 1))
          Oy += O[Op] - Oy;
        else
          if((Ot = O[Op] - Oy) != 0)
            if(Ot < 0)
              Oy += ((Bt + 1) * -1);
            else
              Oy += Bt + 1;
        Bp++;
      }

      Sp++;
    }
    
    fprintf(output, "Case #%d: %LLd\n", casesCounter, time);
  }

  // Salva e fecha o arquivo de output e fecha o arquivo de entrada de dados
  fclose(output);
  fclose(input);

  // Verifica se todos os casos foram analisados e apresenta a resposta
  if(casesInput == casesCounter - 1)
    printf("Finalizado.\n%d Casos processados.\nArquivo \'%s\' criado com sucesso.\n\n", casesCounter - 1, DATAOUTPUT);
  else
    printf("%d Casos processados, mas o Arquivo de entrada de dados informou haver %d.\nO Arquivo \'%s\' nao esta completo.\n\n", casesCounter - 1, casesInput, DATAOUTPUT);
  
	getchar();
	return 0;
  }
