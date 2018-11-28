// alien language

#include <stdio.h>
#define MAXNUM 5050
#define MAXLEN 17
#define PATLEN (MAXLEN*50)

int len,n,qn;
char str[MAXNUM][MAXLEN];
char pat[PATLEN];
bool allow[PATLEN][26];


inline void Process(char *p)
{
  int i,j;
  for(i=0;i<len;i++)
    for(j=0;j<26;j++)
      allow[i][j]=0;
  for(i=j=0;i<len;i++) {
    if(p[j]=='(') {
      for(j=j+1;p[j]!=')';j++)
	allow[i][p[j]-'a']=1;
      j++;
    } else {
      allow[i][p[j]-'a']=1;
      j++;
    }
  }
}

inline bool Valid(char *s)
{
  int i;
  for(i=0;i<len;i++)
    if(!allow[i][s[i]-'a']) return 0;
  return 1;
}

int main(void)
{
  int i,casenum,c;
  scanf("%d %d %d",&len,&n,&qn);
  for(i=0;i<n;i++)
    scanf("%s",str[i]);
  for(casenum=1;casenum<=qn;casenum++) {
    scanf("%s",pat);
    Process(pat);
    c=0;
    for(i=0;i<n;i++)
      if(Valid(str[i])) c++;
    printf("Case #%d: %d\n",casenum,c);
  }
  return 0;
}
