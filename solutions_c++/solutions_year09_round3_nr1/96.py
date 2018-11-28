#include<iostream>
#include<string>
#include<cstring>

using namespace std;

   int used[100];
   int what[600];
   int mas[600];

   string s;
  int br = 1;

   int ans[600];
   int len;

void multi(int num)
{
   int i, all, ost = 0;
   for( i = 0; i < len; ++i)
   {
    all = ans[i] * num + ost;
    ans[i] = all%10;
    ost = all/10;
   }    
   while(ost){ans[len++] = ost % 10; ost/=10;}
}
void Plus(int num)
{
    int i, all, ost = 0;
   for( i = 0; i < len; ++i)
   {
    all = ans[i] + num + ost;
    ans[i] = all%10;
    ost = all/10;
    num = 0;
   }    
   while(ost){ans[len++] = ost % 10; ost/=10;}
}
void print()
{
    //while(len > 0 && ans[len - 1] == 0)len--;
    for( int i = len - 1; i >= 0; --i)cout<<ans[i]; cout<<"\n";
}
void solve()
{
   cin>>s;
   int i;

   memset(used, 0, sizeof(used));
   memset(what, -1, sizeof(what));
   memset(ans, 0, sizeof(ans));
   len = 1;

   /*for( i = 0; i < (int)s.size(); ++i )
   if(s[i] >= '0' && s[i] <= '9')used[s[i]-'0'] = 1;*/

   for( i = 0; i < (int)s.size(); ++i)
   {
    if(what[(int)s[i]]!=-1){mas[i] = what[(int)s[i]]; continue;}

    int j;
    if(i == 0) j = 1;
    else j = 0;

    while(used[j])j++;
    used[j] = 1;
    what[(int)s[i]] = j; mas[i] = j;
   }

   int maxx = 0;
   for(i = 0; i < (int)s.size(); ++i){maxx = max(maxx, mas[i]); }
   maxx++;

   for( i = 0 ; i < (int)s.size(); ++i) 
    {
     multi(maxx);
     //printf("umnojix po %d i polu4ix: ",maxx); print();
     Plus(mas[i]);
     //printf("pribavix %d i polu4ix: ",mas[i]); print();
    }
cout<<"Case #"<<br<<": ";
print();
br++;
}
int main()
{
   int t;
   cin>>t;
   for(;t;t--)solve();
return 0;
}
