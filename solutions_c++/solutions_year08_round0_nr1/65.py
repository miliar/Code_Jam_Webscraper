#include <cstdio>
#include <iostream>
#include <cstring>
#include <map>

using namespace std;

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)
#define wipe(a,x) memset(a,x,sizeof(a))

#define MAX_SIZE 123
#define MAX_Q 1100
#define MAX_S 110

void read_line(char *s)
{
  char c;
  int pos=0;
  c=getchar();
  while (c!='\n' && c!=EOF)
  {
    s[pos++]=c;
    c=getchar();
  }
  s[pos]='\0';
}

int n_tests,test;
int i,j,k;
int n_engines,n_queries;
char buffer[MAX_SIZE];
map<string,int> M;
int v[MAX_Q];
int appear[MAX_S],cont,ans;

int main()
{
  scanf("%d",&n_tests);
  for_to(test,1,n_tests)
  {
    M.clear();
    scanf("%d",&n_engines);
    getchar();
    for_to(i,0,n_engines-1)
    {
      read_line(buffer);
      //printf("lido ->%s<-\n",buffer);
      M[buffer]=i;
    }  
    scanf("%d",&n_queries);
    getchar();
    //cout << "v: ";
    for_to(i,0,n_queries-1)
    {
      read_line(buffer);
      v[i]=M[buffer];
      //cout << v[i] << " ";
    }
    //cout << endl;
    wipe(appear,0);
    cont=ans=0;
    for_to(i,0,n_queries-1)
    {
      if (!appear[v[i]])
      {
        //cout << i << " -> "<< v[i] << endl; 
        ++cont;
      }
      appear[v[i]]=1;
      if (cont==n_engines)
      {
        //cout << "completed in " << i << endl;
        wipe(appear,0);
        appear[v[i]]=1;
        cont=1;
        ++ans;        
      }
    }
    printf("Case #%d: %d\n",test,ans);
  }
  return 0;
}
