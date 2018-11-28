#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
    int tc;
    fstream fin("A-large.in");
    fstream fout("output.txt");
    fin >> tc;
    vector <string> db;
    string str;
    long double wp[100];
    long double wp1[100];
    long double wp2[100];
    long double owp[100];
    long double oowp[100];
    long double temp,tempC,total;
    
    for(int i = 0 ; i < tc; i++){
            int sz;
            db.erase(db.begin(),db.end());
            fin >> sz;
            for(int j = 0; j < sz; j++){
                    fin >> str;
                    db.push_back(str);        
            }
            for(int j = 0; j < sz; j++){
                    temp = tempC = 0;
                    for(int t = 0 ; t < db[j].size(); t++){
                            if(db[j][t] == '1')temp++;
                            if(db[j][t] == '1' || db[j][t] == '0')tempC++;
                    }
                    wp[j] = temp / tempC;
                    wp1[j] = temp;
                    wp2[j] = tempC;
                    //cout<<"wp "<<wp[j]<<endl;
            }
            //OWP[j]
            for(int j = 0; j < sz; j++){
                    temp = tempC = 0;
                    total = 0;
                    for(int t = 0 ; t < db[j].size(); t++){
                            if(t == j)continue;
                            if(wp2[t] == 1)continue;
                            if(db[j][t] == '0') {
                                        total += (wp1[t] - 1) / (wp2[t] -1);//TODO what if 0?
                                        tempC++;
                            }
                            else if(db[j][t] == '1'){ 
                                 total += wp1[t] / (wp2[t] -1);
                                 tempC++;
                                 }
                    }
                    owp[j] = total / tempC;
                    //cout<<"owp "<<owp[j]<<endl;
            }
            //OOWP
            for(int j = 0; j < sz; j++){
                    total = tempC = 0;
                    
                    for(int t = 0; t < db[j].size(); t++){
                            if(t == j)continue;
                            if(db[j][t] != '.'){
                                        tempC++;
                                        total += owp[t];            
                            }
                    }
                    oowp[j] = total / tempC;
                    //cout<<"oowp "<<oowp[j]<<endl;
            }
            fout <<"Case #"<<i+1<<":\n";
            for(int j = 0; j < sz; j++){
                    fout<< .25 * wp[j]+ .5*owp[j] + .25*oowp[j]<<endl;
            }
    }
    fin.close();
    fout.flush();
    fout.close();
    return 0;
}
