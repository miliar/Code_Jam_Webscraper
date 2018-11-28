#include<iostream>
#include<cstdio>
#include<deque>
#include<cmath>
using namespace std;


bool zn;
int k;
deque<int> licz;
deque<int> to;
deque<int> tb;
deque<char> rob;
deque<int> lo;
deque<int> bo;
int pozo=1;
int pozb=1;
int zno=0;
int znb=0;
int glob=0;

int aio()
{
 int top=lo.front();
 // cout << top <<" "<<pozo<<endl;   
 if (pozo==top && to.front()==licz.front() && zn==false)
 {
  licz.pop_front();
  lo.pop_front();
  to.pop_front();
  zn=true;
  return 0;                  
 }
 else
 {
  if (lo.front()>pozo)
  pozo++;
 if (lo.front()<pozo)
  pozo--;
 }
    
}

int aib()
{
 int top=bo.front();
 //cout << top <<" "<<pozb<<endl;      
 if (pozb==top && tb.front()==licz.front() && zn==false)
 {
  licz.pop_front();
  bo.pop_front();
  tb.pop_front();
  zn=true;
  return 0;                  
 }
 else
 {
   if (bo.front()>pozb)
   pozb++;
   if (bo.front()<pozb)
   pozb--;
  }   
}


int main()
{
    scanf("%d",&k);
    for (int i=0;i<k;i++)
    {   
         pozo=1;
         pozb=1;
         zno=0;
         znb=0;
         glob=0;
        licz.clear();
        lo.clear();
        bo.clear();
        rob.clear();
        
      int n;
      scanf("%d",&n);  
      for (int j=0;j<n;j++)
      {
       char co;
       int ile;
       cin >> co;
       cin >> ile;
       if (co=='O')
       {
        lo.push_back(ile);
        to.push_back(j);
       }
       else
       {
        bo.push_back(ile);
        tb.push_back(j);
       }
       rob.push_back(co);
       licz.push_back(j);  
      }
      while(!licz.empty())
      {
       aio();
       aib();
       glob++;           
       zn=false;      
      }
        cout <<"Case #"<<i+1<<": "<<glob<<endl;
    }
   // system("pause");
return 0;    
}
