#include<iostream>
#include<string>
#include<fstream>
#define MAXD 30
#define BASE 10000
using namespace std;

int n;

struct bignumber
{
       long long digi[MAXD + 1];
       void clear()
       {
            for(int i = 0 ; i <= MAXD ; i++)
                    digi[i] = 0;
       }
       void fix()
       {
            for(int i = 0 ; i <= MAXD ; i++)
            {
                    while(digi[i] < 0)
                    {
                                  digi[i] += BASE;
                                  digi[i+1] --;
                    }
                    digi[i+1] += digi[i] / BASE;
                    digi[i] %= BASE;
            }
       }
       bignumber operator +(bignumber u)
       {
                 bignumber ret;
                 ret.clear();
                 for(int i = 0 ; i <= MAXD ; i++)
                         ret.digi[i] = digi[i] + u.digi[i];
                 ret.fix();
                 return ret;
       }
       bignumber operator -(bignumber u)
       {
                 bignumber ret;
                 ret.clear();
                 for(int i = 0 ; i <= MAXD ; i++)
                         ret.digi[i] = digi[i] - u.digi[i];
                 ret.fix();
                 return ret;
       }
       bignumber operator *(bignumber u)
       {
                 bignumber ret;
                 ret.clear();
                 for(int i = 0 ; i <= MAXD ; i++)
                         for(int j = 0 ; i + j <= MAXD ; j++)
                                 ret.digi[i+j] += digi[i] * u.digi[j];
                 ret.fix();
                 return ret;
       }
       bool operator > (bignumber u)
       {
            for(int i = MAXD ; i >= 0 ; i--)
            {
                    if(digi[i] > u.digi[i])
                               return true;
                    if(digi[i] < u.digi[i])
                               return false;
            }
            return false;
       }
       bignumber div(int t)
       {
                 bignumber ret;
                 ret.clear();
                 for(int i = MAXD ; i >= 0 ; i--)
                 {
                         if(i > 0)
                              digi[i-1] += BASE * (digi[i] % t);
                         ret.digi[i] = digi[i] / t;
                 }
                 return ret;
       }
       bool operator == (bignumber u)
       {
            for(int i = 0 ; i <= MAXD ; i++)
                    if(digi[i] != u.digi[i])
                               return false;
            return true;
       }
       void output()
       {
            for(int i = MAXD ; i >= 0 ; i--)
                    if(digi[i] > 0 || i == 0)
                    {
                               cout<<digi[i];
                               for(int j = i - 1 ; j >= 0 ; j--)
                               {
                                       for(int b = 10 ; b < BASE ; b *= 10)
                                               if(digi[j] < b)
                                                          cout<<0;
                                       cout<<digi[j];
                               }
                               break;
                    }
            cout<<endl;
       }
       void input(string s)
       {
            this -> clear();
            int t = 1 , loc = 0;
            for(int i = s.length() - 1 ; i >= 0 ; i--)
            {
                    digi[loc] += t * (s[i] - '0');
                    t *= 10;
                    if(t >= BASE)
                         loc ++ , t = 1;
            }
       }
}INF , ZERO , ONE , T[1001];

bignumber DIV(bignumber A , bignumber u)
{
          bignumber L = ZERO , R = INF , M;
          while(R - L > ONE)
          {

                  M = (L + R).div(2);

                  if(M * u > A)
                       R = M;
                  else
                       L = M;
          }

          return L;
}

bignumber MOD(bignumber A , bignumber u)
{
          bignumber t = DIV(A , u);
          return A - u * t;
}

bignumber gcd(bignumber A , bignumber B)
{
          if(A * B == ZERO)
               return A + B;
          return gcd(B , MOD(A , B));
}



int main()
{
    freopen("B.in" , "r" , stdin);
    freopen("B.out" , "w" , stdout);
    ios::sync_with_stdio(false);
    ZERO.clear();
    ONE.clear();
    INF.clear();
    ONE.digi[0] = 1;
    INF.digi[MAXD / 2] = 1;
    int C;
    cin>>C;
    for(int c = 1 ; c <= C ; c++)
    {
            cin>>n;
            bignumber G = ZERO;
            for(int i = 1 ; i <= n ; i++)
            {
                    string t;
                    cin>>t;
                    T[i].input(t);
                    if(G == ONE)
                         continue;
                    if(i > 1)
                    {
                         bignumber d;
                         if(T[i] > T[i - 1])
                                 d = T[i] - T[i - 1];
                         else
                             d = T[i - 1] - T[i];
                         G = gcd(G , d);
                    }
            }
            bignumber ANS = G - MOD(T[1] , G);
            if(ANS == G)
                   ANS = ZERO;
            cout<<"Case #"<<c<<": ";
            ANS.output();
    }
    return 0;
}
