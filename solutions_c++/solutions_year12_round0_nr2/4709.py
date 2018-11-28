#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>

using namespace std;

int main(){
    ifstream fin( "B-large.in" );
    ofstream fout;
    fout.open ("output.txt");

    int T, N, S, p, t;
    fin >> T;


    for(int k=1; k <= T; k++)
    {
        int total=0;
        fin >> N >> S >> p;
        for(int m=0; m < N; m++)
        {
            fin >> t;
            bool found = false, sFound=false;

            for(int i=p; i <= 10; i++){
                for(int j=10; j >= 0; j--){
                    if(abs(i-j)<=2){
                        for(int q=10; q >= 0; q--){
                            if(abs(i-q)<=2 && abs(j-q)<=2){
                                if(i+j+q==t){
                                    if((abs(i-j)!=2 && abs(i-q)!=2 && abs(j-q)!=2)){
                                        found = true;
                                        total++;

                                    }
                                    else if(S){
                                        sFound = true;
                                    }
                                }
                            }
                            if(found) break;
                        }
                    }
                    if(found) break;
                }
                if(found) break;
            }

            if(!found && sFound){
                S--;
                total++;
            }
        }

        fout << "Case #"<< k <<": " << total << endl;
    }

    return 0;
}
