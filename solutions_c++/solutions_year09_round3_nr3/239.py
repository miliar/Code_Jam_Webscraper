#include <iostream>
#include <vector>
#include <math.h>
using namespace std;


long long get(vector<int> q, int k, vector<int> stat) {
  long long n=0;
  int i=k+1;
  while(i<stat.size() && stat[i]==0) {
    n++;
    i++;
  }
  i=k-1;
  while(i>=0 && stat[i]==0) {
    n++;
    i--;
  }


  long long mmin=100000000;
  for(int i=0; i<q.size(); i++) {
    if(stat[q[i]]==0) {
      stat[q[i]]=1;
      long long m=get(q, q[i], stat);
      stat[q[i]]=0;
      if(m<mmin) mmin=m;
    }
  }
  if(mmin==100000000) mmin=0;


  return mmin+n;
}




int main() {
  int tt;
  scanf("%d", &tt);
  for(int iii=1; iii<=tt; iii++) {
    int p, q;
    scanf("%d %d", &p, &q);

    vector<int> rel;
    rel.clear();
    for(int i=0; i<q; i++) {
      int t;
      scanf("%d", &t);
      rel.push_back(t-1);
    }


    long long mmin=100000000;
//    vector<int> released(q, 0);
    vector<int> status(p);

    for(int i=0; i<q; i++) {
//      released[i]=1;
      status[rel[i]]=1;
      long long m=get(rel, rel[i], status);
      status[rel[i]]=0;
//      released[i]=0;
      if(m<mmin) mmin=m;
    }

//    if(mmin>0) mmin+=1;

    cout<<"Case #"<<iii<<": "<<mmin<<endl;


  }

  return 0;
}

