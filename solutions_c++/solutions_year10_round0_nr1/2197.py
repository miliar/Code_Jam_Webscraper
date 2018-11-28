#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>

using namespace std;

int main(int argc, char** argv)
{
  ifstream ifs(argv[1]);
  string buf;
  int line = 1;

  int tcase;
  vector<int> snps;
  vector<int> fingers;
  
  while(ifs && getline(ifs, buf)){
    istringstream iss(buf);
    int n,k;
    
    if(line == 1)
      iss >> tcase;
    else{
      iss >> n >> k;
      snps.push_back(n);
      fingers.push_back(k);
      //cout << line-2 << " n:" << snps[line-2] << " k:" << finger[line-2] << endl;
    }
    line++;
  } 
  
  {
    ofstream ofs("result.txt");
    for(int i=0; i<tcase; i++){
      int n=snps[i], k=fingers[i];
      int s = (1 << n) -1;
      
      if((s & k) == s){
        cout << "Case #" << i+1 << ":" << " ON" << endl;
        ofs << "Case #" << i+1 << ":" << " ON" << "\r\n";
      }else{
        cout << "Case #" << i+1 << ":" << " OFF" << endl;
        ofs << "Case #" << i+1 << ":" << " OFF" << "\r\n";
      }
    }
  }

  return 0;
}