/*
NAME: Saketh Are
PROG: Bot Trust
LANG: C++
*/

#include<fstream>
using namespace std;

ifstream fin("bottrust.in");
ofstream fout("bottrust.out");

int T, N, loc;
char which;
int locs[2];
int last[2];
int tyme=0;

int main()
{
    fin >> T;
    for(int q = 0; q<T; q++){
        fin >> N;
        locs[0]=locs[1]=1;
        last[0]=last[1]=0;
        tyme=0;
        for(int c=0; c<N; c++){
            fin >> which >> loc;
            int i=((which=='B')?1:0);
            last[i]=max(tyme+1,
              last[i]+abs(loc-locs[i])+1);
            locs[i]=loc;
            tyme=max(tyme,last[i]);
        }
        fout << "Case #" << q+1 << ": "
             << tyme << endl;
    }
    return 0;
}
