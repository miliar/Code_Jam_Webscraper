#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;

   int len, nall;
   vector<string> all;
 
   int brtests;

   string s;

   bool used[200][27];

void input()
{
   scanf("%d%d%d", &len, &nall, &brtests);

   for(int i = 0; i < nall; ++i){ cin>>s; all.push_back(s); }
}
int main()
{
   input();
   
   int cnt = 1;
   int ans = 0;

   for(;brtests;brtests--)
   {
    cin>>s;
 
    memset(used, 0, sizeof(used));

    int flag = 0;
    int pos = 0;
    int ans = 0;

    for(int j = 0; j < (int)s.size(); ++j)
    {
     if(s[j] == '(')
     {
      flag = 1;
     }
     else 
     if(s[j] == ')')
     {
      pos++;
      flag = 0;
     }
     else
     {
     // printf("in %d use %d\n",pos,(int)s[j]-'a');
      used[pos][s[j] - 'a']++;
      if(!flag)pos++;
     }
    }
    
    for(int i = 0; i < nall; ++i)
    {
     int j;
     for(j = 0; j < len; ++j)
     if(!used[j][all[i][j] - 'a'])break;
    
     if(j==len)ans++;
    }
    printf("Case #%d: %d\n",cnt,ans);
    cnt++;
   }
 return 0;
}
