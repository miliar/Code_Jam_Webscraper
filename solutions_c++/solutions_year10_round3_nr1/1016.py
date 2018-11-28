
#include<set>
#include<map>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<cctype>
#include<cstdio>
#include<string>
#include<vector>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<algorithm>
#define fr(i,n) for(int i=0;i<n;++i)
#define For(i,a,b) for(int i=a;i<b;++i)
#define Rev(i,a,b) for(int i=a;i>=b;--i)

using namespace std;

int t,n,cont=1;
pair<int, int> B[1009];
set <int> A;

bool cmp(pair<int,int> a, pair<int , int> b){
    return(a.second<b.second); 
}

int main(){
	freopen("1cb.in","r",stdin);freopen("wert.in","w",stdout);
	scanf("%d",&t);
	while(t--){
        scanf("%d",&n);
        A.clear();
        int temp,t1;
        fr(i,n){   
           scanf("%d%d",&temp,&t1);
           B[i].first=temp;
           B[i].second=t1;     
           A.insert(temp);
        }           
        sort(B,B+n,cmp);
        int ans=0;
        Rev(i,n-1,0){
            set<int> :: iterator it=A.begin();
            int ct=0;
            for(;it!=A.end();++it,ct++){
                if((*it)==B[i].first){
                    ans+=(int)(A.size()-ct-1);
                    A.erase(it); 
                    break;                 
                }                   
            }         
        }
        printf("Case #%d: %d\n",cont++,ans);
    }
}
