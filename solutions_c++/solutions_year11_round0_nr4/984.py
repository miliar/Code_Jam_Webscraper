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

using namespace std;

int t;
int N;
vector<int> arr;

int main()
{
    fstream fin("D-large.in",ifstream::in);
    fstream fout("D-large.out",ofstream::out);
    fin >> t;
    for(int j=1;j<=t;j++)
    {
		fin >> N;
		arr.resize(N);
		rep(i,N) fin >> arr[i];
		double re = 0.;
		rep(i,N) if (arr[i]!=i+1) re += 1.;
        fout << "Case #" << j << ": " << re << "\n";
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC << " s\n";
    system("PAUSE");
    return 0;
}
