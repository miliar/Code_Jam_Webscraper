#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
int solve(vector <int> num, vector <string> who){
  int pos[2];
  int accm[2];
  int cnt=0;
  accm[0]=accm[1]=0;
  pos[1]=pos[0]=1;

  for(int i=0;i<num.size();i++){
    int sign  = who[i]=="O" ? 0:1;
    int dist = abs(pos[sign] - num[i]);
    if(dist <= accm[sign]){
      cnt ++;
      accm[1-sign]++;
    }
    else{
      cnt += dist - accm[sign] + 1;
      accm[1-sign] += dist - accm[sign] + 1;
    }
    accm[sign] = 0;
    pos[sign] = num[i];
  }
  return cnt;
}

int main(){
  fstream fs;
  FILE* ofs;
  vector <int> num;
  vector <string> who;
  int s;

  fs.open("A-large.in", fstream::in);  
  ofs = fopen("outputlarge_A", "w");
  //  ofs.open("in", fstream::out);
  fs >> s;

  for(int i=0;i<s;i++){
    int s2;
    fs >> s2;
    num.clear();
    who.clear();
    for(int j=0;j<s2;j++){
      string str;
      int n;
      fs >> str;
      fs >> n;
      who.push_back(str);
      num.push_back(n);
    }
    int ans = solve(num, who);
    fprintf(ofs, "Case #%d: %d\n", i+1, ans);
    cout << ans <<"\n";
  }
  return 0;
}
