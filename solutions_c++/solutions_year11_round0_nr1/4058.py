  #include "iostream.h"
  
  int main(){
    int bPos = 1, oPos = 1, time = 0;
    int bSeq[100][2], oSeq[100][2];
  
    int T, N;
    char robo;
    int i, io, ib;
    int j = 0;
    int no, nb;

    cin >>T;

    while (T-->0){
      j++;
      cin >> N;
      i =1, ib=0, io=0;
      while (N-->0){
        cin >> robo;
        if (robo == 'B'){
          bSeq[ib][1] = i;
          cin >> bSeq[ib++][0];
        }
        if (robo == 'O'){
          oSeq[io][1] = i;
          cin >> oSeq[io++][0];
        }
        i++;
        }
        no = io;
        nb = ib;
        
        bPos = 1, oPos = 1;
        time = 0;
        io = ib = 0;

        while (io < no || ib < nb){
          if (ib==nb){
        while (io<no){
          if (oPos == oSeq[io][0]) {
          time++;
          io++;
        }
      else if (oPos < oSeq[io][0]) {
        time++;
        oPos++;
        }
      else {
        time++;
        oPos--;
        }
      }      
      }
      else if(io==no){
      while (ib<nb){
        if (bPos == bSeq[ib][0]) {
        time++;
        ib++;
      }
      else if (bPos < bSeq[ib][0]) {
        time++;
        bPos++;
      }
      else {
        time++;
        bPos--;
      }
      }      
        }
    else{
      time++;
      if (bPos == bSeq[ib][0] && oPos == oSeq[io][0])
      {
        if (bSeq[ib][1] < oSeq[io][1]) {
        ib++;
        if (oPos < oSeq[io][0]) oPos++;
          else if (oPos > oSeq[io][0]) oPos--;
      }
      else 
      {
        io++;
        if (bPos < bSeq[ib][0]) bPos++;
          else if (bPos > bSeq[ib][0]) bPos--;
      }
      }
      else if (bPos == bSeq[ib][0])
      {
        if (bSeq[ib][1] < oSeq[io][1]) ib++;
      if (oPos < oSeq[io][0]) oPos++;
        else if (oPos > oSeq[io][0]) oPos--;
      }
      else if (oPos == oSeq[io][0])
      {
        if (bSeq[ib][1] > oSeq[io][1]) io++;
      if (bPos < bSeq[ib][0]) bPos++;
        else if (bPos > bSeq[ib][0]) bPos--;
      }
      else
      {
      if (oPos < oSeq[io][0]) oPos++;
        else if (oPos > oSeq[io][0]) oPos--;
      if (bPos < bSeq[ib][0]) bPos++;
        else if (bPos > bSeq[ib][0]) bPos--;      
      }
    }
      }
  cout << "Case #" << j << ": " << time << endl;  
    }
    return 1;
  }
