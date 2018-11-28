#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

typedef long long int huge;
const int inf=0x3f2f1f0f;
const huge hinf=0x3fff2fff1fff0fffll;

#define foreach(i...) _foreach(i)
#define all(v) v.begin(), v.end()
#define _foreach(i, b, e) for(__typeof(b) i=b; i!=e; i++)

class tree {
public:
  tree *leaf[26];
  tree()
  {
    for(int i=0; i<26; ++i)
      leaf[i]=NULL;
  }
  tree*& operator[](int t)
  {
    return leaf[t];
  }
};

tree* root = new tree();

void insert(tree* r, char *str)
{
  if (*str!=0)
    {
      if ((*r)[*str-'a']==NULL)
	(*r)[*str-'a']=new tree();
      insert((*r)[*str-'a'], str+1);
    }
}

int test(tree* r, string *t)
{
  if (t[0]=="")
    return 1;
  int c=0;
  for(unsigned int i=0; i<t[0].size(); ++i)
    if ((*r)[t[0][i]-'a']!=NULL)
      c+=test((*r)[t[0][i]-'a'], t+1);
  return c;
}

string read()
{
  char ch[32];
  scanf(" %c", ch);
  if (ch[0]=='(')
    scanf("%[a-z])", ch);
  else
    ch[1]=0;
  return string(ch);
}
int main()
{
  int l, d, n;
  char str[32];
  string word[16];
  scanf(" %d %d %d", &l, &d, &n);
  word[l]="";
  for(int i=0; i<d; ++i)
    {
      scanf(" %s", str);
      insert(root, str);
    }
  for(int i=1; i<=n; ++i)
    {
      for(int j=0; j<l; ++j)
	word[j]=read();
      printf("Case #%d: %d\n", i, test(root, word));
    }
  return 0;
}

