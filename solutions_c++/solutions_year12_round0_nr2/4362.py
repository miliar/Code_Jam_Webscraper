#include<iostream>
#include<vector>
#include<cstdlib>
#include<algorithm>
//#include<fstream>

using namespace std;

int main(){
  vector<int> res;
  vector<int> aux;
  int casos;
  int mejor;
  int total;
  int sorp;
  int batos;
  //fstream x;
  
  //x.open("res22.txt", ios::out);
  
  int max;
  
  cin >> casos;
  
  for(int i = 0; i<casos; i++){
    max = 0;
    aux.clear();
    cin >> batos >> sorp >> mejor;
    
    for(int j = 0; j<batos; j++){
      cin >> total;
      aux.push_back(total);
    }
    
    sort(aux.begin(), aux.end());
    
    for(int j = batos-1; j!=-1; j--){
      int actual, ax, ay, az;    
      
      actual = aux[j];    //Disque mayor
      
      ax = actual/3;
      ay = (actual%3==0?ax:ax + 1);
      az = (actual%3==0?ax:actual - (ax + ay));
      
      if (ay>=mejor){
        max++;
        continue;
      }
      
      else if(sorp!=0 && actual%3!=1 && ay>0 && (ay+1 == mejor)){
        max++;
        sorp--;
      }
      
    }
    
    res.push_back(max);
  }
  
  for(int i = 0; i<casos; i++){
    cout << "Case #" << (i+1) << ": " << res[i] << endl;
    //x << "Case #" << (i+1) << ": " << res[i] << endl;
  }
  
  //cin >> casos;
  
  return 0;
}
