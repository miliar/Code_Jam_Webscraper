#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T;
    scanf("%d",&T);
    for(int ii=1; ii<=T;ii++) {
        int C,D,l;
        char comb[4],repel[3],str[11];
        vector<char> list_str;
        scanf( "%d", &C );
        if(C) scanf("%s",comb);
        scanf( "%d", &D );
        if(D) scanf("%s",repel);
        scanf("%d", &l);
        scanf("%s",str);

        int sz=0;
        for(int i=0; i<l; i++) {
            list_str.push_back(str[i]); sz++;
            while(C && sz>=2 &&
               ((list_str[sz-1]==comb[0]&&list_str[sz-2]==comb[1])||
                (list_str[sz-1]==comb[1]&&list_str[sz-2]==comb[0])) ) {
                list_str.pop_back();
                list_str.pop_back();
                //list_str.erase(list_str.end()-2,list_str.end());
                list_str.push_back(comb[2]);
                sz--;
            }
            if(D && (list_str[sz-1]==repel[0]||list_str[sz-1]==repel[1]) ) {
                vector<char>::iterator beg;
                if(str[i]==repel[0])
                beg=find(list_str.begin(),list_str.end(),repel[1]);
                else
                beg=find(list_str.begin(),list_str.end(),repel[0]);
                if(beg!=list_str.end()) {
                    list_str.clear();
                    sz=0;
                }
            }
        }


        printf( "Case #%d: [", ii );
        sz = list_str.size();
        for(int c=0;c<sz;c++) {
            printf("%c",list_str[c]);
            if(c+1<sz)printf(", ");
        }
        printf("]\n");
    }
    return 0;
}
