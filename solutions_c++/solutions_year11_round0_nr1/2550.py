#include<iostream>

using namespace std;

int findNextPos(int s, int e , int * seq, int val){

  int i;
  for(i=s;i<e;i+=2){
    if(seq[i] == val)
      break;
  }
  return i;
}

int move(int lr, int cs){

  if(lr == cs) return 0;
  else if (lr > cs) return 1;
  else return -1;
}

int main(){

  int t,n, step;
  int i,j=0;
  char col;
  int seq[500];
  int ts, csO, csB, lrO, lrB;

  cin>>t;

  while(j++ < t){
    cin>>n;

    for(i=0;i<n;i++)
    {
      cin>>col>>step;
      seq[2*i]=col;
      seq[2*i+1]=step;
    }

    csO=1;
    csB=1;
    ts=0;
    lrB = findNextPos(0,2*n,seq,66);
    lrO= findNextPos(0,2*n,seq,79);

    i=0;
    while(i<n){
      ts++;
//      cout<<ts<<" "<<2*i<<" "<<lrB<<" "<<csB<<" "<<lrO<<" "<<csO<<endl;
      if(lrO < 2*n) {
        if(seq[2*i] == 79 && csO == seq[2*i +1]) {
          i++;
          lrO = findNextPos(lrO+2, 2*n, seq, 79);
          csB += move(seq[lrB+1], csB);
          continue;
        }
        else
          csO += move(seq[lrO+1], csO);
      }

      if(lrB < 2*n) {
        if(seq[2*i] == 66 && csB == seq[2*i +1]) {
          i++;
          lrB = findNextPos(lrB+2, 2*n, seq, 66);
        }
        else 
          csB += move(seq[lrB+1], csB);
      }
    }
    
/*
    cout<<ts<<endl; 
    cout<<"---"<<endl;
    for(i=0;i<2*n;i++)
      cout<<seq[i]<<" ";
    cout<<endl;
    */

    cout<<"Case #"<<j<<": "<<ts<<endl;
  }

  return 0;
}
