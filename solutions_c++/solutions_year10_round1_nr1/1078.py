#include<stdio.h>
#include<conio.h>
#include<windows.h>
#include<process.h>
#include<time.h>

//Input structure
typedef struct task_input{
  char table[50][50];          
  int N,K,result;  
}task_input;


////
//SOLVING ALGORITHM
////
void rotate(task_input &input){
  char tmpTable[50][50];
  for(int x=0;x<input.N;x++){
    for(int y=0;y<input.N;y++){
      tmpTable[y][x]=input.table[x][y];
    }
  }
  
  for(int x=0;x<input.N;x++){
    for(int y=0;y<input.N;y++){
      input.table[input.N-x-1][y]=tmpTable[x][y];
    }
  }    
}

void gravity(task_input &input){
  int swap=0,y;
  for(int x=0;x<input.N;x++){
    swap=1;
    while(swap==1){
      swap=0;
      for(y=input.N-1;y>0;y--){
        if((input.table[x][y]=='.' && input.table[x][y-1]!='.') ||swap){
          input.table[x][y]=input.table[x][y-1];
          swap=1;
        }
      }
      if(swap==1){
       input.table[x][y]='.';
      }

    }          
  }
}

int getResultHorizontal(task_input &input){
  int red=0,blue=0;
  int result=0;
  for(int y=0;y<input.N;y++){
    red=0;
    blue=0;
    for(int x=0;x<input.N;x++){
      if(input.table[x][y]=='R'){
        red++;
        blue=0;
      }
      if(input.table[x][y]=='B'){
        blue++;
        red=0;
      }
      if(input.table[x][y]!='B' && input.table[x][y]!='R'){
        red=0;
        blue=0;                          
      }
      if(red==input.K)
        result=result|1;
      if(blue==input.K)
        result=result|2;
    }
  }
  return result;
}

int getResultVerticaly(task_input &input){
  int red=0,blue=0;
  int result=0;
  for(int x=0;x<input.N;x++){
    red=0;
    blue=0;
    for(int y=0;y<input.N;y++){
      if(input.table[x][y]=='R'){
        red++;
        blue=0;
      }
      if(input.table[x][y]=='B'){
        blue++;
        red=0;
      }
      if(input.table[x][y]!='B' && input.table[x][y]!='R'){
        red=0;
        blue=0;                          
      }
      if(red==input.K)
        result=result|1;
      if(blue==input.K)
        result=result|2;
    }
  }
  return result;
}

int getResultDiagonaly(task_input &input){
  int red=0,blue=0;
  int result=0,x,y,xR,yR;
  
  
  //X-line ->
  for(xR=0;xR<input.N;xR++){
    red=0;
    blue=0;
    y=input.N-1;
    x=xR;
    while(x<input.N && y>=0 && x>=0 && y<input.N){
      if(input.table[x][y]=='R'){
        red++;
        blue=0;
      }
      if(input.table[x][y]=='B'){
        blue++;
        red=0;
      }
      if(input.table[x][y]!='B' && input.table[x][y]!='R'){
        red=0;
        blue=0;                          
      }
      if(red==input.K)
        result=result|1;
      if(blue==input.K)
        result=result|2;
      x++;
      y--;
    }
  }
  
  
  //Y-line ->
  for(yR=0;yR<input.N;yR++){
    red=0;
    blue=0;
    x=0;
    y=yR;
    while(x<input.N && y>=0 && x>=0 && y<input.N){
      if(input.table[x][y]=='R'){
        red++;
        blue=0;
      }
      if(input.table[x][y]=='B'){
        blue++;
        red=0;
      }
      if(input.table[x][y]!='B' && input.table[x][y]!='R'){
        red=0;
        blue=0;                          
      }
      if(red==input.K)
        result=result|1;
      if(blue==input.K)
        result=result|2;
      x++;
      y--;
    }
  }
  
  
  //X-line <-
  for(xR=0;xR<input.N;xR++){
    red=0;
    blue=0;
    y=input.N-1;
    x=xR;
    while(x<input.N && y>=0 && x>=0 && y<input.N){
      if(input.table[x][y]=='R'){
        red++;
        blue=0;
      }
      if(input.table[x][y]=='B'){
        blue++;
        red=0;
      }
      if(input.table[x][y]!='B' && input.table[x][y]!='R'){
        red=0;
        blue=0;                          
      }
      if(red==input.K)
        result=result|1;
      if(blue==input.K)
        result=result|2;
      x--;
      y--;
    }
  }
  
  
  //Y-line <-
  for(yR=0;yR<input.N;yR++){
    red=0;
    blue=0;
    x=0;
    y=yR;
    while(x<input.N && y>=0 && x>=0 && y<input.N){
      if(input.table[x][y]=='R'){
        red++;
        blue=0;
      }
      if(input.table[x][y]=='B'){
        blue++;
        red=0;
      }
      if(input.table[x][y]!='B' && input.table[x][y]!='R'){
        red=0;
        blue=0;                          
      }
      if(red==input.K)
        result=result|1;
      if(blue==input.K)
        result=result|2;
      x--;
      y--;
    }
  }
  
  
  return result;
}

void solve(task_input &input){
  int result=0;
  
  rotate(input);
  gravity(input);
  
  result=result | getResultHorizontal(input);
  result=result | getResultVerticaly(input);
  result=result | getResultDiagonaly(input);
  input.result=result;
  //getch();
}




//////
//GLOBAL PART WHAT I WROTE TO GET USE OF THE i7 4 physical processors(with hyperthreading) in case when I can't think of the better solution then brute for
//////

#define NUMBER_OF_THREADS 8

task_input inputs[100];
int inputToSolve,numberOfInputs,solvedCount;

CRITICAL_SECTION cs_solvedCount;


//marks solved
void addSolved(){
  EnterCriticalSection(&cs_solvedCount);
  solvedCount++;
  LeaveCriticalSection(&cs_solvedCount);
}

//gets solved count
int getSolved(){
  EnterCriticalSection(&cs_solvedCount);
  int result=solvedCount;
  LeaveCriticalSection(&cs_solvedCount);
  return result;
}

//Solving function
void solvingThread(void *input){
  printf("THREAD %d STARTED\n",input);
  int nr=(int)input;
  while(nr<numberOfInputs){
    solve(inputs[nr]);
    nr+=NUMBER_OF_THREADS;              
    addSolved();
  }
  printf("THREAD %d ENDED\n",input);
}


int main(){
  //Global things
  int started=clock();
  FILE *fin;
  FILE *fout;
  int x,y;
  fin=fopen("D:\\task.in","r");
  fout=fopen("D:\\task.out","w");  
  fscanf(fin,"%d\n",&numberOfInputs);
  for(int h=0;h<numberOfInputs;h++){
    fscanf(fin,"%d %d\n",&inputs[h].N,&inputs[h].K);     
    for(y=0;y<inputs[h].N;y++){
      for(x=0;x<inputs[h].N;x++){
        fscanf(fin,"%c",&inputs[h].table[x][y]); 
      }
      fscanf(fin,"\n");
    }
  }
  inputToSolve=0;
  solvedCount=0;
  InitializeCriticalSection(&cs_solvedCount);
  
  
  //Global things(i7 processor with hyperthreading ;)
  for(int count=0;count<NUMBER_OF_THREADS;count++)
    _beginthread(solvingThread, 0, (void*)count);
  
  //As long as nessesary
  int solved=getSolved();
  while(solved<numberOfInputs){
    printf("Solved %d\n",solved);
    Sleep(200);
    solved=getSolved();
  }  
  printf("Writing into file\n");
  
  //All is over
  for(int h=0;h<numberOfInputs;h++){
    switch(inputs[h].result){
      case 0:
        fprintf(fout,"Case #%d: Neither\n",h+1);
        break;
      case 1:
        fprintf(fout,"Case #%d: Red\n",h+1);
        break;
      case 2:
        fprintf(fout,"Case #%d: Blue\n",h+1);
        break;
      case 3:
        fprintf(fout,"Case #%d: Both\n",h+1);
        break;
    }
  }
  
  //Global things
  fclose(fin);
  fclose(fout);   
  int ended=clock();
  printf("Files are closed\nDONE( whole solving took %d and %d/%d seconds)\n",((ended-started)/CLOCKS_PER_SEC),((ended-started)%CLOCKS_PER_SEC),CLOCKS_PER_SEC);
  getch();
}
