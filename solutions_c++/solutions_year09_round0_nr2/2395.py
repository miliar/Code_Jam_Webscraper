#include <cstdio>
#include <cctype>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

const int MAX_H = 100, MAX_W = 100;

unsigned short alts[MAX_H + 1][MAX_W + 1];
vector< pair<unsigned short, pair<int, int> >  > alts_tab;
int alt_map[MAX_H + 1][MAX_W + 1];
int T, H, W;
char current_label;
int current_counter;
map<int, char> labels;

pair<int, int> determine_flow(int i, int j){
  int min_i = -1, min_j = -1, lowest_alt = alts[i][j];
  // N, W, E, S
  if( i - 1 >= 0 && alts[i - 1][j] < lowest_alt ){
    min_i = i - 1;
    min_j = j;
    lowest_alt = alts[i - 1][j];
  }
  if ( j - 1 >= 0 && alts[i][j - 1] < lowest_alt ){
    min_i = i;
    min_j = j - 1;
    lowest_alt = alts[i][j - 1];    
  }
  if ( j + 1 < W && alts[i][j + 1] < lowest_alt ){
    min_i = i;
    min_j = j + 1;
    lowest_alt = alts[i][j + 1];    
  }
  if ( i + 1 < H && alts[i + 1][j] < lowest_alt ){
    min_i = i + 1;
    min_j = j;
    lowest_alt = alts[i + 1][j];    
  }
  return make_pair(min_i, min_j);
}  

void visit(int i, int j){
  alt_map[i][j] = current_counter;
  pair<int, int> flow;
  if( i - 1 >= 0 && alt_map[i-1][j] == 0) {
    flow = determine_flow(i-1, j);
    if( i == flow.first && j == flow.second ){
      visit(i-1, j);
    }
  }
  if ( j - 1 >= 0 && alt_map[i][j-1] == 0){
    flow = determine_flow(i, j-1);
    if( i == flow.first && j == flow.second ){
      visit(i, j-1);    
    }
  }
  if ( j + 1 < W && alt_map[i][j+1] == 0){
    flow = determine_flow(i, j+1);
    if( i == flow.first && j == flow.second ){
      visit(i, j+1);    
    }
  }
  if ( i + 1 < H && alt_map[i+1][j] == 0){
    flow = determine_flow(i+1, j);
    if( i == flow.first && j == flow.second ){
      visit(i+1, j);    
    }
  }  
}

int main(){
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t){
        scanf("%d%d", &H, &W);
        for(int i = 0; i < H; ++i)
          for(int j = 0; j < W; ++j){
              scanf("%hd", &alts[i][j]);
              alts_tab.push_back(make_pair(alts[i][j], make_pair(i, j)));
              alt_map[i][j] = 0;
          }
        sort(alts_tab.begin(), alts_tab.end());

        current_counter = 1;
        for(int i = 0; i < H*W; ++i)
          if(alt_map[alts_tab[i].second.first][alts_tab[i].second.second] == 0){
            visit(alts_tab[i].second.first, alts_tab[i].second.second);
            ++current_counter;
          }
          
        current_label = 'a';
        
        printf("Case #%d:\n", t);
        for(int i = 0; i < H; ++i){
          for(int j = 0; j < W - 1; ++j){
            if(labels.find(alt_map[i][j]) == labels.end())
              labels[alt_map[i][j]] = current_label++;
            printf("%c ", labels[alt_map[i][j]]);
          }
          if(labels.find(alt_map[i][W-1]) == labels.end())
            labels[alt_map[i][W-1]] = current_label++;
          printf("%c\n", labels[alt_map[i][W-1]]);          
        }
          
            
        labels.clear();
        alts_tab.clear();
    }
    return 0;
}