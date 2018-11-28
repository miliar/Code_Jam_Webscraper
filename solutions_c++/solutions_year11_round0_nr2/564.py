#include<fstream>
#include<vector>
#include<string>
using namespace std;
ifstream in("B.in");ofstream out("B.out");
int main(){
    vector<char> my_list;
    vector<char> combinewith[26];
    vector<char> toform[26];
    vector<char> cancelwith[26];

    int t, T,c, C,d, D,n, N,l,m,toquit,i;
    string cc;
    in>>T;
    for (t=1;t<=T;t++){
        my_list.clear();
        for(i=0;i<26;i++){
            combinewith[i].clear();
            toform[i].clear();
            cancelwith[i].clear();
        }

        in>>C;
        for (c=0;c<C;c++){
            in>>cc;
            combinewith[cc[0]-'A'].push_back(cc[1]);
            combinewith[cc[1]-'A'].push_back(cc[0]);
            toform[cc[0]-'A'].push_back(cc[2]);
            toform[cc[1]-'A'].push_back(cc[2]);
        }

        in>>D;
        for (d=0;d<D;d++){
            in>>cc;
            cancelwith[cc[0]-'A'].push_back(cc[1]);
            cancelwith[cc[1]-'A'].push_back(cc[0]);
        }

        in>>N>>cc;
        my_list.push_back(cc[0]);
        for(n=1;n<N;n++){
            if (my_list.size()==0){
                my_list.push_back(cc[n]);
            }
            else{
                toquit=0;
                for(l=0;l<combinewith[cc[n]-'A'].size();l++){
                    if (my_list.back()==combinewith[cc[n]-'A'][l]){
                        my_list.pop_back();
                        my_list.push_back(toform[cc[n]-'A'][l]);
                        toquit=1;
                        break;
                    }
                }
                if (toquit==0){
                    for(m=0;m<my_list.size();m++){
                        for(l=0;l<cancelwith[cc[n]-'A'].size();l++){
                            if (my_list[m]==cancelwith[cc[n]-'A'][l]){
                                my_list.clear();
                                toquit=1;
                                break;
                            }
                        }
                        if (toquit) break;
                    }
                }
                if (toquit==0){
                    my_list.push_back(cc[n]);
                }
            }
        }
        out<<"Case #"<<t<<": [";
        for(m=0;m<my_list.size();m++){
            out<<my_list[m];
            if (m<my_list.size()-1) out<<", ";
        }
        out<<"]\n";
    }
    return 0;
}
