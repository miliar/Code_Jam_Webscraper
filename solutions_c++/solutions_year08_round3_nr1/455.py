#include <iostream>
#include <fstream>

using namespace std;

int N, P, K, L,temp;
int f[1001];
int keys[1001][1001];

static int maxindex(int* f, int length){
    int result=0;
    for (int i=0;i<length;i++){
        if (f[i]>f[result]){
            result=i;
        }
    }
    return result;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.txt");

    fin >> N;

    for(int nn=1;nn<=N;nn++){
        fin >> P >> K >> L;

        if (L>(K*P)){
            cout << "Case #" << nn << "Impossible"<<endl;
            for (int i=0;i<L;i++){
                fin>>temp;
            }
        } else {
            for ( int i=0;i<L;i++){
                fin >> f[i];
            }
            long long numpresses=0;
            for (int level=0;level<P;level++){
                for (int key=0;key<K;key++){
                    int letter=maxindex(f,L);
                    if (f[letter]>0){
                        numpresses+=f[letter]*(level+1);
                        f[letter]=0;
                    }
                }
            }

            fout << "Case #" << nn << ": "<<numpresses <<endl;
        }
    }


    return 0;
}
