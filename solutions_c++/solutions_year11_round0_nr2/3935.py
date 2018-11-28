#include <cstdio>
#include <vector>

std::vector<char> stack;
char combines[256][256];
bool opposes[256][256];

void clear() {
   stack.clear();
   for(int i = 0; i < 256; i++) {
      for(int j = 0; j < 256; j++) {
         combines[i][j] = 0;
         opposes[i][j] = false;
      }
   }
}

void solve(int caseN) {
   clear();
   int c;
   scanf("%d", &c);
   for(int i = 0; i < c; i++) {
      char tmp[4];
      scanf("%s", tmp);
      combines[tmp[0]][tmp[1]] = combines[tmp[1]][tmp[0]] = tmp[2];
   }
   int d;
   scanf("%d", &d);
   for(int i = 0; i < d; i++) {
      char tmp[3];
      scanf("%s", tmp);
      opposes[tmp[0]][tmp[1]] = opposes[tmp[1]][tmp[0]] = true;
   }
   int n;
   scanf("%d", &n);
   for(int i = 0; i < n; i++) {
      char el = getchar();
      if(!('A' <= el && el <= 'Z')) {
         i--;
         continue;
      }
      stack.push_back(el);
      if(stack.size() < 2) continue;
      char replace = combines[stack[stack.size()-1]][stack[stack.size()-2]];
      if(replace != 0) {
         stack.pop_back();
         stack.pop_back();
         stack.push_back(replace);
      } else {
         for(int j = 0; j < stack.size(); j++) {
            if(opposes[stack[j]][el]) {
               stack.clear();
               break;
            }
         }
      }
   }
   printf("Case #%d: [", caseN);
   for(int i = 0; i < stack.size(); i++) {
      printf("%c", stack[i]);
      if(i != stack.size() - 1) {
         printf(", ");
      }
   }
   printf("]\n");
}

int main() {
   int n;
   scanf("%d", &n);
   for(int i = 1; i <= n; i++) {
      solve(i);
   }
   return 0;
}
