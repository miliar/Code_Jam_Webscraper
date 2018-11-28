#include <iostream>
#include <fstream>

using namespace std;

#define cin fin
#define cout fout

ifstream fin("C-small-attempt0.in");
ofstream fout("c.out");

const int maxn = 101;

int c[maxn];

const int maxk = 5001;
int d[maxk];

int main()
{
    int num, t, now, i , j , k , n, tmp;
    cin >> t;
    for (num = 1;num <= t;num ++)
    {
        cin >> k >> n;
        for (i = 0;i <n;i ++)
         cin >> c[i];
        now = 0;
        memset(d, 0, sizeof(d));
        d[0] = 1;
        for (i = 1;i <= k;i ++)
        {
            j = k - i + 1;
            tmp = (i - 1) % j + 1;
  //        cout << tmp << " ";
            while (tmp > 0)
            {
                  do {
                      now ++;
                      if (now > k) now = 1;
                  } while (d[now] > 0);
                  tmp --;                  
            }
            d[now] = i;
//          cout << now << " "<< i << endl;
        }
        cout << "Case #" << num << ":";
        for (i = 0;i < n;i ++)
           cout << " " << d[c[i]];
        cout<< endl;
        
    }
    return 0;
}
