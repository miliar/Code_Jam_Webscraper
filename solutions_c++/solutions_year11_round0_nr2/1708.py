#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    int nn;
    scanf("%d",&nn);
    for(int ix=1;ix<=nn;ix++){
        int c;
        scanf("%d ",&c);
        vector<pair<pair<int,int>,int> >  comb(c);
        for(int i=0;i<c;i++){
            char c1,c2,c3;
            scanf("%c%c%c ",&c1,&c2,&c3);
            comb[i]=make_pair(make_pair(c1,c2),c3);
        }
        int d;
        scanf("%d ",&d);
        vector<pair<int,int> > oppo(d);
        for(int i=0;i<d;i++){
            char c1,c2;
            scanf("%c%c ",&c1,&c2);
            oppo[i]=make_pair(c1,c2);
        }
        int n;
        scanf("%d ",&n);
        vector<char> list;
        for(int i=0;i<n;i++){
            char ins;
            scanf("%c",&ins);
            if(list.empty()){
                list.push_back(ins);
            }else{
                bool isch=false;
                for(int j=0;j<c;j++){
                    char f1=comb[j].first.first,f2=comb[j].first.second,to=comb[j].second;
                    if((list.back()==f1&&ins==f2)||(ins==f1&&list.back()==f2)){
                        list.pop_back();
                        list.push_back(to);
                        isch=true;
                        break;
                    }
                }
                if(!isch){
                    bool iscl=false;
                    for(int j=0;j<d;j++){
                        char c1=oppo[j].first,c2=oppo[j].second;
                        if((ins==c1&&find(list.begin(),list.end(),c2)!=list.end())||(ins==c2&&find(list.begin(),list.end(),c1)!=list.end())){
                            list.clear();
                            iscl=true;
                            break;
                        }
                    }
                    if(!iscl) list.push_back(ins);
                }
            }
        }
        scanf("\n");
        printf("Case #%d: [",ix);
        if(list.empty()) printf("]\n");
        else {
            for(int i=0;i<(int)list.size()-1;i++){
                printf("%c, ",list[i]);
            }
            printf("%c]\n",list.back());
        }
    }
}
