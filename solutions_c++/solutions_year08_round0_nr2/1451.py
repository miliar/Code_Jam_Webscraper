// using107@gmail.com

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int nCaseCnt = 0;
int T = 0;

typedef struct _TrainTime
{
  int s;
  int e;
  struct _TrainTime* next;
}TrainTime;

int nA = 0;
int nB = 0;
TrainTime* pA = NULL;
TrainTime A[100];
TrainTime* pB = NULL;
TrainTime B[100];

void AddItem(TrainTime*& start, TrainTime*item)
{
  item->next = NULL;
  if(start == NULL){
    start = item;
    return;
  }

  
  TrainTime* cur = start;
  TrainTime* previous = NULL;

  while(cur != NULL)
  {
    if(cur->s > item->s)
    {
      if(previous == NULL)
      {
        item->next = cur;
        start = item;
      }
      else
      {
        item->next = cur;
        previous->next = item;
      }
      return ;
    }
    else
    {
      previous = cur;
      cur = cur->next;
    }
  }

  previous->next = item;  
  
}
TrainTime* GetItem(TrainTime*& start, int sTime) // 
{
  TrainTime* cur = start;

  if(cur == NULL)
    return NULL;

  if(start->s >= sTime)
  {
    start = cur->next;
    return cur;
  }

  TrainTime* pre = NULL;

  while(cur != NULL)
  {
  pre = cur;
  cur = cur->next;

  if(cur == NULL)
  {
    // list end
    return NULL;
  }
  if(cur->s >= sTime)
  {
    pre->next = cur->next;
    return cur;
  }
  }

  



  return NULL;
}

void result(ifstream& fin, int&a,int&b)
{
  fin >> T;
  fin >> nA;
  fin >> nB;

  //init
  pA = pB = NULL;

  int hours, minutes;
  for(int i = 0 ; i < nA; i ++)
  {
    fin >> hours; fin.get();fin>>minutes;
    A[i].s = hours*60+minutes;
    fin.get();
    fin >> hours; fin.get();fin>>minutes;
    A[i].e = hours*60+minutes;
    AddItem(pA,&A[i]);
  }
  for(int i = 0;  i < nB; i++)
  {
    fin >> hours; fin.get();fin>>minutes;
    B[i].s = hours*60+minutes;
    fin.get();
    fin >> hours; fin.get();fin>>minutes;
    B[i].e = hours*60+minutes;
    AddItem(pB, &B[i]);
  }

  // calc the train count from A to B
  a = 0;
  b = 0;
  TrainTime* p = NULL;

  while(pA != NULL || pB != NULL)
  {
    bool Aturn;
    if(pA == NULL) Aturn = false;
    else if(pB == NULL) Aturn = true;
    else if(pA->s > pB->s)
      Aturn = false;
    else
      Aturn = true;
  
  
  if(Aturn)
  {
    a++;
    int isStartA = 0; // if modular is 0 , true
    p = GetItem(pA, 0);
    while(p!= NULL)
    {
      isStartA ++;
      p = GetItem(isStartA%2?pB:pA, p->e + T);
    }
  }
  else
  // calc the train count from B to A
  {
    b++;
    int isStartB = 0;
    p = GetItem(pB, 0);
    while(p!= NULL)
    {
      isStartB++;
      p = GetItem(isStartB%2?pA:pB, p->e + T);
    }
  }
  }
}

int main(int argc, char* argv[])
{
  ifstream fin;
  ofstream fout;
  fin.open(argv[1]);
  fout.open("trainTimeTable.out");
  
  if(!fin.is_open())
  {
    cout << " file is not opened" << endl;
    return 0;
  }

  fin >> nCaseCnt;

  int a, b;
  for(int i = 0; i < nCaseCnt;i++)
  {
    result(fin, a,b);
    fout << "Case #" << i+1 << ": " << a << " " << b << endl;
  }

  fin.close();
  fout.close();
  return 0;
}