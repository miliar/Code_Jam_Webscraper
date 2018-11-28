#include <cstdio>
#include <cstring>

#define MAX_L  20
#define MAX_D  6000
#define MAX_N  600
#define MAX_ALPHA  26

bool pos[MAX_L][MAX_ALPHA];

char dict[MAX_D][MAX_L+1];

int n,l,d;

void read_input()
{
  scanf("%d %d %d",&l,&d,&n);
  for(int i=0; i<d; i++)
    scanf("%s",dict[i]);
}

void clear_pos_tab()
{
  for(int i=0; i<l; i++)
    for(int c=0; c<26; c++)
      pos[i][c] = false;
}

void build_pos_tab(char* word)
{
  clear_pos_tab();
  int c = 0;
  int wlen = strlen(word);
  bool in_set = false;
  for(int i=0; i<wlen; i++) {
    if(word[i]=='(') {
      in_set = true;
    } else if(word[i]==')') {
      in_set = false;
      c++;
    } else {
      pos[c][word[i]-'a'] = true;
      if(!in_set)
	c++;
    }
  }
}

bool check(char *d)
{
  for(int i=0; i<l; i++)
    if(!pos[i][d[i]-'a'])
      return false;
  return true;
}

main()
{
  char w[MAX_L*(MAX_ALPHA+2) + 1];
  read_input();
  for(int i=0; i<n; i++) {
    scanf("%s",w);
    build_pos_tab(w);

    int count = 0;
    for(int j=0; j<d; j++)
      if(check(dict[j]))
	count++;
    printf("Case #%d: %d\n",i+1,count);
  }
}
