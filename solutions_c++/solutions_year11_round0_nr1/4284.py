#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

struct Checkpoint {
  int oQuePos,bQuePos,quePos,time;
};

int main() {
  int N;
  scanf("%d",&N);
  for(int N__=1;N__<=N;N__++) {
    int oQue[101],bQue[101],que[100],oQueN,bQueN,queN;
    memset(oQue,0,sizeof(oQue));
    memset(bQue,0,sizeof(bQue));
    memset(que,0,sizeof(que));
    char queColor[100];
    oQueN=bQueN=queN=0;
    scanf("%d",&queN);

    for(int i=0;i<queN;i++) {
      char bot;
      while(1) {
	bot=getchar();
	if(bot=='B' || bot=='O')
	  break;
      }
      scanf("%d",que+i);
      if(bot=='B') {
	bQue[bQueN]=que[i];
	queColor[i]='B';
	bQueN++;
      }
      else {
	oQue[oQueN]=que[i];
	queColor[i]='O';
	oQueN++;
      }
    }

    Checkpoint checkpoint={0,0,0,0};
    int bAbsPos=1,oAbsPos=1;
    while(checkpoint.quePos!=queN) {
      int bAbsTarget=bQue[checkpoint.bQuePos];
      int oAbsTarget=oQue[checkpoint.oQuePos];
      int moveTimes;
      char turn=queColor[checkpoint.quePos];
      moveTimes= (turn=='O')?abs(oAbsTarget-oAbsPos):abs(bAbsTarget-bAbsPos);
      moveTimes++;
      if(turn=='O') {
	checkpoint.oQuePos++;
	oAbsPos=oAbsTarget;
	if(abs(bAbsTarget-bAbsPos)<=moveTimes)
	  bAbsPos=bAbsTarget;
	else
	  bAbsPos+= (bAbsTarget>bAbsPos)?moveTimes:-moveTimes;
      }
      if(turn=='B') {
	checkpoint.bQuePos++;
	bAbsPos=bAbsTarget;
	if(abs(oAbsTarget-oAbsPos)<=moveTimes)
	  oAbsPos=oAbsTarget;
	else
	  oAbsPos+= (oAbsTarget>oAbsPos)?moveTimes:-moveTimes;
      }
      checkpoint.quePos++;
      checkpoint.time+=moveTimes;
    }
    printf("Case #%d: %d\n",N__,checkpoint.time);
  }
  return 0;
}
