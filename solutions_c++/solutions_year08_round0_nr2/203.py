#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

int testNum,testCase;

int NA,NB;

int T;

struct Schedule
{
  int dep;
  int arr;
  char local;
};

bool compare_sch (const Schedule &A,const Schedule &B)
{
  return A.dep<B.dep;
}

Schedule sch[200];

int cntA,cntB;

int heapA[200],heapB[200];
int hAs,hBs;

int main()
{
  cin>>testNum;
  for (testCase=1;testCase<=testNum;++testCase)
  {
    cin>>T;
    cin>>NA>>NB;
    for (int i=0;i<NA;++i)
    {
      char dumb;
      int hh,mm;
      cin>>hh>>dumb>>mm;
      sch[i].dep=hh*60+mm;
      cin>>hh>>dumb>>mm;
      sch[i].arr=hh*60+mm;
      sch[i].local='A';
    }
    for (int i=0;i<NB;++i)
    {
      char dumb;
      int hh,mm;
      cin>>hh>>dumb>>mm;
      sch[i+NA].dep=hh*60+mm;
      cin>>hh>>dumb>>mm;
      sch[i+NA].arr=hh*60+mm;
      sch[i+NA].local='B';
    }
    sort(sch,sch+NA+NB,compare_sch);
    cntA=cntB=0;
    hAs=hBs=0;
    for (int i=0;i<NA+NB;++i)
      if (sch[i].local=='A')
      {
        if (hAs==0 || heapA[0]>sch[i].dep)
          ++cntA;
        else
        {
          pop_heap(heapA,heapA+hAs,greater<int>());
          --hAs;
        }
        heapB[hBs++]=sch[i].arr+T;
        push_heap(heapB,heapB+hBs,greater<int>());
      }
      else
      {
        if (hBs==0 || heapB[0]>sch[i].dep)
          ++cntB;
        else
        {
          pop_heap(heapB,heapB+hBs,greater<int>());
          --hBs;
        }
        heapA[hAs++]=sch[i].arr+T;
        push_heap(heapA,heapA+hAs,greater<int>());
      }
    cout<<"Case #"<<testCase<<": ";
    cout<<cntA<<' '<<cntB<<endl;
  }
}
