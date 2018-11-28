#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(void){
  string s1;
  string s2;
  string s3;
  string s4;

  int t=0;

  cin >> t;

  

  for(int i=0;i<t;i++){
    cin >> s1 >> s2 >> s3 >> s4;
    bool ok = true;
vector<int> o(10,0);
  vector<int> x(10,0);
    for(int j=0;j<4;j++){
        if(s1[j] == '.' || s2[j] == '.' || s3[j] == '.' || s4[j] == '.') { ok = false;}
        if(s1[j] == 'O' || s1[j] == 'T'){ o[0]++; o[6+j]++;}
        if(s2[j] == 'O' || s2[j] == 'T'){ o[1]++; o[6+j]++;}
        if(s3[j] == 'O' || s3[j] == 'T'){ o[2]++; o[6+j]++;}
        if(s4[j] == 'O' || s4[j] == 'T'){ o[3]++; o[6+j]++;}
        if(s1[j] == 'X' || s1[j] == 'T'){ x[0]++; x[6+j]++;}
        if(s2[j] == 'X' || s2[j] == 'T'){ x[1]++; x[6+j]++;}
        if(s3[j] == 'X' || s3[j] == 'T'){ x[2]++; x[6+j]++;}
        if(s4[j] == 'X' || s4[j] == 'T'){ x[3]++; x[6+j]++;}
    }
        if(s1[0] == 'O' || s1[0] == 'T') o[4]++;
        if(s2[1] == 'O' || s2[1] == 'T') o[4]++;
        if(s3[2] == 'O' || s3[2] == 'T') o[4]++;
        if(s4[3] == 'O' || s3[3] == 'T') o[4]++;
        if(s1[0] == 'X' || s1[0] == 'T') x[4]++;
        if(s2[1] == 'X' || s2[1] == 'T') x[4]++;
        if(s3[2] == 'X' || s3[2] == 'T') x[4]++;
        if(s4[3] == 'X' || s4[3] == 'T') x[4]++;

        if(s1[3] == 'O' || s1[3] == 'T') o[5]++;
        if(s2[2] == 'O' || s2[2] == 'T') o[5]++;
        if(s3[1] == 'O' || s3[1] == 'T') o[5]++;
        if(s4[0] == 'O' || s4[0] == 'T') o[5]++;
        if(s1[3] == 'X' || s1[3] == 'T') x[5]++;
        if(s2[2] == 'X' || s2[2] == 'T') x[5]++;
        if(s3[1] == 'X' || s3[1] == 'T') x[5]++;
        if(s4[0] == 'X' || s4[0] == 'T') x[5]++;
vector<int>::iterator largest = max_element(o.begin(), o.end());
  vector<int>::iterator largest2 = max_element(x.begin(), x.end());
  if(*largest == 4){ cout << "Case #" << i+1 <<": O won" << endl;}
  if(*largest2 == 4){ cout << "Case #" << i+1 <<": X won" << endl;}
  if(!ok && *largest2 != 4 && *largest != 4){
    cout << "Case #" << i+1 << ": Game has not completed" << endl;
  }
  if(ok && *largest2 != 4 && *largest != 4){
    cout << "Case #" << i+1 << ": Draw" << endl;
  }
  }
  
}
