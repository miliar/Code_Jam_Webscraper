#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

int main()
{
 int L, D, N;
 scanf("%d %d %d", &L, &D, &N);
 
 string words[30];  int pos[200][200] = {0};
 for(int i = 0; i < D; ++i)
 {
  char s[20];
  scanf("%s", s);
  words[i] = s;
  for(int j = 0; j < strlen(s); ++j)
   pos[j][s[j] - 'a'] = 1;
 }

 string tcases[20];
 int matches[20] = {0};
 for(int i = 0; i < N; ++i)
 {
    char s[1500];
    scanf("%s", s);	
    int sz = strlen(s);
 
    int tpos [200] [200] = {0};	   
    bool flag = false, match = true;
    for(int j = 0, p = 0; j < sz; ++j)
    {
      if (s[j] == '(') flag = true; 
      else if (s[j] == ')') { flag = false; ++p; continue; }
      else tpos[p][s[j] - 'a'] = 1;
      if (!flag)  { if (!pos[p][s[j] - 'a']) { match = false; break; } ++p; }
    }
    if (!match) continue;	

    for(int ii = 0; ii < D; ++ii)
    {
	string word = words[ii];
        int sz = word.size();
        for(int j = 0; (j < sz); ++j) 
	{
		int val = word[j] - 'a';
		match = tpos[j][val];
		if (!match) break; 
	}
       	matches[i] += match;
    }   
 }

 for(int i = 1; i <= N; ++i)
	printf("Case #%d: %d\n", i, matches[i-1]);
return 0;
}
