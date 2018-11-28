#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <memory.h>
#include <string>
#include <math.h>

using namespace std;

#define fori(i,j,k) for(int i=j;i<k;i++)
#define ford(i,j,k) for(int i=j-1;i>=k;i--)
#define i64 __int64
#define ld long double
#define mp make_pair

int sign(int x){
    if (x>0) return 1;
    if (x==0) return 0;
    return -1;
}

int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
    int t;
    scanf("%d\n",&t);

    fori(h,0,t){
        vector<pair<int,int> > a;
        vector<int> b[2];
        char ch;
        int d;
        int k;
        scanf("%d ",&k);
        fori(j,0,k){
            scanf("%c ",&ch);
            //  if (ch=='\n') break;
            scanf("%d ",&d);
            if(ch=='B'){
                a.push_back(mp(1,d));
                b[1].push_back(d);
                //if (j==k-1) b[1].push_back(d);
            }
            else{
                a.push_back(mp(0,d));
                b[0].push_back(d);
                //if (j==k-1) b[0].push_back(d);
            }
        }
        if(b[0].empty()) b[0].push_back(1);
        if(b[1].empty()) b[1].push_back(1);
        
        vector<pair<int,int> >::iterator iter=a.begin();
        vector<int>::iterator it[2];
        /*
        for(it[0]=b[0].begin();it[0]!=b[0].end();it[0]++)
            printf("%d ",*it[0]);    
        printf("\n");
        for(it[1]=b[1].begin();it[1]!=b[1].end();it[1]++)
            printf("%d ",*it[1]);   
            printf("\n\n");
        */     
		b[0].push_back(b[0].at(b[0].size()-1));
		b[1].push_back(b[1].at(b[1].size()-1));
        it[1]=b[1].begin();
        it[0]=b[0].begin();
        int p=0;
        int x[2];
        x[0]=1;
        x[1]=1;
//        int t=1;
        
        while(iter!=a.end()){
          //  printf(" %d %d\n",*it[0],*it[1]);
           
            while((iter!=a.end())&&(x[iter->first]==iter->second)) {
			x[0]+=sign(*it[0]-x[0]);
            x[1]+=sign(*it[1]-x[1]);
            it[iter->first]++;
			p++;
            iter++;
            }
			x[0]+=sign(*it[0]-x[0]);
            x[1]+=sign(*it[1]-x[1]);
            //printf("%d %d\n",x[0],x[1]);
            p++;
        }
        printf("Case #%d: %d\n",h+1,p-1);
    }
    return 0;
}
