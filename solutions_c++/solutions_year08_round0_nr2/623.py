#include <algorithm>
#include <iostream>

#define MAXNA 101

using namespace std;

int NTest;
int Arrival[2][MAXNA],Departure[2][MAXNA]; // A=0; B=1

int main()
{
  //freopen("qwer","rt",stdin);

  scanf("%d ",&NTest);
  for(int test=1;test<=NTest;test++)
  {
    int Delay,NA,NB;
    char buff[30],buf;
    scanf("%d %d %d ",&Delay,&NA,&NB);
    for(int e=0;e<NA;e++)
    {
      int q,w;
      scanf("%s ",buff);
      sscanf(buff,"%d %c %d",&q,&buf,&Departure[0][e]);
      scanf("%s ",buff);
      sscanf(buff,"%d %c %d",&w,&buf,&Arrival[0][e]);
      Departure[0][e]+=q*60;
      Arrival[0][e]+=w*60;
    }
    for(int e=0;e<NB;e++)
    {
      int q,w;
      scanf("%s ",buff);
      sscanf(buff,"%d %c %d",&q,&buf,&Departure[1][e]);
      scanf("%s ",buff);
      sscanf(buff,"%d %c %d",&w,&buf,&Arrival[1][e]);
      Departure[1][e]+=q*60;
      Arrival[1][e]+=w*60;
    }
    sort(Arrival[0],Arrival[0]+NA);
    sort(Arrival[1],Arrival[1]+NB);
    sort(Departure[0],Departure[0]+NA);
    sort(Departure[1],Departure[1]+NB);
    int AnswerA=0,AnswerB=0,inda=0,indb=0;
    for(int q=0;q<NA;q++)
      if(indb<NB&&Arrival[1][indb]+Delay<=Departure[0][q])
      {
	indb++;
	AnswerA++;
      }
    AnswerA=NA-AnswerA;
    for(int q=0;q<NB;q++)
      if(inda<NA&&Arrival[0][inda]+Delay<=Departure[1][q])
      {
	inda++;
	AnswerB++;
      }
    AnswerB=NB-AnswerB;
    printf("Case #%d: %d %d\n",test,AnswerA,AnswerB);
  }
  return 0;
}
