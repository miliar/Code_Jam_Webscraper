#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;


int printqueue(vector<int> queue){
  int qsize = queue.size();
  for(int i=0; i<qsize; i++){
    cout << queue[i] << " ";
  }
  cout << endl;
  return 0;
}

int nexthead(int k, vector<int>& queue, int head, int& cost)
{
  int qsize = queue.size();
  int sum = 0;
  int i;
  
  for(i=head; i<qsize; i++){
    sum += queue[i];
    if(sum > k)
      return i;
    else
      cost += queue[i];
  }
  
  for(i=0; i<head; i++){
    sum += queue[i];
    if(sum > k)
      return i;
    else
      cost += queue[i];
  }

  return head;
}

int themepark(int r, int k, vector<int> queue)
{
  int cost = 0;
  int qsize = queue.size();

  //printqueue(queue);
  int h=0;
  for(int i=0; i<r; i++){
    //cout << "h:" << h << endl;
    h = nexthead(k, queue, h, cost);
  }
  return cost;
}

int main(int argc, char** argv)
{
  ifstream ifs(argv[1]);
  string buf;
  int line = 0;

  int tcase;
  vector<int> round, capa, nog;
  vector<vector<int> > groups;
  
  while(ifs && getline(ifs, buf)){
    istringstream iss(buf);
    vector<int> tmp;
    int r,k,n,g;
    
    if(line == 0){
      iss >> tcase;
      cout << "tcase:" << tcase << endl;
    }
    if(line%2 == 1){
      iss >> r >> k >> n;
      round.push_back(r);
      capa.push_back(k);
      nog.push_back(n);
    }
    if(line%2 == 0 && line > 0){
      for(int i=0; i<n; i++){
        iss >> g;
        tmp.push_back(g);
      }
      groups.push_back(tmp);
    }
    
    line++;
  } 

  
  {
    ofstream ofs("result.txt");
    for(int i=0; i<tcase; i++){
      int res = themepark(round[i], capa[i], groups[i]);
      cout << "Case #" << i+1 << ": " << res << endl;
      ofs << "Case #" << i+1 << ": " << res << "\r\n";
    }
  }
  
  
  return 0;
}