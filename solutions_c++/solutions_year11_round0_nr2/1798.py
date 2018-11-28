#include <cstdio>
#include <vector>

using namespace std;

char buf[128];
int C, D;
char Combinations[26][26];
bool Oppositions[26][26];

inline void
print_list(vector<char> l)
{
  if (l.size() == 0)
	 printf("[]\n");
  else {
	 printf("[%c", l[0]);
	 
	 for (int i = 1; i < (int)l.size(); ++i)
		printf(", %c", l[i]);
	 printf("]\n");
  }

}

int
main()
{
  int T;

  scanf("%d", &T);

  for (int t = 0; t < T; ++t) {
	 for (int i = 'A'; i <= 'Z'; ++i) 
		for (int j = 'A'; j <= 'Z'; ++j) {
		  Oppositions[i-'A'][j-'A'] = false;
		  Combinations[i-'A'][j-'A'] = 0;
		}

	 scanf("%d", &C);

	 for (int i = 0; i < C; ++i) {
		scanf("%s", buf);
		// DEBUG
		//printf("Registering combo %c, %c -> %c\n", buf[0], buf[1], buf[2]);
		Combinations[buf[0]-'A'][buf[1]-'A'] = buf[2];
		Combinations[buf[1]-'A'][buf[0]-'A'] = buf[2];
	 }

	 scanf("%d", &D);

	 for (int i = 0; i < D; ++i) {
		scanf("%s", buf);
		// DEBUG
		//printf("Registering oppostion %c, %c\n", buf[0], buf[1]);
		Oppositions[buf[0]-'A'][buf[1]-'A'] = true;
		Oppositions[buf[1]-'A'][buf[0]-'A'] = true;
	 }

	 vector<char> list;

	 int N;

	 scanf("%d", &N);

	 scanf("%s", buf);

	 //printf("Invoke line : [%s]\n", buf);

	 for (int i = 0; i < N; ++i) {
		// DEBUG
		//printf("Invoking %c... ", buf[i]);

		if (list.size() == 0) {
		  list.push_back(buf[i]);
		  // DEBUG
		  //printf("succes ");
		  //print_list(list);
		  continue;
		}

		if (Combinations[list[list.size()-1]-'A'][buf[i]-'A'] != 0) {
		  list[list.size()-1] =
			 Combinations[list[list.size()-1]-'A'][buf[i]-'A'];
		  // DEBUG
		  // printf("succes ");
		  // print_list(list);
		  continue;
		}
		 
		for (int j = 0; j < (int)list.size(); ++j)
		  if (Oppositions[list[j]-'A'][buf[i]-'A']) {
			 list.clear();
			 // DEBUG
			 // printf("failure ");
			 // print_list(list);
			 break;
		  }

		if (list.size() > 0) { // it has not been cleared
		  list.push_back(buf[i]);
		  // DEBUG
		  // printf("succes ");
		  // print_list(list);
		}
	 }

	 printf("Case #%d: ", t + 1);

	 print_list(list);
  }

  return (0);
}
