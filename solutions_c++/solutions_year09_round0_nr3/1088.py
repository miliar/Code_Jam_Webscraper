#include <iostream>
#include <string>
using namespace std;

int f[600][20];
string welcome = "welcome to code jam";

void deal(string & query)
{
     memset(f, 0, sizeof(f));
     for (int i = 0; i < query.length(); ++i)
         if (query[i] == welcome[0])
            f[i][0] = 1;
     
     for (int i = 0; i < query.length(); ++i) {
         for (int j = 1; j < welcome.length(); ++j) {
             if (query[i] == welcome[j]) {
                 for (int k = 0; k < i; ++k) {
                     f[i][j] += f[k][j-1];
                     f[i][j] %= 10000;
                 }
             }
         }
     }
     
     int ans = 0;
     for (int i = 0; i < query.length(); ++i)
         ans += f[i][welcome.length() - 1], ans %= 10000;
         
     static int cases = 0;
     cases++;
     printf("Case #%d: ", cases);
     char temp[100];
     sprintf(temp, "%d", ans + 10000);
     printf("%s\n" , temp + 1);
}
     
int main()
{
    string query;
    int T;
    cin >> T;
    getline(cin, query);
    
    while (T--) {
          getline(cin, query);
          deal(query);
    }
}
                     
     
