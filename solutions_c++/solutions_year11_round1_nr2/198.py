#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
using namespace std;
typedef vector<int> VI;
typedef map<VI,vector<string> > MS;

VI getlist(string str,char fi){
    VI ve;
    for(int i=0;i<str.size();i++){
        if(str[i]==fi) ve.push_back(i);
    }
    return ve;
}
int main(){
    int T;
    cin>>T;
    for(int iff=1;iff<=T;iff++){
        printf("Case #%d:",iff);
//        map<char,MS> maps;
//        for(char i='a';i<='z';i++){
//            maps[i]=MS();
//        }
        int N,M;
        cin>>N>>M;
        vector<string> strs(N);
        vector<vector<string> > lenstrs(11,vector<string>());
        for(int i=0;i<N;i++){
            cin>>strs[i];
            lenstrs[strs[i].size()].push_back(strs[i]);
        }
//        for(int i=0;i<N;i++){
//            for(char j='a';j<='z';j++){
//                VI vi=getlist(strs[i],j);
//                if(maps[j].find(vi)==maps[j].end()){
//                    vector<string> vs;
//                    vs.push_back(strs[i]);
//                    maps[j][vi]=vs;
//                }else maps[j][vi].push_back(strs[i]);
//            }
//        }
        for(int ix=0;ix<M;ix++){
            string list;
            cin>>list;
            string retstr;
            int minpo=-1;
            for(int i=0;i<N;i++){
                string nows=strs[i];
                int po=0;
                vector<string> remain=lenstrs[nows.size()];
                for(int j=0;j<list.size();j++){
                    bool isco=false;
                    for(int k=0;k<remain.size();k++){
                        for(int l=0;l<remain[k].size();l++){
                            if(remain[k][l]==list[j]){
                                isco=true;
                            }
                        }
                    }
                    if(!isco) continue;
                    else{
                        bool nowisco=false;
                        for(int k=0;k<nows.size();k++){
                            if(nows[k]==list[j]) nowisco=true;
                        }
                        if(!nowisco) po++;
                        vector<string> nextremain;
                        VI nowsli=getlist(nows,list[j]);
                        for(int k=0;k<remain.size();k++){
                            if(nowsli==getlist(remain[k],list[j])){
                                nextremain.push_back(remain[k]);
                            }
                        }
                        remain=nextremain;
                    }
                    if(remain.size()==1) break;
                }
                if(po>minpo){
                    minpo=po;
                    retstr=nows;
                }
            }
            printf(" %s",retstr.c_str());
        }
        printf("\n");
    }
}
