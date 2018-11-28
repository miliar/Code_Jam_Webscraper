#include<iostream>
#include<map>
#include<vector>
using namespace std;

int main(void){

  int t,n;
  pair<char,int>r[120];
  vector<int> vo;
  vector<int> vb;


  while(cin >> t){
     
    for(int i = 0 ; i < t ; i++){
      
      int pos_o = 1,pos_b = 1;
      int cnt_o = 0,cnt_b = 0,ind = 0,cnt =0;
      vo.clear();
      vb.clear();

      cin >> n;
      for(int j = 0 ; j < n ; j++){
	cin >> r[j].first >> r[j].second;
	if(r[j].first == 'O') vo.push_back(r[j].second);
	else if(r[j].first == 'B') vb.push_back(r[j].second);
      }
    

      while(1){

	bool f = true;

	if(f && r[ind].first == 'O' && pos_o == r[ind].second){
	  ind++;
	  cnt_o++;
	  f = false;
	}
	else if(pos_o > vo[cnt_o])pos_o--;
	else if(pos_o < vo[cnt_o])pos_o++;

        if(f && r[ind].first == 'B' && pos_b == r[ind].second){
	  ind++;
	  cnt_b++;
	  f = false;
	}
	else if(pos_b > vb[cnt_b])pos_b--;
	else if(pos_b < vb[cnt_b])pos_b++;
  
	cnt++;
	if(ind == n)break;
      }
      cout << "Case #" << i + 1 << ": " << cnt << endl; 
    }
  }
  return 0;
}
