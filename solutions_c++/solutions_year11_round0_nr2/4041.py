#include <iostream>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <map>
using namespace std;

int main(int argc, char* argv[]){
  int testCases;
  scanf("%d", &testCases);  
  for(int i=0; i<testCases; i++){
    int C, D, N;    
    char c1, c2, res;
    char op1, op2;
    char combine[256][256];
    for(int j=0; j<256; j++)
      for(int k=0; k<256; k++)
	combine[j][k]='\0';
    char oppose[256];
    for(int j=0; j<256; j++)
      oppose[j]='\0';
    scanf("%d", &C);
    for(int j=0; j<C; j++){
      string comb;
      cin>>comb;
      if(comb.size()!=3)
	exit(-1);
      c1=comb[0]; c2=comb[1]; res=comb[2];
      combine[c1][c2]=combine[c2][c1]=res;      
    }
    scanf("%d", &D);
    for(int j=0; j<D; j++){
      string opp;
      cin>>opp;
      if(opp.size()!=2)
	exit(-1);
      op1=opp[0]; op2=opp[1];
      oppose[op1]=op2;
      oppose[op2]=op1;      
    }
    //cout<<oppose['F']<<" "<<oppose['Q']<<endl;
    scanf("%d", &N);
    string invoke;
    cin>>invoke;
    if(invoke.size()!=N)
	exit(-1);
    string answer="";
    char cur_char;
    for(int j=0; j<N; j++){
      //cout<<"j="<<j<<endl;
      cur_char=invoke[j];
      char ans_last = answer[answer.size()-1];
      if(combine[cur_char][ans_last]!='\0' && combine[ans_last][cur_char]!='\0'){
	//cout<<"combine "<<cur_char<<" "<<ans_last<<endl;
	answer[answer.size()-1]=combine[cur_char][ans_last];
      }
      else{
	//cout<<"In oppose"<<endl;
	bool flag=false;
	for(int k=0; k<answer.size(); k++){
	  //cout<<"print "<<answer[k]<<" "<<ans_last<<endl;
	  if(oppose[answer[k]]==cur_char && oppose[cur_char]==answer[k]){
	    //cout<<"oppose "<<cur_char<<" "<<answer[k]<<endl;
	    answer="";
	    flag=true;
	    break;
	  }
	}
	if(!flag){
	  //cout<<"appending "<<cur_char<<endl;
	  answer.push_back(cur_char);
	}
      }
    }
    cout<<"Case #"<<i+1<<": [";
    for(int j=0; j<answer.size(); j++){
      if(j==answer.size()-1)
	cout<<answer[j];
      else
	cout<<answer[j]<<", ";
    }
    cout<<"]"<<endl;
  }
  return 0;
}
