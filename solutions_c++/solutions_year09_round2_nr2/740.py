#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int dig[10];

bool finish(string s, string O, bool flag)
{
 int insi[10];
 
 for (int i = 1; i <= 9; i++)
  insi[i] = dig[i];
 
 int h = 0;
 if (!flag) h = 1; 
 
 while (s.size() < O.size() + h)
 {
  bool tak = false;
  for (int d = '9'; d >= '1'; d--)
   if (insi[ d - '0' ] > 0)
   {
    insi[d - '0']--;
    tak = true;
    s += d;
    break;
   }
   
  if (!tak) s += '0';
 }
 
 for (int d = 1; d <= 9; d++)
  if (insi[d] > 0)
   return false;
 
 if (!flag) return true;
 
 return s > O;
}

string construct(string N, string st, bool flag)
{
 string ans = st;
 
 for (int i = 0; i < N.size(); i++)
 {
  for (char d = '0'; d <= '9'; d++)
  {
   if (d == '0' && i == 0 && flag) continue;
   
   if (d == '0')
   {
    string temp = ans + '0';
    
    if (finish(temp, N, flag))
    {
     ans = temp;
     break;
    }
   }
   else
   {   
    int di = d - '0';
    if (dig[di] < 1) continue;
   
    dig[di]--;
    string temp = ans + d;
    
    if (!finish(temp, N, flag))
     dig[di]++;
    else
    {
     ans = temp;
     break;
    }
   }
  }
 }
 
 return ans;
}

string solve(string N)
{
 memset(dig, 0, sizeof(dig));

 for (int i = 0; i < N.size(); i++)
  dig[ N[i] - '0' ]++;
  
 string ans = construct(N, "", true);
 
 if (ans != "") return ans;
 
 for (int st = 1; st <= 9; st++)
 {
  if (dig[st] < 1) continue;
  
  dig[st]--; string help = ""; help += char('0' + st);
  string temp = construct(N, help, false);
  if (temp != "")
  {
   ans = temp;
   break;
  }
  dig[st]++;
 }
 
 return ans;
}

int main()
{
 int T;
 cin >> T;
 
 for (int t = 0; t < T; t++)
 {
  string s; cin >> s;
  printf("Case #%d: %s\n", t + 1, solve(s).c_str());
 }     
 
 return 0;
}
