#include<stdio.h>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;

struct trip {
    int sm,sh,em,eh,t;
}tmp;

inline bool op(trip a, trip b) {
    if(a.sh == b.sh) return a.sm < b.sm;
    return a.sh < b.sh;
}
        
int ra, rb, ile, tr, pa, pb, sm, sh, em, eh;
vector<trip> tab, wa, wb;    

int main() {
    scanf("%d",&ile);
    for(int z=0;z<ile;z++) {
        scanf("%d",&tr);
        scanf("%d %d",&pa,&pb);
        tab.clear();
        wa.clear(); wb.clear();
        ra = rb = 0;
        for(int i=0;i<pa;i++) {
            scanf("%d:%d",&sh,&sm);
            scanf("%d:%d",&eh,&em);
            tmp.sh = sh, tmp.sm = sm, tmp.eh = eh, tmp.em = em, tmp.t = 0;
            tab.push_back(tmp);
        }
        for(int i=0;i<pb;i++) {
            scanf("%d:%d",&sh,&sm);
            scanf("%d:%d",&eh,&em);
            tmp.sh = sh, tmp.sm = sm, tmp.eh = eh, tmp.em = em, tmp.t = 1;
            tab.push_back(tmp);
        }
        sort(tab.begin(),tab.end(),op);
        for(int i=0;i<tab.size();i++) {
            if(tab[i].t == 0) {
                tmp.sm = (tab[i].em+tr)%60;
                tmp.sh = tab[i].eh+(tab[i].em+tr)/60;
                wb.push_back(tmp);
                sort(wb.begin(),wb.end(),op);
                if(wa.size() == 0) ra++;
                else {
                    bool ok = 0;
                    for(int j=wa.size()-1;j>=0;j--) {
                        if(wa[j].sh < tab[i].sh ||(wa[j].sh == tab[i].sh && wa[j].sm <= tab[i].sm)) {
                            wa.erase(wa.begin()+j);
                            ok = 1;
                            break;
                        }
                    }
                    if(!ok) ra++;
                }
            }
            else if(tab[i].t == 1) {
                tmp.sm = (tab[i].em+tr)%60;
                tmp.sh = tab[i].eh+(tab[i].em+tr)/60;
                wa.push_back(tmp);
                sort(wa.begin(),wa.end(),op);
                if(wb.size() == 0) rb++;
                else {
                    bool ok = 0;
                    for(int j=wb.size()-1;j>=0;j--) {
                        if(wb[j].sh < tab[i].sh ||(wb[j].sh == tab[i].sh && wb[j].sm <= tab[i].sm)) {
                            wb.erase(wb.begin()+j);
                            ok = 1;
                            break;
                        }
                    }
                    if(!ok) rb++;
                }
            }
        }
        printf("Case #%d: %d %d\n",z+1,ra,rb);                          
    }
    return 0;
}
