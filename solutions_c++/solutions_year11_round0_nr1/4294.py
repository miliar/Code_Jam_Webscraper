#include <string>
#include <vector>
#include <set>
#include <algorithm>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

class OP
{
public:
  int pos;
  int color;
};

class Target
{
public:
  int pos;
  int step;
};

Target nextTarget(int color, int curStep, vector<OP>& vop)
{
  Target target;
  target.step = -1;
  target.pos = -1;
  for(int i = curStep+1; i < vop.size(); i++){
    if(vop[i].color == color){
      target.pos = vop[i].pos;
      target.step = i;
      break;
    }
  }
  return target;
}

int main()
{
  FILE* fin = fopen("small.in","r");
  FILE* fout = fopen("small.out","w");

  int t;
  fscanf(fin, "%d\n", &t);
  for(int j = 0; j < t; j++){  
    int n;
    fscanf(fin, "%d ", &n);
    
    vector<OP> vop;
    for(int i = 0; i < n; i++){
      char r;
      int p;
      fscanf(fin, "%c %d ", &r, &p);
      OP op;
      op.color = r=='O'?0:1;
      op.pos = p;
      vop.push_back(op);
    }

    int oPos = 1;
    int bPos = 1;
    Target oTarget = nextTarget(0,-1,vop);
    Target bTarget = nextTarget(1,-1,vop);
    int count = 0;
    int currentStep = 0;

    while(1){      
      bool isButtonPushed = false;
      //printf("ops %d oTarget %d %d, bpos %d bTarget %d %d\n",oPos, oTarget.pos, oTarget.step,bPos, bTarget.pos, bTarget.step);
      if(currentStep == vop.size())break; 
      if(oTarget.pos != -1){
	if(oPos < oTarget.pos){
	  oPos ++;
	}else if(oPos > oTarget.pos){
	  oPos --;
	}else if(oPos == oTarget.pos && oTarget.step == currentStep){
	  oTarget = nextTarget(0, currentStep, vop);
	  currentStep++;
	  isButtonPushed = true;
	}
      }

      if(bTarget.pos != -1){
	if(bPos < bTarget.pos){
	  bPos ++;
	}else if(bPos > bTarget.pos){
	  bPos --;
	}else if(bPos == bTarget.pos && bTarget.step == currentStep && !isButtonPushed){
	  bTarget = nextTarget(1, currentStep, vop);
	  currentStep++;
	}
      }
      count++;
    }
    fprintf(fout, "Case #%d: %d\n", j+1, count); 
  }

  fclose(fin);
  fclose(fout);

  return 0;
}
