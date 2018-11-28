#include <cstdio>
#include <cstring>

bool patt[15][26];
char word[5000][15];

int main()
{
  int l, d, n;
  scanf(" %d %d %d", &l, &d, &n);
  for(int i=0; i<d; ++i)
    {
      char buf[40];
      scanf(" %s", buf);
      for(int j=0; j<l; ++j)
	word[i][j] = buf[j] - 'a';
    }
  for(int i=0; i<n; ++i)
    {
      memset(patt, 0, sizeof(patt));
      for(int j=0; j<l; ++j) // letras
	{
	  char buf[40];
	  if(scanf(" (%[^)])", buf) == 1)
	    {
	      //printf("patt: %s\n", buf);
	      int len = strlen(buf);
	      for(int k=0; k<len; ++k)
		patt[j][buf[k] - 'a'] = true;
	    }
	  else
	    {
	      char c;
	      scanf(" %c", &c);
	      //printf("patt: %c\n", c);
	      patt[j][c - 'a'] = true;
	    }
	}
      int count = 0;
      for(int j=0; j<d; ++j) // palavras
	{
	  bool include = true;
	  for(int k=0; k<l; ++k)
	    if(!patt[k][word[j][k]])
	      {
		include = false;
		break;
	      }
	  if(include)
	    ++count;
	}
      printf("Case #%d: %d\n", i + 1, count);
    }
}
