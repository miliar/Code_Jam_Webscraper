#include <fstream>
#include <cstring>
#include <cstdlib>

using namespace std;

char s[100], ss[100];

int main()
{
    ifstream f("a.in");
    ofstream g("a.out");
    int T, t = 0, A, B;
    f >> T;
    while(t++ < T){
        f >> A >> B;
        int nr = 0;
        for(int i = A; i <= B; ++i)
            for(int j = i + 1; j <= B; ++j){
                itoa(i, s, 10);
                strcpy(ss, s);
                strcat(ss, s);
                itoa(j, s, 10);
                if(strstr(ss, s))
                    nr++;
            }
        g << "Case #" << t << ": " << nr << endl;
    }

    return 0;
}
