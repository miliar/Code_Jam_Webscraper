#include <iostream>
#include <cstdio>
#include <set>
#include <utility>

using namespace std;

#define AA 0
#define BB 1
#define notBB 2

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int N,j;
    scanf("%d",&N);
    for(j=1;j<=N;j++){
        int T,NA,NB,i;
        multiset<pair<int,int> > A,B;
        scanf("%d",&T);
        scanf("%d %d",&NA,&NB);
        for(i=0;i<NA;i++){
            int temp1,temp2,temp3,temp4;
            scanf("%d:%d %d:%d",&temp1,&temp2,&temp3,&temp4);
            A.insert(pair<int,int>(temp1*60+temp2,temp3*60+temp4));
        }
        for(i=0;i<NB;i++){
            int temp1,temp2,temp3,temp4;
            scanf("%d:%d %d:%d",&temp1,&temp2,&temp3,&temp4);
            B.insert(pair<int,int>(temp1*60+temp2,temp3*60+temp4));
        }

        int tA=0,tB=0,wA=NA,wB=NB;
        multiset<pair<int,int> > sA,sB;
        for(set<pair<int,int> >::iterator ii=A.begin();ii!=A.end();ii++){
            sA.insert(pair<int,int>((*ii).second+T,AA));
        }
        for(set<pair<int,int> >::iterator ii=B.begin();ii!=B.end();ii++){
            sA.insert(pair<int,int>((*ii).first,BB));
        }
        for(set<pair<int,int> >::iterator ii=sA.begin();ii!=sA.end();ii++){
            if((*ii).second==AA)
                tA++;
            else
                if(tA>0){
                    wB--;
                    tA--;
                }
        }

        for(set<pair<int,int> >::iterator ii=A.begin();ii!=A.end();ii++){
            sB.insert(pair<int,int>((*ii).first,notBB));
        }
        for(set<pair<int,int> >::iterator ii=B.begin();ii!=B.end();ii++){
            sB.insert(pair<int,int>((*ii).second+T,BB));
        }
        for(set<pair<int,int> >::iterator ii=sB.begin();ii!=sB.end();ii++){
            if((*ii).second==BB)
                tB++;
            else
                if(tB>0){
                    wA--;
                    tB--;
                }
        }
        printf("Case #%d: %d %d\n",j,wA,wB);
    }
	return 0;
}
