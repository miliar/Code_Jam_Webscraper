#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<b;i++)

using namespace std;

long long n,p,k,l;
long long re;
vector <long long> fr;


int main()
{
    fstream fin("A-large.in",ifstream::in);
    fstream fout("A-large.out",ofstream::out);
    fin >> n;
    for(int j=1;j<=n;j++)
    {
        re=0;
        fin >> p >> k >> l;
        fr.resize(l);
        rep(i,l) fin >> fr[i];
        sort(fr.begin(),fr.end());
        reverse(fr.begin(),fr.end());
        long long cp=0;
        rep(i,l)
        {
            if (i%k==0) cp++;
            re+=cp*fr[i];
        }
        fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    system("PAUSE");
    return 0;
}
