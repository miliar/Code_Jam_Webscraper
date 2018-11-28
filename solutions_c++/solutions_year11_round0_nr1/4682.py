#include<iostream>
using  namespace std;

int num;        // no of button-presses
char bot[200];  
int but[200];
int currseq = 0;
int oloc = 1;
int bloc = 1;
int toto = 0;
int totb = 0;
int tot = 0;
bool firsttime = true;
int findnextbut(char bottype) {
  bool found = false;
  for(int i = currseq+1; i < num ; i++) {
    if(bottype == bot[i]) {
      found = true;
      return but[i];
      break;
    }
  }
  if(found == false)
    return -1;
}

void reachbutton(char bot) {
  if(bot == 'B') {
    if(bloc < but[currseq]) {
//      cout<<"B moved right\n"<<endl;
      bloc++;
    } else 
    if(bloc > but[currseq]) {
//      cout<<"B moved leftt\n"<<endl;
      bloc--;
    }
  }
  if(bot == 'O') {
    if(oloc < but[currseq]) {
  //    cout<<"O moved right\n"<<endl;
      oloc++;
    } else 
    if(oloc > but[currseq]) {
//      cout<<"O moved left\n"<<endl;
      oloc--;
    }
  }
}

void reachbuttonnext(char bot) {
  int nextloc;
  if(bot == 'B') {
    nextloc = findnextbut('B');
    if(bloc < nextloc) {
//      cout<<"B moved right\n"<<endl;
      bloc++;
    } else 
    if(bloc > nextloc) {
//      cout<<"B moved left\n"<<endl;
      bloc--;
    }
  }
  if(bot == 'O') {
    nextloc = findnextbut('O');
    if(oloc < nextloc) {
//      cout<<"O moved right\n"<<endl;
      oloc++;
    } else 
    if(oloc > nextloc) {
//      cout<<"O moved left\n"<<endl;
      oloc--;
    }
  }
}

int tick = 0;

int main() {

  // taking inputs
  int numcases;
  cin>>numcases;
  for(int i = 0; i < numcases; i++) {
    cin>>num;
    //resetting variables
    currseq = 0;
    oloc = 1;
    bloc = 1;
    toto = 0;
    totb = 0;
    tot = 0;
    for(int j = 0; j < num; j++) {
      cin>>bot[j];
      if(bot[j] == 'B')
        totb++; else toto++;
      cin>>but[j];
    }
    tot = totb + toto;
/*    cout<<num<<" "<<currseq<<" "<<oloc<<" "<<bloc<<" "<<toto<<" "<<totb<<" "<<endl;
    for(int j = 0; j < num; j++) {
      cout<<" "<<bot[j];
      cout<<" "<<but[j];
    }
    cout<<endl;
*/
  
    //main execution here
/*    if(firsttime){
      firsttime = false;
    } else {
      cout<<"HHHHHHHHOOOOOOOHHHHHHAAAAAAA: Case #"<<i+1<<": "<<tick<<endl;
    }
*/    tick = 0;
    do {
      tick++;
//      cout<<"Tick "<<tick<<endl;
      
      if(bot[currseq] == 'B') {

        // if B is at the button and its his turn
        if(bloc == but[currseq]) {
//          cout<<"B pressed button at "<<bloc<<endl;
          reachbuttonnext('O');
          currseq++;
          totb--;
        } else {
          reachbutton('B');
          reachbuttonnext('O');
        }
        
      } else {

        // if O is at the button and its his turn
        if(oloc == but[currseq]) {
//          cout<<"O pressed button at "<<oloc<<endl;
          reachbuttonnext('B');
          currseq++;
          toto--;
        } else {
          reachbuttonnext('B');
          reachbutton('O');
        }
      
      }
    } while (totb > 0 || toto > 0);

      cout<<"Case #"<<i+1<<": "<<tick<<endl;

  }
  
}
