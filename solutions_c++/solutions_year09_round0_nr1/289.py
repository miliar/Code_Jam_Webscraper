#include <iostream>
using namespace std;

bool v[20][30];
char w[6000][20];
char s[1000];
int l,d,n;

int here(char *s)
{
  for(int i=0;i<l;i++) if (!v[i][s[i]-'a']) return false;
  return true;
}

main()
{
  cin >> l >> d >> n;
  for(int i=0;i<d;i++) scanf("%s",w[i]);

  for(int i=1;i<=n;i++)
  {
    memset(v,0,sizeof(v)); scanf("%s",s);
    int pos=0; bool inb=false;
    for(int j=0;s[j];j++)
    {
      int c=s[j]-'a';
      if (isalpha(s[j]))
      {
        v[pos][c]=true;
        if (!inb) pos++;
      }
      else if (s[j]=='(') inb=true;
      else if (s[j]==')') { inb=false; pos++; }
    }

    int t=0; for(int j=0;j<d;j++) if (here(w[j])) t++;
    printf("Case #%d: %d\n",i,t);
  }
}
