#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#define f(i, n) for(int i = 0; i < n; i++)
#define s(n) scanf("%d", &n)
#define sc(n) scanf("%s", &n)
#define fill(a, v) memset(a, v, sizeof a)
#define inf (int)1e9
using namespace std;

int freq[20][26], l, d, n;
long long ans;
string dict[5010], word;

main()
{
	s(l); s(d); s(n); getline(cin, word);
	f(i, d) getline(cin, dict[i]);
	
	f(z, n)
	{
         ans = 0;
         fill(freq, 0);
         getline(cin, word);
         int p = 0, len = word.length(), ptr = 0;
         
         while(p < len)
         {
              if(word[p] == '(')
              {
                 p++;
                 while(word[p] != ')') freq[ptr][word[p++] - 'a']++;
                 ptr++;
                 p++;
              }
              else freq[ptr++][word[p++] - 'a']++;
         }
         //for(char i = 'a'; i <= 'z'; i++) cout << i << " "; cout << endl;
         //f(i, l) {f(j, 26) cout << freq[i][j] << " "; cout << endl;}
         
         f(j, d)
         {
              long long x = 1;
              f(k, l)
              {
                   x *= freq[k][dict[j][k] - 'a']; 
                   //cout << freq[k][dict[j][k] - 'a'];
              }
              //cout << " " << dict[j] << " " << x << endl;
              ans += x;
         }
         
         printf("Case #%d: %d\n", z + 1, ans);
    }
}
