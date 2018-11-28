#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <list>
#include <utility>
using namespace std;

int main(int argc, char* argv[])
{
    if(argc < 3)
        return 1;
    FILE* in = fopen(argv[1], "r");
    FILE* out = fopen(argv[2], "w");

    int T;
    int S,X,R,RT,N;
    fscanf(in, "%d", &T);
    for(int t=0; t<T; t++){
        double time = 0.0;
        fscanf(in, "%d %d %d %d %d", &X, &S, &R, &RT, &N);
        int x = 0;
        list<pair<int,int> > walkways;//length, speed. Sorted by speed
        for(int n=0; n<N; n++){
            int b,e,w;
            fscanf(in, "%d %d %d",&b,&e,&w);
            bool inserted = false;
            x += e-b;
            for(std::list<std::pair<int, int> >::iterator iter = walkways.begin(); iter != walkways.end(); iter++){
                if(iter->second > w){
                    walkways.insert(iter, pair<int,int>(e-b, w));
                    inserted = true;
                    break;
                }
            }
            if(!inserted)
                walkways.insert(walkways.end(), pair<int,int>(e-b,w));
        }
        walkways.insert(walkways.begin(), pair<int,int>(X-x, 0));

        double rt = (double) RT;
        for(list<pair<int, int> >::iterator iter = walkways.begin(); iter != walkways.end(); iter++){
            if(rt > 0.0){
                double wt = (double)iter->first / (double)(iter->second + R);
                rt -= wt;
                if(rt < 0.0){
                    wt -= ((double)(R-S) * rt) / (double)(iter->second + S);//subtract false runtime
                }
                time += wt;
            }else{
                time += (double)iter->first / (double)(iter->second + S);
            }
        }

        fprintf(out, "Case #%d: %.9lf\n", t+1, time);
    }
    return 0;
}
