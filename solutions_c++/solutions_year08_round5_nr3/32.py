#include <stdio.h>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
char buffer[200];
int mapjoin[2000][2000];

int main(){
    int ntc,ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        int n,m;
        scanf("%d%d", &n,&m);
        
        vector<int> goodrow;
        vector<int> goodcount;
        for (int i=0;i<1<<m;i++){
            int valid=1;
            int count=i%2;
            for (int j=1;j<m;j++){
                if ((i& (1<<j)) && (i& (1<<(j-1)))){
                    valid=0;break;
                }
                count+= (i&(1<<j))?1:0;
            }
            if (valid){ 
                goodrow.push_back(i);
                goodcount.push_back(count);
            }
        }    
        
        memset(mapjoin,0,sizeof(mapjoin));
        for (int i=0;i<goodrow.size();i++){
            for (int j=0;j<goodrow.size();j++){
                int valid=1;
                for (int k=0;k<m;k++){
                    if (goodrow[j]& (1<<k)){
                        if (k>0 && (goodrow[i]&(1<<k-1))){
                            valid=0; break;
                        }
                        if (k+1<m && (goodrow[i]&(1<<k+1))){
                            valid=0; break;
                        }
                    }
                }
                mapjoin[goodrow[i]][goodrow[j]]=valid;
            }    
        }   
         
        vector<int> rowconfig;
        for (int i=0;i<n;i++){
            scanf("%s", buffer);
            int crow = 0;
            
            for (int j=0;j<m;j++){
                crow*=2;
                if (buffer[j]=='x'){
                    crow+=1;                    
                }
            }
            rowconfig.push_back(crow);
        }
        map<int,int> curmap;
        // first line
        int res = 0;
        for (int i=0;i<goodrow.size();i++){
            if (!(goodrow[i] & rowconfig[0])){
//                printf(">%d %d\n", goodrow[i], rowconfig[0]);
                curmap[goodrow[i]]=goodcount[i];
                res>?=goodcount[i];
            }
        }  
        for (int line = 1;line<n;line++){
            map<int,int> nextmap;
            
            for (map<int,int>::iterator it = curmap.begin();it!=curmap.end();it++){
                pair<int,int> cur = *it;
                for (int i=0;i<goodrow.size();i++){
                    if (!(goodrow[i]&rowconfig[line])){
                      //  printf(">%d> %d\n", cur.first, goodrow[i]);
                        if (mapjoin[cur.first][goodrow[i]]){
                        //printf(">%d> %d\n", cur.first, goodrow[i]);
                            nextmap[goodrow[i]]>?=cur.second+goodcount[i];
                            res>?=nextmap[goodrow[i]];
                        }
                    }
                }
            }
            
            curmap = nextmap;
        }        
        printf("Case #%d: %d\n", ++ttc, res);
    }
    
    return 0;
}
