#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <vector>

char replace[256][256];
bool forbidden[256][256];

void clear() {
  for (int i=0; i<256; i++) {
    for (int j=0; j<256; j++) {
      replace[i][j] = 0;
      forbidden[i][j] = false;
    }
  }   
}

bool shrink_if_neccessery(std::vector<char>& result) {  
  int n = result.size();
  
  if (n < 2) return false;
  if (replace[result[n-2]][result[n-1]] == 0) return false;
  
  result[n-2] = replace[result[n-2]][result[n-1]];
  result.pop_back();
  return true;
}

void clear_if_neccessery(std::vector<char>& result) {  
  for (int i=0; i<result.size(); i++) {
    for (int j=0; j<i; j++) {
      if (forbidden[result[i]][result[j]]){
        result.clear();
        return ;
      } 
    }
  } 
}

void readAndSolveSingleCase() {
  clear();
  
  char word[1010];
  int n, len;
  
  scanf("%d ",&n);
  for (int i=0; i<n; i++){
    scanf("%s",word);
    replace[word[0]][word[1]] = word[2];
    replace[word[1]][word[0]] = word[2];
  }
  
  scanf("%d ",&n);
  for (int i=0; i<n; i++){
    scanf("%s",word);
    forbidden[word[0]][word[1]] = true;
    forbidden[word[1]][word[0]] = true;
  }
  
  scanf("%d %s",&len, word);
  std::vector<char> result;
  for (int i=0; i<len; i++) {
    result.push_back(word[i]);
    while (shrink_if_neccessery(result)); //while shrinking is neccessery
    clear_if_neccessery(result);
  }
  
  if (result.size() == 0){ puts("[]"); return ; }
  printf("[%c", result[0]);
  for(int i=1; i<result.size(); i++) printf(", %c",result[i]);
  puts("]");
}

int main(){
  int cases;
  scanf("%d", &cases);
  for (int i = 1; i <= cases; i++) {
    printf("Case #%d: ",i);
    readAndSolveSingleCase();
  }
  return 0;
}
