#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int main(int argc, char *argv[])
{
    fstream ifin,fout;
    ifin.open("C-large.in");
    fout.open("output.txt");
    int tc,N,tempInt,total,minT;
    ifin >> tc;
    vector <int> cont;
    for(int i = 1 ; i < tc + 1; i++){
            ifin >> N;
            bool poss = true;
            cont.erase(cont.begin(),cont.end());
            total = 0;
            minT = 1000001;
            for(int j = 0 ; j < N; j++ ){
                    ifin >> tempInt;
                    if(tempInt < minT)minT = tempInt;
                    total += tempInt;
                    cont.push_back(tempInt);
            }
            for(int bitP = 21; bitP >=0; bitP-- ){
                            //cout <<"bitP" <<bitP<<endl;
                            int counter = 0;
                            tempInt = (1 << bitP);
                            for(int itr = 0 ; itr < cont.size(); itr++){
                                           if((cont[itr] & tempInt) == tempInt)
                                                        counter++;
                            }
                            if(counter%2 == 1){poss = false;
                            //cout <<"sal "<<bitP<<" "<<tempInt<<endl;
                            }
                            
            }
            if(!poss)fout <<"Case #"<<i<<": "<<"NO"<<endl;       
            if(poss)fout <<"Case #"<<i<<": "<<total - minT<<endl;       
    }
    //cin >> tc;
    return 0;
}
