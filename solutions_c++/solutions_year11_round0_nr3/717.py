#include <iostream>
#include <algorithm>

#define N 1000

using namespace std;

int main(){
  int case_num,flag,i, j, k, num, piles[N],binary[21], keep=0;
  cin >> case_num;
  for(j=0; j<case_num ; j++){
    cin >> num;
    flag=0;
    keep =0;
    for(i=0; i<21; i++){
      binary[i]=0;
    }

    for(i =0; i<num; i++){
      cin >> piles[i];
    }
    sort(piles, piles+num);
    
    //able to separate?
    for(k=0 ;k<num ;k++){
      int t=piles[k];
      for(i=0;t>0;i++){
	binary[i] += t%2;
	t=(t-t%2)/2;
      }
    }
    for(k=0;k<21;k++){
      //cout << binary[k] << endl;
      if(binary[k]%2!=0)
	flag=1;
    }
    if(flag==1){
      cout << endl << "Case #" << j+1 << ": NO";
    }else{
      for(i=1; i < num; i++){
	//cout << "piles"<<piles[i] << endl;
	keep+=piles[i];
      }
      cout <<endl<< "Case #" << j+1 << ": " << keep;
    }
  }//one case
  cout << endl;
  return 0;
}

