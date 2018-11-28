#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <deque>
#include <sstream>

using namespace std;

deque <int> ora;
deque <int> bl;
deque <char> turn;

int main(int argc, char *argv[])
{
    int tc;
    fstream ifin;
    ifin.open("A-large.in");
    string s;
    getline(ifin, s, '\n');
    stringstream parser1(s);
    parser1 >> tc;
    tc++;
    fstream ofin;
    ofin.open("output.txt");
    for(int ii = 1 ; ii < tc; ii++){

                getline(ifin, s, '\n');
//                cout <<s<<endl;
                stringstream parser(s);
                char tempChar;
                int tempInt;
                ora.erase(ora.begin(),ora.end());
                bl.erase(bl.begin(),bl.end());
                turn.erase(turn.begin(),turn.end());
                parser >> tempInt;
                while(parser >> tempChar >> tempInt){
                             turn.push_back(tempChar);
                             if(tempChar == 'O')
                                         ora.push_back(tempInt);
                              else       bl.push_back(tempInt);                          
                }
                int step = 0;
                int pOra = 1 , pBl = 1;
                    //cout << "salam3"<<endl;
                while(!turn.empty()){
                                         //cout << "salam2"<<endl;
                                       
                                       if(turn.at(0) == 'O'){
                                                      //cout << "salam5"<<endl;
                                                if(ora.at(0) == pOra){
                                                          ora.pop_front();
                                                          turn.pop_front();
                                                } else if(ora.at(0) > pOra)pOra++;
                                                 else if (ora.at(0) <pOra)pOra--;
                                                 
                                                 if(bl.size() > 0 && bl.at(0) > pBl)pBl++;
                                                 else if(bl.size() > 0 && bl.at(0) < pBl)pBl--;
                                       }
                                       else{
                                             //cout << "salam6"<<endl;
                                            if(bl.at(0) == pBl){
                                                        //cout << "salam6"<<endl;
                                                          bl.pop_front();
                                                          turn.pop_front();
                                                } else if(bl.at(0) > pBl)pBl++;
                                                 else if (bl.at(0) <pBl)pBl--;
                                                 
                                                 if(ora.size() > 0 && ora.at(0) > pOra)pOra++;
                                                 else if(ora.size() > 0 && ora.at(0) < pOra)pOra--;
                                       }
                                        //cout << "salam7"<<endl;
                                       step++;
                }
                ofin <<"Case #"<<ii<<": "<<step<<endl;
    }
    //cout << "salam"<<endl;
    ofin.flush();
    ofin.close();
  //  cin >> tc;
    return 0;
}
