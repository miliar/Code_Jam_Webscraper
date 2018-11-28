#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_DANCERS = 1000;
const int INFINI = 2654454;
const int INCONNU = -1;

int nbTests;
int nbDancers;
int nbSurpr;
int scoreToBeat;

int scores[MAX_DANCERS];

int dyn[101][101][50];

struct Triplet
{
  int n1;
  int n2;
  int n3;
};

vector<Triplet> notes[MAX_DANCERS];

void
init_dyn()
{
  for(int i = 0; i <= nbDancers; i++)
    for(int j = 0; j <= nbSurpr; j++)
      for(int k = 0; k <= (int)notes[i].size(); k++)
	dyn[i][j][k] = INCONNU;
}

void
init_notes()
{
  for(int i = 0; i < nbDancers; i++)
    notes[i].erase(notes[i].begin(), notes[i].end());
}

bool
estValide(int a, int b, int c)
{
  if((abs(a-b) <= 2) && (abs(a-c) <= 2) && (abs(b-c) <= 2))
    return true;
  return false;
}

int
estSurpr(Triplet t)
{
  int a = t.n1;
  int b = t.n2;
  int c = t.n3;

  if(abs(a-b) == 2)
    return 1;
  if(abs(a-c) == 2)
    return 1;
  if(abs(b-c) == 2)
    return 1;
  return 0;
}

int
beat(Triplet t)
{
  int a = t.n1;
  int b = t.n2;
  int c = t.n3;
  
  if(a >= scoreToBeat)
    return 1;
  if(b >= scoreToBeat)
    return 1;
  if(c >= scoreToBeat)
    return 1;

  return 0;
}

int
nbBeatMax(int curDancer, int surprRest, int iRepr)
{

  //printf("curD %d, surpr %d, irepr %d\n", curDancer, surprRest, iRepr);

  if(curDancer == nbDancers && surprRest > 0)
    return -INFINI;
  if(surprRest < 0)
    return -INFINI;
  if((curDancer == nbDancers) && (surprRest == 0))
    return 0;

  if(dyn[curDancer][surprRest][iRepr] != INCONNU)
    return dyn[curDancer][surprRest][iRepr];

  int maxi = -INFINI;
  // pour chaque triplet possible, ou on le prend ou on le prend pas
  for(int i = iRepr; i < (int)notes[curDancer].size(); i++)
    {
      //on le prend
      maxi = max(maxi, nbBeatMax(curDancer+1, surprRest - estSurpr(notes[curDancer][i]), 0) + beat(notes[curDancer][i]));

      //on le prend pas
      maxi = max(maxi, nbBeatMax(curDancer, surprRest, i+1));
    }

  dyn[curDancer][surprRest][iRepr] = maxi;
  return maxi;
}

void
solve()
{
  init_dyn();
  init_notes();
  for(int dancer = 0; dancer < nbDancers; dancer++)
    {
      int curScore = scores[dancer];
      int mid = curScore / 3;

      for(int n1 = mid - 3; n1 < mid + 4; n1++)
	for(int n2 = mid - 3; n2 < mid + 4; n2++)
	  for(int n3 = mid - 3; n3 < mid + 4; n3++)
	    if((n1 >= 0 && n2 >= 0 && n3 >= 0) && estValide(n1,n2,n3) && ((n1 + n2 + n3) == scores[dancer]))
	      {
		Triplet t;
		t.n1 = n1;
		t.n2 = n2;
		t.n3 = n3;

		//printf("triplet %d %d %d\n", n1, n2, n3);
		
		notes[dancer].push_back(t);

	      }
      //printf("size %d\n", (int)notes[dancer].size());
    }
 
  printf("%d\n", nbBeatMax(0, nbSurpr, 0));
}

void
scan_input()
{
  scanf("%d", &nbTests);
  for(int test = 1; test <= nbTests; test++)
    {
      printf("Case #%d: ", test);
      scanf("%d", &nbDancers);
      scanf("%d", &nbSurpr);
      scanf("%d", &scoreToBeat);
      for(int i = 0; i < nbDancers; i++)
	scanf("%d", &scores[i]);

      solve();
    }
}

int
main()
{
  scan_input();

  return 0;
}
