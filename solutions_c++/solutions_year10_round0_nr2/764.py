#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

/* m > n */
int gcd(int m, int n)
{
  if(n==0) return m;

  while(n != 0){
    int t = m%n;
    m = n;
    n = t;
  }
  return m;
}

int fairwarning(vector<int> sec)
{
  int ssize = sec.size();
  int a[ssize-1];
  int g;

  sort(sec.begin(), sec.end());

  for(int i=0; i<ssize-1; i++){
    a[i] = sec[i+1] - sec[i];

    if(i==0)
      g = a[0];
    if(i>0)
      if(a[i] > g){
        g = gcd(a[i], g);
      }else{
        g = gcd(g, a[i]);
      }
  }
  cout <<"gcd: " << g << endl;
  int mod = sec[0]%g;
  cout <<"mod: " << mod <<endl;
  cout <<"res: " << g-mod << endl;
  if(mod == 0) return 0;
  else return g-mod;
}

int main(int argc, char** argv)
{
  ifstream ifs(argv[1]);
  string buf;
  int line = 1;

  int tcase;
  vector<vector<int> > sec;
  
  while(ifs && getline(ifs, buf)){
    istringstream iss(buf);
    vector<int> tmp;
    int n,k;
    
    if(line == 1)
      iss >> tcase;
    else{
      iss >> n;
      //cout << "n:" << n;
      for(int i=0; i<n; i++){
        iss >> k;
        //cout << " " << k;
        tmp.push_back(k);
      }
      sec.push_back(tmp);
      //cout << endl;
    }
    line++;
  } 

  {
    ofstream ofs("result.txt");
    for(int i=0; i<tcase; i++){
      int res = fairwarning(sec[i]);
      cout << "Case #" << i+1 << ": " << res << endl;
      ofs << "Case #" << i+1 << ": " << res << "\r\n";
    }
  }
  
  
  return 0;
}