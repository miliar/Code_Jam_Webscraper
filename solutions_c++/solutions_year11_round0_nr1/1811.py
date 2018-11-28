#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int main(){
    int nn;
    scanf("%d\n",&nn);
    for(int ix=1;ix<=nn;ix++){
        int n;
        scanf("%d ",&n);
        queue<int> oeve,beve;
        queue<char> alleve;
        for(int i=0;i<n;i++){
            char c;
            int ins;
            scanf("%c %d ",&c,&ins);
            if(c=='O') oeve.push(ins);
            else beve.push(ins);
            alleve.push(c);
        }
        scanf("\n");
        int ret,oat=1,bat=1;
        for(ret=1;;ret++){
            char now=alleve.front();
            int oto=oeve.front(),bto=beve.front();
            bool opush=false,bpush=false;
            if(now=='O'){
                if(oat==oto){
                    opush=true;
                    alleve.pop();
                    oeve.pop();
                }
            }else{
                if(bat==bto){
                    bpush=true;
                    alleve.pop();
                    beve.pop();
                }
            }
            if(alleve.empty()) break;
            if(!opush){
                if(oat<oto) oat++;
                else if(oat>oto) oat--;
            }
            if(!bpush){
                if(bat<bto) bat++;
                else if(bat>bto) bat--;
            }
        }
        printf("Case #%d: %d\n",ix,ret);
    }
}
