#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
using namespace std;
int main (){
   ifstream fin ("B-large.in");
    ofstream fout ("B-large.out");
    int T;
    fin >>T;
    cout <<T<<endl;
    for (int i=1; i<=T; i++){
        vector <string> res;
        int C;
        fin >>C;
        //cout <<C<<endl;
        map <string, string> m;
        map <string, string> d;
        for (int k=0; k<C; k++){
            string a;
            fin >>a;
        //    cout <<a<<endl;
            string ini="";
            ini+=a[0]; 
            ini+=a[1];
            string fini=""; fini+=a[2];
            m[ini]=fini; 
            swap(ini[0],ini[1]);
            m[ini]=fini;
        }
        int D;
        fin >>D;
      //  cout <<D<<endl;
        for (int k=0; k<D; k++){
            string a;
            fin >>a;
        //cout <<a<<endl;
            string ini="";
            ini+=a[0]; ini+=a[1];
            d[ini]="!"; swap(ini[0],ini[1]);
            d[ini]="!";
        }
        int N; fin >>N;
        //cout <<N<<endl;
        string ex; fin >>ex;
      //  cout <<ex<<endl;
        for (int k=0; k<N; k++){
            string el="";
            el+=ex[k];
            res.push_back(el);
            string combi="";
            if (res.size()>1){
                combi=(string)(res[res.size()-1])+(string)(res[res.size()-2]);
                if (m.count(combi)!=0){
                   res.pop_back(); res[res.size()-1]=m[combi];
                }/*
                for (int is=0; is<res.size(); is++) cout <<res[is]<<" ";
                cout <<endl;*/
                for (int j=0; j<res.size()-1; j++){
                    string tet="";
                    tet+=res[j];
                    tet+=string(res[res.size()-1]);
                    if (d.count(tet)!=0){
                        res.clear();
                        j=res.size();
                        break;
                    }
                }
                //system ("pause");
            }
            /*for (int is=0; is<res.size(); is++) cout <<res[is]<<" ";
            cout <<endl;*/
           // system ("pause");
        }
       // cout <<"-----"<<endl;
        fout <<"Case #"<<i<<": [";
        for (int is=0; is<res.size(); is++){
            fout <<res[is];
            if (is<res.size()-1) fout <<", ";
        }
        fout <<"]"<<endl;
    }
   // system ("pause");
}
