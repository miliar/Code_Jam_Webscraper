#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>

using namespace std;

// O is 0, X is 1, none is 2
int hasline(string ch){
  if(((ch[0]=='O')||(ch[0]=='T'))&&((ch[1]=='O')||(ch[1]=='T'))&&((ch[2]=='O')||(ch[2]=='T'))&&((ch[3]=='O')||(ch[3]=='T')))return 0;
  else if(((ch[0]=='X')||(ch[0]=='T'))&&((ch[1]=='X')||(ch[1]=='T'))&&((ch[2]=='X')||(ch[2]=='T'))&&((ch[3]=='X')||(ch[3]=='T')))return 1;
  else return 2;
}

// O is 0, X is 1, none is 2
int hascolumn(string ch1, string ch2, string ch3, string ch4, int col){
  if((ch1[col]=='O'||ch1[col]=='T')&&(ch2[col]=='O'||ch2[col]=='T')&&(ch3[col]=='O'||ch3[col]=='T')&&(ch4[col]=='O'||ch4[col]=='T'))return 0;
  else if((ch1[col]=='X'||ch1[col]=='T')&&(ch2[col]=='X'||ch2[col]=='T')&&(ch3[col]=='X'||ch3[col]=='T')&&(ch4[col]=='X'||ch4[col]=='T'))return 1;
  else return 2;
} 

// upper left-lower right diagonal
int hasposdiag(string ch1, string ch2, string ch3, string ch4){
  
  if((ch1[0]=='O'||ch1[0]=='T')&&(ch2[1]=='O'||ch2[1]=='T')&&(ch3[2]=='O'||ch3[2]=='T')&&(ch4[3]=='O'||ch4[3]=='T'))return 0;
  else if((ch1[0]=='X'||ch1[0]=='T')&&(ch2[1]=='X'||ch2[1]=='T')&&(ch3[2]=='X'||ch3[2]=='T')&&(ch4[3]=='X'||ch4[3]=='T'))return 1;
  else return 2;
    
}

// upper right-lower left diagonal
int hasnegdiag(string ch1, string ch2, string ch3, string ch4){
  
  if((ch1[3]=='O'||ch1[3]=='T')&&(ch2[2]=='O'||ch2[2]=='T')&&(ch3[1]=='O'||ch3[1]=='T')&&(ch4[0]=='O'||ch4[0]=='T'))return 0;
  else if((ch1[3]=='X'||ch1[3]=='T')&&(ch2[2]=='X'||ch2[2]=='T')&&(ch3[1]=='X'||ch3[1]=='T')&&(ch4[0]=='X'||ch4[0]=='T'))return 1;
  else return 2;
    
}


int isfull(string ch1, string ch2, string ch3, string ch4){
  int resp=1;
  for(int i=0;i<4;++i){
    if(ch1[i]=='.')resp=0;
  }
  for(int i=0;i<4;++i){
    if(ch2[i]=='.')resp=0;
  }
  for(int i=0;i<4;++i){
    if(ch3[i]=='.')resp=0;
  }
  for(int i=0;i<4;++i){
    if(ch4[i]=='.')resp=0;
  }
  return resp;
}  


int main(){

  ifstream input("input.in",ios::in);
  ofstream output("output.out", ios::out);
  
  int t;

  char l1[4];
  char l2[4];
  char l3[4];
  char l4[4];
  
  
  
  input>>t;
  for(unsigned i=0; i<t; ++i){
    
    input>>l1;
    cout<<l1<<"\n";
    string L1(l1,4);
    cout<<L1<<"\n";
    
    input>>l2;
    cout<<l2<<"\n";
    string L2(l2,4);
    cout<<L2<<"\n";
    
    input>>l3;
    cout<<l3<<"\n";
    string L3(l3,4);
    cout<<L3<<"\n";
    
    input>>l4;
    cout<<l4<<"\n";
    string L4(l4,4);
    cout<<L4<<"\n";
    
    //input.getline(l1, 4);
    //input.getline(l2, 4);
    //input.getline(l3, 4);
    //input.getline(l4, 4);
    
    int xwon=0;
    int owon=0;
    
    
    if(!hasline(L1)||!hasline(L2)||!hasline(L3)||!hasline(L4)||!hascolumn(L1,L2,L3,L4,0)||!hascolumn(L1,L2,L3,L4,1)||!hascolumn(L1,L2,L3,L4,2)||!hascolumn(L1,L2,L3,L4,3)||!hasposdiag(L1,L2,L3,L4)||!hasnegdiag(L1,L2,L3,L4)){owon=true;} 
    else if(hasline(L1)==1||hasline(L2)==1||hasline(L3)==1||hasline(L4)==1||hascolumn(L1,L2,L3,L4,0)==1||hascolumn(L1,L2,L3,L4,1)==1||hascolumn(L1,L2,L3,L4,2)==1||hascolumn(L1,L2,L3,L4,3)==1||hasposdiag(L1,L2,L3,L4)==1||hasnegdiag(L1,L2,L3,L4)==1){xwon=true;} 
    
    cout<<"\n";
    cout<<hasline(L1);
    cout<<owon;
    cout<<xwon;
    cout<<"\n\n";
    
    
    if(xwon&&owon){output<<"Case #"<<i+1<<": Draw\n";}
    else if(xwon&&!owon){output<<"Case #"<<i+1<<": X won\n";}
    else if(!xwon&&owon){output<<"Case #"<<i+1<<": O won\n";}
    else if(isfull(L1,L2,L3,L4)){output<<"Case #"<<i+1<<": Draw\n";}
    else{output<<"Case #"<<i+1<<": Game has not completed\n";}
  } 
  
  return 1;

}