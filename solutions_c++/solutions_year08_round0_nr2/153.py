#include <stdio.h>
#include <string.h>

const int N_MAX  = 100;
const int NA_MAX = 100;
const int NB_MAX = 100;
const int T_MAX  =  60;

int N, NA, NB, T;
int resNA, resNB;

int ScheduleDep[NA_MAX+NB_MAX];
int ScheduleArr[NA_MAX+NB_MAX];
int SchedulePnt[NA_MAX+NB_MAX]; /* 0 - from A, 1 - from B */

int CurrentTrains;
int CurrentArr[NA_MAX+NB_MAX];
int CurrentPnt[NA_MAX+NB_MAX];

void Solver(void){
  int RemainingTrains = NA+NB;
  int MaxArr, MaxTrain;
  int SuitableTrain;
  int i;

  CurrentTrains = 0;
  while( RemainingTrains > 0 ){
    /* finding max arrival time */
    MaxTrain = 0;
    MaxArr = ScheduleArr[0];
    for( i = 1; i < RemainingTrains; i ++ ){
      if( MaxArr < ScheduleArr[i] ){
        MaxTrain = i;
        MaxArr = ScheduleArr[i];
      }
    }
    SuitableTrain = -1;
    for( i = 0; i < CurrentTrains; i ++ ){
      if( ( ScheduleArr[MaxTrain] <= CurrentArr[i] )
          &&( SchedulePnt[MaxTrain] != CurrentPnt[i] ) ){
        SuitableTrain = i;
      }
    }
    if( SuitableTrain != -1 ){
      CurrentArr[SuitableTrain] = ScheduleDep[MaxTrain] - T;
      CurrentPnt[SuitableTrain] = SchedulePnt[MaxTrain];
    }
    else{
      CurrentTrains ++;
      CurrentArr[CurrentTrains-1] = ScheduleDep[MaxTrain] - T;
      CurrentPnt[CurrentTrains-1] = SchedulePnt[MaxTrain];
    }
    RemainingTrains --;
    if( RemainingTrains > 0 ){
      ScheduleDep[MaxTrain] = ScheduleDep[RemainingTrains];
      ScheduleArr[MaxTrain] = ScheduleArr[RemainingTrains];
      SchedulePnt[MaxTrain] = SchedulePnt[RemainingTrains];
    }
  }
  resNA = 0;
  resNB = 0;
  for( i = 0; i < CurrentTrains; i ++ ){
    if( CurrentPnt[i] == 0 ){
      resNA++;
    }
    else{
      resNB++;
    }
  }
}

int main(int argc, char *argv[]){
  FILE* file;
  FILE* fileout;
  int n, i, res, h1, m1, h2, m2;

  if( argc < 2 ){
    printf("Usage is: task1 filename\n");
    return 0;
  }

  /* Input */

  file = fopen(argv[1], "r");
  if( file == NULL ){
    printf("Error open();\n");
    return 0;
  }
  fileout = fopen("res.txt", "w");


  fscanf(file, "%d\n", &N);
  for( n = 0; n < N; n ++ ){
    fscanf(file, "%d\n", &T);
    fscanf(file, "%d %d\n", &NA, &NB);
    for( i = 0; i < NA; i ++ ){
      fscanf(file, "%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
      ScheduleDep[i] = h1*60 + m1;
      ScheduleArr[i] = h2*60 + m2;
      SchedulePnt[i] = 0;
    }
    for( i = 0; i < NB; i ++ ){
      fscanf(file, "%d:%d %d:%d\n", &h1, &m1, &h2, &m2);
      ScheduleDep[NA+i] = h1*60 + m1;
      ScheduleArr[NA+i] = h2*60 + m2;
      SchedulePnt[NA+i] = 1;
    }

  printf("%d\n", T);
  printf("%d %d\n", NA, NB);
  for( i = 0; i < NA; i ++ ){
    printf("%d %d %d\n", ScheduleDep[i], ScheduleArr[i], SchedulePnt[i]);
  }
  for( i = 0; i < NB; i ++ ){
    printf("%d %d %d\n", ScheduleDep[NA+i], ScheduleArr[NA+i], SchedulePnt[NA+i]);
  }

    /* Solving */
    Solver();
    /* Output */
    fprintf(fileout, "Case #%d: %d %d\n", n+1, resNA, resNB);
  }


  fclose(fileout);
  fclose(file);

  return 0;
}
