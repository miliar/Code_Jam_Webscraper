#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>

using namespace std;

int main(){
    int t;
    int n,q;
    char temp[150];
    string s;

    int cse=0;
    scanf("%d",&t);
    while(t--){
        cse++;
        vector <string> engines;
        vector <string> queries;
        scanf("%d",&n);

        map <string, int> val;

        for(int i=0;i<n;i++){
            scanf(" %[^\n]",temp);
            s=temp;
            engines.push_back(s);
            val.insert(make_pair(s,0));
        }

        scanf("%d",&q);

        for(int i=0;i<q;i++){
            scanf(" %[^\n]",temp);
            s=temp;
            queries.push_back(s);
        }

        int ans=0;

        for(int i=0;i<q;i++){
            int flag=0;
            if(val.find(queries[i])!=val.end()){
                val[queries[i]]++;
            }
            map <string, int> :: iterator iter = val.begin();
            for(;iter!=val.end();iter++){
                if(iter->second==0)flag=1;
            }

            if(flag==1)continue;
            else{
                ans++;
                map <string, int> :: iterator it = val.begin();
                for(;it!=val.end(); it++)
                    it->second = 0;
                val[queries[i]]=1;
            }
        }

        printf("Case #%d: %d\n",cse, ans);

        queries.clear();
        val.clear();
        engines.clear();
    }
    return 0;
}
