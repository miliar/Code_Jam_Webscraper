/*
NAME: Saketh Are
PROG: Magicka
LANG: C++
*/

#include<fstream>
#include<map>
#include<set>
#include<vector>
using namespace std;

ifstream fin("magicka.in");
ofstream fout("magicka.out");

int T, C, D, N, A, B;
char j, k, l;
map<char, int> ind;
set<char> comb[8];
set<char> opps[8];
map<pair<char,char>, char> combs;
char queue[128];

int main()
{
    ind['Q']=0; ind['W']=1; ind['E']=2; ind['R']=3;
    ind['A']=4; ind['S']=5; ind['D']=6; ind['F']=7;
    fin >> T;
    for(int q = 0; q<T; q++){
        A = B = 0;
        fin >> C;
        for(int c=0; c<8; c++){
             comb[c].clear();
             opps[c].clear();
             combs.clear();
        }
        for(int c=0; c<C; c++){
            fin >> j >> k >> l;
            comb[ind[j]].insert(k);
            comb[ind[k]].insert(j);
            combs[pair<char,char>(j,k)]=l;
            combs[pair<char,char>(k,j)]=l;
        }
        fin >> D;
        for(int d=0; d<D; d++){
            fin >> j >> k;
            opps[ind[j]].insert(k);
            opps[ind[k]].insert(j);
        }
        fin >> N;
        for(int n=0; n<N; n++){
            fin >> queue[B++];
            if(A+1 == B) continue;
            if(comb[ind[queue[B-1]]].find(queue[B-2])
                !=comb[ind[queue[B-1]]].end()){
                    queue[B-2]=combs[pair<char,char>(
                        queue[B-1], queue[B-2])];
                    B-=1;
                }
            else
                for(int c=0; A+c < B-1; c++)
                    if(opps[ind[queue[B-1]]].find(queue[A+c])
                        !=opps[ind[queue[B-1]]].end()){
                            A=B;
                            break;
                    }
        }
        fout << "Case #" << q+1 << ": [";
        for(int c=0; A+c < B; c++)
            fout << ((c>0)?", ":"") << queue[A+c];
        fout << "]" << endl;
    }
    return 0;
}
