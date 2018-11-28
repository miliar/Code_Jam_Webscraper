#include<iostream>
#include<queue>
using namespace std;

const int MAXN = 128;
const int INF = 1000000000;

struct vert
{
       char color;
       int position;
};

queue<int> o;
queue<int> b;
vert seq[MAXN];
int t,n;

inline int MyAbs(int value)
{
       if(value < 0) return value * (-1);
       else return value;
}

inline int MyMin(int value1, int value2)
{
       if(value1 < value2) return value1;
       else return value2;
}

int Result()
{
     int currentO = 1, nextO; if(!o.empty()) { nextO = o.front(); o.pop(); } else nextO = INF;
     int currentB = 1, nextB; if(!b.empty()) { nextB = b.front(); b.pop(); } else nextB = INF;
     int seconds = 0, step;

     for(int i = 0; i < n; i++)
     {
             if(seq[i].color == 'O')
             {
                  step = MyAbs(nextO - currentO) + 1;
                  if(nextB > currentB) currentB += MyMin(step, MyAbs(nextB - currentB));
                  else if(nextB < currentB) currentB -= MyMin(step, MyAbs(nextB - currentB));
                 
                  seconds += step;
                  currentO = nextO; if(!o.empty()) { nextO = o.front(); o.pop(); } else nextO = INF;                          
             }
             else if(seq[i].color == 'B')
             {
                  step = MyAbs(nextB - currentB) + 1;
                  if(nextO > currentO) currentO += MyMin(step, MyAbs(nextO - currentO));
                  else if(nextO < currentO) currentO -= MyMin(step, MyAbs(nextO - currentO));
                  
                  seconds += step;
                  currentB = nextB; if(!b.empty()) { nextB = b.front(); b.pop(); } else nextB = INF;
             }
     }
     return seconds; 
}

int main()
{
    scanf("%d", &t);
    int test = 1;
    while(test <= t)
    {
            scanf("%d", &n);
            
            for(int i = 0; i < n; i++)
            {
                  cin>>seq[i].color>>seq[i].position;
                  if(seq[i].color == 'O') o.push(seq[i].position);
                  else if(seq[i].color == 'B') b.push(seq[i].position);
            }
            
            printf("Case #%d: %d\n", test, Result());
            test++;
    }
    return 0;
}
