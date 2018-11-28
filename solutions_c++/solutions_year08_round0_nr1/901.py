#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> machine;
vector<string> query;
int n;

void work(int cases)
{
   int s = machine.size();
   int q = query.size();
   int now = 0, ans = 0;
   string str = "";
   bool f[100];
   int i, j, k;
   i = 0;
   while(i < query.size())
   {
      int ns = 0;
      memset(f, false, sizeof(f));
      for(j = i; j < query.size(); j++)
      {
         for(k = 0; k < machine.size(); k++)
         {
            if(machine[k] == query[j] && query[j] != str && f[k]== false)
            {
               f[k] = true;
               ns++;
            }
         }
         if( (str == "" && ns == machine.size()) || (str != "" && ns == machine.size() - 1))
         { 
            now = j;
            ans++;
            break;
         }
      }
      if (!((str == "" && ns == machine.size()) || (str != "" && ns == machine.size() - 1))) break;
      
      i = now;
      str= query[now];
      i++;
   }
   cout << "Case #" << cases << ": " << ans << endl;
}
void readIn()
{
   int i, j;
   cin >> n;
   for(i = 1; i <= n; i++)
   {
      int s , q;
      cin >> s ;
      string temp;
      getline(cin, temp);
      for(j = 0; j < s; j++)
      {
         string str;
         getline(cin, str);
         machine.push_back(str);
      }
      
      cin >> q;
      getline(cin, temp);
      for(j = 0; j < q; j++)
      {
         string str;
         getline(cin, str);
         query.push_back(str);
      }
      work(i);
      machine.clear();
      query.clear();
   }
}
int main()
{ 
   freopen("A-large.in","r",stdin);
   freopen("save3.out","w",stdout);
   
   readIn();
   return 0;
}
