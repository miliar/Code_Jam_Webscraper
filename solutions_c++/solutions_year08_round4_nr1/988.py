#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<iostream>
#include<string>

using namespace std;

struct Elem {
  int v;
  int op;
  int ch;
};

long long n;
long long tst;
long long m,ocz;

vector<Elem> tab;

int min(int a,int b){
  if (a<0 && b<0) return -1100000;
  if (a<0) return b;
    if (b<0) return a;
      if (a<b) return a;
      else return b;
}

int andy(int a,int b){
  if (a==1 && b==1) return 1; else
  return 0;
}
int ory(int a,int b){
  if (a==0 && b==0) return 0; else
  return 1;
}

int rozw(int poz,int ocz){
    //cout<<poz<<" "<<ocz<<" "<<tab[poz].v<<"\n";
  if ( tab[poz].v == ocz ) return 0;
  if (poz+1>(m-1)/2) return -1100000;
  if (ocz==0) {
      if ((tab[2*(poz+1)].v==0 || tab[2*(poz+1)-1].v==0) && tab[poz].ch == 1){
         return 1;
      }
        else
        {
      if (tab[poz].op==1 && tab[poz].ch == 0) return min(rozw(2*(poz+1),0),rozw(2*(poz+1)-1,0));
      if (tab[poz].op==0 && tab[poz].ch == 0) return rozw(2*(poz+1),0)+rozw(2*(poz+1)-1,0);
      if (tab[poz].op==1 && tab[poz].ch == 1) return min(rozw(2*(poz+1),0),rozw(2*(poz+1)-1,0));
      if (tab[poz].op==0 && tab[poz].ch == 1) return 1+min(rozw(2*(poz+1),0),rozw(2*(poz+1)-1,0));
        }
  } else {
      if ((tab[2*(poz+1)-1].v==1 || tab[2*(poz+1)].v==1) && tab[poz].ch == 1) return 1;
        else
        {

      if (tab[poz].op==1 && tab[poz].ch == 0) return rozw(2*(poz+1),1)+rozw(2*(poz+1)-1,1);
      if (tab[poz].op==0 && tab[poz].ch == 0) return min(rozw(2*(poz+1),1),rozw(2*(poz+1)-1,1));
      if (tab[poz].op==1 && tab[poz].ch == 1) return 1+min(rozw(2*(poz+1),1),rozw(2*(poz+1)-1,1));
      if (tab[poz].op==0 && tab[poz].ch == 1) return min(rozw(2*(poz+1),1),rozw(2*(poz+1)-1,1));
        }
  }

}

int main() {



tst = 0;

cin >> tst ;
for(int u=0;u<tst;u++) {
cin >> m;
cin >> ocz;
tab.clear();
  for(int uu=0;uu<(m-1)/2;uu++){
    int a,b;
    cin >> a;
    cin >> b;
    Elem elem;
    elem.v = -1;
    elem.op = a;
    elem.ch = b;
    tab.push_back(elem);

  }
  for(int uu=0;uu<(m+1)/2;uu++){
    int a,b;
    cin >> a;
    Elem elem;
    elem.v = a;
    tab.push_back(elem);
  }

  for(int uu=m-1;uu>=0;uu--){
    if (2*(uu+1)<m)
      if (tab[uu].op==1)
      {
       tab[uu].v = andy(tab[2*(uu+1)].v,tab[2*(uu+1)-1].v);

      }
       else
       {
       tab[uu].v = ory(tab[2*(uu+1)].v,tab[2*(uu+1)-1].v);

       }
  }

  if (tab[0].v == ocz)  {

     cout << "Case #" << u+1 << ": 0 \n";
  } else
  {
    int wyn = rozw(0,ocz);
    if (wyn <-1)
       cout << "Case #" << u+1 << ": IMPOSSIBLE\n";
       else
        cout << "Case #" << u+1 << ": "<< wyn<<"\n";
  }
}


return 0;
}
