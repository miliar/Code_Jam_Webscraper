#include <iostream>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef struct str_node {
  str_node *childs[30];
} node;


int l, d, n, i;
node *root;

void regword(char *word)
{
  node *cur=root;
  unsigned int j;
  for(j=0;j<l-1;j++)
  {
    if(cur->childs[word[j]-'a'] == NULL)
    {
      cur->childs[word[j]-'a'] = new str_node;
      memset(&(cur->childs[word[j]-'a']->childs), 0, sizeof(node *) * 30);
    }
    cur = cur->childs[word[j]-'a'];
  }
  cur->childs[word[j]-'a'] = cur;
}

unsigned int count(node *cur, char *pattern)
{
  unsigned int total = 0;
  char *end = pattern;
  if(*pattern == '(')
  {
    pattern++;
    while(*end != ')') end++;
  }
  end++;
  while(!(pattern == end) && *pattern != ')')
  {
    if(*end == '\0' && cur->childs[*pattern - 'a'] == cur)
      total++;
    else
      if(*end != '\0' && cur->childs[*pattern - 'a'] != NULL)
        total += count(cur->childs[*pattern - 'a'], end);

    pattern++;
  }
  return total;
}

int main()
{
  char buf[2000];
  unsigned int total;
  cin >> l >> d >> n;
  cin.ignore();
  
  root = new str_node;
  memset(&(root->childs), 0, sizeof(node *) * 30);
  
  for(i=0;i<d;i++)
  {
    cin.getline(buf, 20);
    regword(buf);
  }

  for(i=0;i<n;i++)
  {
    total = 0;
    cin.getline(buf, 1999);
    total = count(root, buf);
    cout << "Case #" << (i+1) << ": " << total << endl;
  }

  return 0;
}
