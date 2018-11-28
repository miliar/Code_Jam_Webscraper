#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
#define MAX 'Z' + 1
#define MAX_STR 102400
int main() {
  int oposite[MAX][MAX];
  char combine[MAX][MAX];
 
  int T;
  scanf("%d",&T);
  for (int case_n = 1 ; case_n <= T ; case_n++) {
    int C, O, E;
    memset(combine, 0, sizeof(combine));
    memset(oposite, 0, sizeof(oposite));
    char aux[MAX_STR];
    scanf("%d",&C);
  
    for (int i = 0 ; i < C ; i++)  {
      scanf("%s",aux);
      combine[aux[0]][aux[1]] = aux[2];
      combine[aux[1]][aux[0]] = aux[2];
    }
    scanf("%d",&O);
    for (int i=  0 ; i < O ; i++) {
      scanf("%s", aux);
      oposite[aux[0]][aux[1]] = oposite[aux[1]][aux[0]] = 1;
    }
    scanf("%d",&E);
    vector<char> answer;
    for (int i = 0 ; i < E ; i++) {
      char v_aux;
      scanf(" %c",&v_aux);
      if (answer.size() == 0)
	answer.push_back(v_aux);
      else {
	if (combine[answer[answer.size()-1]][v_aux] != 0)
	  answer[answer.size()-1] = combine[answer[answer.size()-1]][v_aux];
	else {
	  answer.push_back(v_aux);
	  for (int i = 0 ; i < answer.size() ; i++)
	    if (oposite[v_aux][answer[i]] == 1) {
	      answer.erase(answer.begin(), answer.end());

	      break;
	    }
	}
      }
    }
    printf("Case #%d: [", case_n);
    for (int i = 0 ; i < ((int)answer.size()) - 1 ; i++) {
      printf("%c, ", answer[i]);
     
    }
    if (answer.size())
      printf("%c", answer[answer.size()-1]);
    printf("]\n");
    
  }
    
  return 0;
}
