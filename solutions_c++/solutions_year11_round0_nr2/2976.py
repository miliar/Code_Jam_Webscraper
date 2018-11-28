#include <iostream>
#include <vector>
using namespace std;

int a[256][256];
int b[256][256];

int main(){
  int t, n,x,y,kase=1;
  cin >> t;
  string s;
  while(t--){   
      memset(a,-1,sizeof a);
      memset(b,0,sizeof b);
      cin >> x ;
      for(int j=0 ; j < x; j++){
        cin >> s;
        a[s[0]][s[1]] = s[2];
        a[s[1]][s[0]] = s[2];
      }
      cin >> x ;
      for(int j= 0; j < x; j++){
        cin >> s;
        b[s[0]][s[1]] = 1;
        b[s[1]][s[0]] = 1;
      }
      cin >> x >> s;
      vector<int> v;
      int exist[256] = {0};
      int tmp = 0;
      for(int i = 0; i < s.length(); i++){
        if(v.empty()){v.push_back(s[i]);exist[s[i]]++;continue;}
        if(a[v.back()][s[i]]>=0){
          exist[v.back()]--;
          tmp = v.back();
          v.pop_back();
          v.push_back(a[tmp][s[i]]);
          exist[a[tmp][s[i]]]++;
        }
        else{
          int tmp2 = 0;
          v.push_back(s[i]);        
          for(int j =0 ; j < 256; j++){
               
            if(b[j][s[i]] && exist[j]){
            tmp2=1;
              memset(exist,0,sizeof exist);
              v.clear();
            }
          }
          if(!tmp2)
            exist[s[i]]++;
        }

      }
      cout << "Case #" << kase++ << ": [";
      for(int i =0; i < v.size(); i++){
        if(i){
          cout << ", "; 
        }
        cout << (char)v[i];
      }
      cout << "]" << endl;
  }
  return 0;    
}
