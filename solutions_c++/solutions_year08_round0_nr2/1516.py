#include<stdio.h>
#include<conio.h>


int process_t(char timestr[])
{
int time;
time=(timestr[0]-'0')*600+(timestr[1]-'0')*60+(timestr[3]-'0')*10+(timestr[4]-'0');
return time;
}

int main()
{
    int stationA[1600], stationB[1600];
    int i,j,k, minA,sumA, sumB, minB;
    
    int N, T, NA, NB;
    scanf(" %d", &N);
    
    char time[5];
    
    for(k=0; k<N; k++)
    {
             sumA=0;
             minA=0;
             sumB=0;
             minB=0;
             scanf(" %d", &T);
             scanf(" %d %d", &NA, &NB);
             
             for(i=0; i<1600; i++)
             {
                      stationA[i]=0;
                      stationB[i]=0;
             }
             
             for(i=0; i<NA; i++)
             {
                      //int dephrs, depmins, arrhrs, arrmins;
                      
                      //scanf(" %d:%d %d:%d", &dephrs, &depmins, &arrhrs, &arrmins);
                      scanf(" %s", time);
                      
                      stationA[process_t(time)]-=1;
                      scanf(" %s", time);
                      stationB[process_t(time) + T]+=1;
             }
             
             for(i=0; i<NB; i++)
             {
                      //int dephrs, depmins, arrhrs, arrmins;
                      //scanf(" %d:%d %d:%d", &dephrs, &depmins, &arrhrs, &arrmins);
                      scanf(" %s", time);
                      stationB[process_t(time)]-=1;
                      scanf(" %s", time);
                      stationA[process_t(time)+T]+=1;
             }
             
             for(i=0;i<1600; i++)
             {
                             
                             sumA+=stationA[i];
                             if(sumA<minA)
                             minA=sumA;
                             
                             sumB+=stationB[i];
                             if(sumB<minB)
                             minB=sumB;
                             
             }
             
             printf("Case #%d: %d %d\n", k+1, -minA, -minB);
    }

             return 0;
}
                             
                             
             
             
             
             
                      
