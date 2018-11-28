#include<iostream>
#include<map>
#include<set>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<stack>
#include<queue>
#include<cstring>
#include<climits>

using namespace std;

int main()
{

freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
     
  int t;
  scanf("%d",&t);
  getchar();
  string key="yhesocvxduiglbkrztnwjpfmaq";

  for(int tt=0;tt<t;tt++)
    {
      char a[105];
      cin.getline(a,105);

      for(int i=0;i<strlen(a);i++)
	{ 
	  if(a[i]!=' ')
	  a[i]=key[a[i]-'a'];
	}
      cout<<"Case #"<<tt+1<<": "<<a<<"\n";

    }


  return 0;
}
