#include <iostream>
#include <string>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <vector>

using namespace std;

int compute(int int_cont_nr, int int_surprise, int int_min_score, int *v){
	int count=0;
	int surprise=int_surprise;
	for (int i=0;i<int_cont_nr;i++){
		int rounded_nr=(v[i]+2)/3;
		int rest=v[i]%3;
		if (rounded_nr>=int_min_score)
		{
			count++;
		}
		if((rounded_nr==int_min_score-1) && (surprise>0) && (rest!=1) && (rounded_nr!=0))
		{
			count++;
			surprise--;
		}
	}
	return count;
}

int main () {
	
  char case_nr[256];
  cin>>case_nr;
  int k=atoi(case_nr);
  string getToNextLine;
  getline (cin,getToNextLine);
    
  for (int i=0;i<k;i++){
	  char cont_nr[256];
	  char surprise[256];
	  char min_score[256];
	  cin>>cont_nr;
	  cin>>surprise;
	  cin>>min_score;
	  int int_cont_nr=atoi(cont_nr);
	  int int_surprise=atoi(surprise);
	  int int_min_score=atoi(min_score);
	  int *v=(int*)calloc(int_cont_nr, sizeof(int));
	  for (int j=0; j<int_cont_nr;j++){
		  char in_str[256];
		  cin>>in_str;
		  v[j]=atoi(in_str);
	  }
	  int res= compute(int_cont_nr, int_surprise, int_min_score,v);
	  cout<<"Case #"<<i+1<<": "<<res<<"\n";
	}
	
  return 0;
}
