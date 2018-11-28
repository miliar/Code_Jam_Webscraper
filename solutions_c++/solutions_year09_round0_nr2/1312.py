#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("file.out");

vector<vector<pair<int, int> > > map;
vector<vector<int> > result;

void func(int i, int j, int id) {
  //Нужно найти всех, кто стекает в (i,j) среди незатронутых
  result[i][j] = id;
  int cur = i*map[0].size() + j;
  if(i != 0) {
    //North
    if(map[i-1][j].second == cur) {
      func(i-1, j, id);
    }
  }
  if(j != 0) {
    //West
    if(map[i][j-1].second == cur) {
      func(i, j-1, id);
    }
  }
  if(j != map[0].size()-1) {
    //East
    if(map[i][j+1].second == cur) {
      func(i, j+1, id);
    }
  }
  if(i != map.size()-1) {
    //South
    if(map[i+1][j].second == cur) {
      func(i+1, j, id);
    }
  }
}

int main() {
  int T;
  fin >> T;
  for(int t = 0; t < T; t++) {
    int H, W;
    fin >> H >> W;
    map.resize(H, vector<pair<int, int> > ());
    result.resize(H);
    for(int i = 0; i < H; i++) {
      map[i].resize(W, make_pair(0,-1));
      result[i].resize(W, 0);
      for(int j = 0; j < W; j++) {
        int temp;
        fin >> temp;
        map[i][j] = make_pair(temp, -1);
      }
    }
    vector<pair<int, int> > sinks;  //Коллекция точек слива
    for(int i = 0; i < H; i++) {
      for(int j = 0; j < W; j++) {
        bool b = true;
        int mn = 10000;
        if(i != 0) {
          if(map[i][j].first > map[i-1][j].first) {
            b = false;
            mn = mn < map[i-1][j].first ? mn : map[i-1][j].first;
          }
        }
        if(j != 0) {
          if(map[i][j].first > map[i][j-1].first) {
            mn = mn < map[i][j-1].first ? mn : map[i][j-1].first;
            b = false;
          }
        }
        if(j != W-1) {
          if(map[i][j].first > map[i][j+1].first) {
            b = false;
            mn = mn < map[i][j+1].first ? mn : map[i][j+1].first;
          }
        }
        if(i != H-1) {
          if(map[i][j].first > map[i+1][j].first) {
            mn = mn < map[i+1][j].first ? mn : map[i+1][j].first;
            b = false;
          }
        }
        if(b) {
          sinks.push_back(make_pair(i,j));
          continue;
        }
        //Есть куда стекать
        if(i != 0) {
          if(mn == map[i-1][j].first) {
            map[i][j].second = (i-1)*W + j;
            continue;
          }
        }
        if(j != 0) {
          if(mn == map[i][j-1].first) {
            map[i][j].second = i*W + j-1;
            continue;
          }
        }
        if(j != W-1) {
          if(mn == map[i][j+1].first) {
            map[i][j].second = (i)*W + j+1;
            continue;
          }
        }
        if(i != H-1) {
          if(mn == map[i+1][j].first) {
            map[i][j].second = (i+1)*W + j;
            continue;
          }
        }
      }
    }
    //
    for(unsigned int i = 0; i < sinks.size(); i++) {
      func(sinks[i].first, sinks[i].second, i);
    }
    //Осталось переименовать при выводе
    vector<char> new_id(sinks.size(), 0);
    fout << "Case #" << t+1 << ":" << endl;
    char last = 'a';
    for(int i = 0; i < H; i++) {
      for(int j = 0; j < W; j++) {
        if(new_id[result[i][j]] == 0)
          new_id[result[i][j]] = last++;
        fout << new_id[result[i][j]] << " ";
      }
      fout << endl;
    }
  }
}
