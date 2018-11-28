#include<fstream>
#include<map>
#include<string>
#include<iostream>
using namespace std;
int main(){
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in>>t;
    for(int i=0;i<t;i++){
            map<string,char> combtab;
            map<string,bool> notab;
            int c;
            in>>c;
            string aux,auxc;
            char auxb;
            for(int x=0;x<c;x++){
                    in>>aux;
                    auxb=aux[2];
                    aux=aux.substr(0,2);
                    combtab[aux]=auxb;
                    auxc="";
                    auxc+=aux[1];
                    auxc+=aux[0];
                    combtab[auxc]=auxb;
            }
            int d;
            in>>d;
            for(int x=0;x<d;x++){
                    in>>aux;
                    notab[aux]=true;
                    //cout<<aux<<endl;
                    auxc="";
                    auxc+=aux[1];
                    auxc+=aux[0];
                    notab[auxc]=true;
                    //cout<<auxc<<endl;
            }
            //system("pause");
            int n;
            in>>n;
            in>>aux;
            string re="";
            for(int x=0;x<n;x++){
                    re+=aux[x];
                    if(re.size()>1){
                                    while(re.size()>1&&combtab.count(re.substr(re.size()-2,2))){
                                                                       re=re.substr(0,re.size()-2)+combtab[re.substr(re.size()-2,2)];
                                    }
                                    for(int y=0;y<re.size()-1;y++){
                                            auxc="";
                                            auxc+=re[y];
                                            auxc+=re[re.size()-1];
                                            if(notab.count(auxc)){
                                                                  //cout<<"Era: "<<re<<" y por "<<auxc<<" ahora es: ";
                                                                  re="";
                                                                  //cout<<re<<" "<<y<<endl;
                                                                  //system("pause");
                                                                  break;
                                                                  //y=0;
                                            }
                                    }
                    }
            }
            //cout<<aux<<" "<<re<<endl;
            out<<"Case #"<<(i+1)<<": [";
            if(re.size()>0){
            for(int x=0;x<re.size()-1;x++){
                    out<<re[x]<<", ";
            }
            out<<re[re.size()-1]<<"]"<<endl;
            }else{
                  out<<"]"<<endl;
            }
            //system("pause");
    }
}
