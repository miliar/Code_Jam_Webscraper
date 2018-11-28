#include <iostream>
#include <iomanip>
using namespace std;

char s[]="welcome to code jam";
char p[510];
int r[510][25];
int main () {
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);
    int z=strlen(s);
    int n; cin >> n;
    gets(p);
    for (int x=1; x<=n; x++) {
        memset(r, 0, sizeof r);
        r[0][0]=1; gets(p);
        int i;
        for (i=0; p[i]; i++) {
            for (int j=0; j<=z; j++)
                r[i+1][j]=r[i][j];
            for (int j=0; j<z; j++)
                if (p[i]==s[j])
                    r[i+1][j+1]=(r[i+1][j+1]+r[i][j])%10000;
        }
        cout << "Case #" << x << ": " << setw(4) << setfill('0') << r[i][z] << endl;
    }
    return 0;
}
