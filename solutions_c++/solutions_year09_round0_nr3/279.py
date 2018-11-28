#include<fstream>
using namespace std;

const int maxn = 500+3;
const string a = "welcome to code jam";

int cases, f[maxn][20], ans, x;
string t;

int main()
{
    ifstream input("3.in");
    ofstream output("3.out");
    input >> cases;
    getline(input,t);
    for (int k = 1; k <= cases; ++k){
      output << "Case #" << k << ": ";
      getline(input,t); ans = 0;
      for (int i = 0; i <= t.size(); ++i){
        for (int j = 0; j <= a.size(); ++j){
          f[i][j] = 0;
          if (t[i] == a[j]){
            if (j == 0) f[i][j] = 1;
            else
              for (int z = 0; z <= i-1; ++z)
                f[i][j] = (f[i][j]+f[z][j-1])%10000;  
          }       
        }
        ans = (ans+f[i][18])%10000;
      }
      x = 1000;
      while ((ans < x)&&(x > 1)){
        output << "0";
        x = x/10;      
      }
      output << ans << endl;
    }
    return 0;    
}
