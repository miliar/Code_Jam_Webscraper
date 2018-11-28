#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
    fstream fin("A-large.in");
    fstream fout("output.txt");
    int tc,R,C;
    vector<string> fld;
    string str;
    bool mark[50][50];
    fin >> tc;
    for(int i = 0 ; i < tc; i++){
                fin >> R;
                fin >> C;
                //cout << R<<" "<<C<<endl;
                for(int row = 0; row < 50; row++)
                        for(int col = 0; col < 50; col++)
                                mark[row][col] = true;
                fld.erase(fld.begin(),fld.end());
                for(int j =0 ; j < R; j++){
                        
                        fin >> str;
                        fld.push_back(str);
                }
                //populate
                for(int row = 0; row < fld.size() - 1; row++)
                        for(int col = 0; col < fld[row].size() - 1; col++){
                                if(fld[row][col] == '#' && mark[row][col]){
                                                 if(fld[row][col+1] == '#' && mark[row][col+1]
                                                 && fld[row+1][col] == '#' && mark[row+1][col]
                                                 && fld[row+1][col+1] == '#' && mark[row+1][col+1]
                                                 ){
                                                                      fld[row][col] = '/';
                                                                      mark[row][col] = false;
                                                                      fld[row][col+1] = '\\';
                                                                      mark[row][col+1] = false;
                                                                      fld[row+1][col] = '\\'; 
                                                                      mark[row+1][col] = false;
                                                                      fld[row+1][col+1] = '/';
                                                                      mark[row+1][col+1] = false;
                                                                      }
                         //                                        cout <<"Case #"<<fld.size()<<" "<<row<<" "<<col<<endl;
                                }
                                
                        }
                //check validity?
                bool pos = true;
                for(int row = 0; row < fld.size() ; row++)
                        for(int col = 0; col < fld[row].size(); col++)
                                if(fld[row][col] == '#')pos=false;
                fout <<"Case #"<<i+1<<":"<<endl;
                if(!pos){
                         fout<<"Impossible"<<endl;
                }
                if(pos){
                        for(int row = 0; row < fld.size(); row++){
                            for(int col = 0; col < fld[row].size(); col++){
                                    fout<<fld[row][col];
                            }
                            fout<<endl;
                        }
                }
    }
    fin.close();
    fout.flush();
    fout.close();
    return 0;
}
