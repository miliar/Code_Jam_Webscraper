/*
Author:MarsChenly
Date:2011.06.04
*/
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std;

const int maxn(1005);
int prime[maxn],tot(0);
bool yes[maxn];
int num[maxn],num1[maxn];

long long gcd(long long a,long long b)
{
      if (a == 0) return b;
      return gcd(b%a,a);
}

void prepare()
{
      memset(yes,1,sizeof(yes));
      yes[0] = false; yes[1] = false;
      for (int i(2);i<maxn;i++)
      if (yes[i])
      {
            prime[++tot] = i;
            int j =i +i;
            while (j < maxn)
            {
                  yes[j] =false;
                  j = j +i;
            }
      }
}

void work(int x)
{
      memset(num1,0,sizeof(num1));
      for (int i(1);i<=tot;i++)
      {
            if (x == 1) continue;
            while (x % prime[i] == 0)
            {
                  num1[i]++;
                  x = x / prime[i];
            }
      }
}

int main()
{
      freopen("C.in","r",stdin);
      freopen("C.out","w",stdout);
      int task,cases(0);
      scanf("%d",&task);
      prepare();
      while (task--)
      {
            //int ans(0);
            int n;
            scanf("%d",&n);
            int s(0);
            memset(num,0,sizeof(num));
            for (int i(1);i<=n;i++)
            {
                  if (i == 1)
                  {
                        s++;
                        continue;
                  }
                  work(i);
                  bool flag(false);
                  for (int j(1);j<=tot;j++)
                  {
                        if (num1[j] > num[j])
                        {
                              num[j] = num1[j];
                              flag = true;
                        }
                  }
                  if (flag) s++;
            }
            int maxx;
            maxx = s;
            s = 0;
            memset(num,0,sizeof(num));
            for (int i(n);i>=2;i--)
            {
/*                  if (i == 1)
                  {
                        s++;
                        continue;
                  }
            */
                  work(i);
                  bool flag(false);
                  for (int j(1);j<=tot;j++)
                  {
                        if (num1[j] > num[j])
                        {
                              num[j] = num1[j];
                              flag = true;
                        }
                  }
                  if (flag) s++;
            }
            int minx;
            if (n == 1) minx = 1; 
                  else minx = s;
            cout << minx << " " << maxx << endl;
            printf("Case #%d: %d\n",++cases,maxx- minx);
      }
//      system("pause");
      return 0;
}
