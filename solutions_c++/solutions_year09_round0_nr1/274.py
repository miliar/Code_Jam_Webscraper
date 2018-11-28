#include<fstream>
using namespace std;

const int maxn = 500+3;

int l, m, n, k, y, ans;
char a[5000+1][15+1];
int b[15+1][26+1];
string t;

int main()
{
    ifstream input("1.in");
    ofstream output("1.out");
    input >> l >> m >> n; 
    for (int i = 1; i <= m; ++i)
      for (int j = 1; j <= l; ++j) input >> a[i][j];
    getline(input,t);
    for (int i = 1; i <= n; ++i){
      output << "Case #" << i << ": ";   
      getline(input,t); k = 0; ans = 0;
      memset(b, 0, sizeof(b));
      for (int j = 1; j <= l; ++j){
        if (t[k] == '('){
          ++k;
          while (t[k] != ')'){
            b[j][int(t[k])-int('a')] = 1;
            ++k;        
          }         
        }
        else {
          b[j][int(t[k])-int('a')] = 1;     
        }        
        ++k;
      }
      for (int x = 1; x <= m; ++x){
        y = 1;  
        for (int j = 1; j <= l; ++j)
          y &= b[j][int(a[x][j])-int('a')];
        if (y == 1) ++ans;    
      }
      output << ans << endl;
    }
    return 0;    
}
