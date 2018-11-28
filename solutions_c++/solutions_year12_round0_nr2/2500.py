#include <iostream>
#include <vector>


using namespace std;


int main() {
  
  int cases;
  int number=1;
  cin >> cases;
 
while(cases--){ 
  
  int googlers=0, surprizes=0, atleastscore=0;
  
  cin >> googlers >> surprizes>> atleastscore;
  
  vector<int> scores;
  vector<int>::iterator it;
  scores.resize(googlers);
  
  for (int i=0; i<googlers; i++){
    cin >> scores[i];
  }
  
  int max_count=0;
  
  for (int i=0; i<googlers; i++){
    int base_score=scores[i]/3;
    
    if (scores[i]%3>0){
      base_score++;
    }
    
    if (base_score>=atleastscore){
      max_count++;
    } else {
      if ((scores[i]%3==2 || scores[i]%3==0)&& surprizes!=0){
	
	if ((base_score-1)>=0) base_score++;
	
	if (base_score>=atleastscore){
	  max_count++;
	  surprizes--;
	}
	
      }
    }
    
  }
  
  cout<< "Case #" << number <<": "<< max_count << endl;
  
  number++; 
}
  
  return 0;
}