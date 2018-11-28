#include <iostream>
#include <algorithm>
#include <fstream>
//#include <stdlib.h>
//#include <stdio.h>
//#include <cstring>
#include <conio.h>

using namespace std;
char letters[26];

int main()
{
  freopen("test.in", "rt", stdin);
  freopen("test.out", "wt", stdout);
  int i, t, j;
  char ch;
  char* s = "yeqejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
  char* l = "aozourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
  for(i = 0; ; i++)
  {
    if(s[i] == 0)
      break;
    letters[s[i] - 97] = l[i];
  
  }
  //for(ch = 97; ch < 97 + 26; ch++)
  //  cout << ch;
  //cout << "\n";
  letters[25] = 'q';
  //for(i = 0; i < 26; i++)
  //  cout << letters[i];
  //sort(letters, letters + 26);
  //for(i = 0; i < 26; i++)
  //  cout << letters[i];
  scanf("%d", &t);
  scanf("%c", &ch);
  for(i = 0; i < t; i++)
  {
    printf("Case #%d: ", i + 1);
    for(;;)
    {
      //ch = getch();
      scanf("%c", &ch);
      if(ch >= 97 && ch < 97 + 26)
        printf("%c", letters[ch - 97]);
      else if(ch == ' ')
        printf(" ");
      else
      {  
        printf("\n");
        break;
      }
    }
  }
  return 0;
}




//qz
// q to ?
// z to q
//ejp myslc kd xvn r ib  ta h wf oya u g 
//our lange is mpb t dh  wy x fc kay j v 