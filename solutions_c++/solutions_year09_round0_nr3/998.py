#include <cstdio>
#include <cstring>

#define MAX_LEN  600
#define MAX_S_LEN  20

char* s = "welcome to code jam";
char t[MAX_LEN];

int n;
int count[MAX_LEN][MAX_S_LEN];

int match(int len)
{
  int slen = strlen(s);
  for(int j=0; j<slen; j++)
    count[0][j] = 0;
  for(int i=0; i<len; i++) {
    for(int j=0; j<slen; j++) {
      count[i+1][j] = count[i][j];
      if(t[i]==s[j]) {
	if(j!=0)
	  count[i+1][j] += count[i][j-1];
	else
	  count[i+1][j] += 1;
	count[i+1][j] %= 10000;
      }
    }
    /*
    for(int j=0; j<slen; j++)
      printf("%d ",count[i+1][j]);
    printf("\n");
    */
  }
  return count[len][slen-1];
}

main()
{
  char line[100];
  fgets(line,100,stdin);
  sscanf(line,"%d",&n);
  for(int i=0; i<n; i++) {
    fgets(t,MAX_LEN,stdin);
    int c = match(strlen(t));
    c %= 10000;
    sprintf(line,"%d",c+10000);
    printf("Case #%d: %s\n",i+1, line+1);
  }
}
