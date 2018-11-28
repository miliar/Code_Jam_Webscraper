#include <iostream>
#include <algorithm>

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)

using namespace std;

#define MAX 1123


int n_tests,test;
int i,j,k;
char s[MAX];
char q[MAX];
int p[MAX],ans,block,n_blocks,len,temp;

int main()
{
  scanf("%d",&n_tests);
  for_to(test,1,n_tests)
  {
    scanf("%d",&k);
    scanf(" %s",s);
    for_to(i,1,k)
    {
      p[i]=i;
    }
    ans=MAX;
    n_blocks=strlen(s)/k;
    //cout << "n_blocks=" << n_blocks << endl;
    do
    {
      temp=0;
      for (block=1; block<=n_blocks; ++block)
      {
        //cout << "from " << (block-1)*k << " to " << block*k-1 << endl;
        for (i=(block-1)*k; i<=block*k-1; ++i)
        {
          q[i]=s[p[i-(block-1)*k+1]+(block-1)*k-1];
          //cout << " arg " << i-(block-1)*k+1 << "-> " << p[i-(block-1)*k+1] << endl;
          //cout << "put " << q[i] << " from " << p[i-(block-1)*k+1]+(block-1)*k-1 << endl;
          if (i==0 || q[i]!=q[i-1]) ++temp;
        }
      }
      q[n_blocks*k]='\0';
      //cout << q << endl << ":" << temp << endl;
      ans=min(ans,temp);
    }  while (next_permutation(p+1,p+1+k));
    printf("Case #%d: %d\n",test,ans); 
  }
  return 0;
}
