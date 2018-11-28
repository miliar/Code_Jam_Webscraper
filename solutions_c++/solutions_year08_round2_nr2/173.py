#include <iostream>
#include <fstream>

using namespace std;

#define cin fin
#define cout fout


ifstream fin("B-small-attempt0.in");
ofstream fout("b.out");

const int maxp = 100000;
const int maxnum = 10000;
bool prime[maxp];
int root[maxnum];
int pl[100000], l;
long long ans;

void getPrime()
{
     l = -1;
     memset(prime, 0, sizeof(prime));
     int i = 3, j;
     for (i = 2;i < maxp;i ++)
      if (prime[i] == 0)
      {
         //          cout << i << endl;
        for (j = i + i ;j < maxp;j = j + i)
        {
            prime[j] = 1;
        }
        l ++;
        pl[l] = i;
      }
 }

int myMerge(int i, int j)
{
    if (root[root[i]] == root[i] && root[root[j]] == root[j]) {
     if (root[i] == root[j]) return root[i];
     else {
          ans --;
          root[root[i]] = root[j];
          return root[j];
     }
    } else {
     root[i] = myMerge(root[i], root[j]);
     return root[i];
    }
     
}
int main()
{
	int num, t;
	long long a, b, p, i , j, k;
	getPrime();
    //cout << "ok" << endl;	
    cin >> t;
	for (num = 1;num <= t;num ++)
	{
        cin >> a >> b >> p;
        
        for (i = 0;i <= b - a;i ++)
          root[i] = i;
        ans = b - a + 1;
        for (i = p;i <= b / 2;i ++)
         if (prime[i] == 0)
         {
           k = ((a - 1) / i + 1) * i;
           for (j = k + i;j <= b;j=j +i) {
//            cout << k << " " << j << endl;
            myMerge(k - a, j - a);
          }
         }
		cout << "Case #" << num << ": " << ans << endl;
	}
	fout.close();
	return 0;
}
