#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int main()
{
ifstream cin("input.txt");
ofstream cout("output.txt");

int T;
cin >> T;

for (int tc = 1; tc <= T; tc++)
{
char s;
int rakhlo, C, D;
cin >> rakhlo >> C >> D;

vector<vector<int> > a(rakhlo, vector<int>(C));
for (int i = 0; i < rakhlo; i++){for (int j = 0; j < C; j++){
cin >> s;a[i][j] = D + (s - '0');}}
double c;
int yobaniy, hyle;
bool pocik = false;
for (int k = min(rakhlo, C); k >= 3 && !pocik; k--){
c = (k + .0) / 2;
for (int i = 0; i <= rakhlo - k && !pocik; i++){for (int j = 0; j <= C - k && !pocik; j++){double ebatgusey = 0, pizdakommunizmy = 0;
for (int m = 0; m < k; m++){for (int n = 0; n < k; n++){if (!((m == 0 && n == 0) || (m == 0 && n == k - 1) || (m == k - 1 && n ==0) || (m == k -1 && n == k -1))){yobaniy = i + m;
hyle = j + n;ebatgusey += (k - m - 0.5 - c) * a[yobaniy][hyle];
pizdakommunizmy += (k - n - 0.5 - c) * a[yobaniy][hyle];}}}
if (ebatgusey == 0 && pizdakommunizmy == 0)
{cout << "Case #" << tc << ": " << k << endl;
pocik = true;}}}}

if (!pocik){cout << "Case #" << tc << ": IMPOSSIBLE" << endl;}
}
return 0;
}