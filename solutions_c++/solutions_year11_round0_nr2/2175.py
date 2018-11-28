#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
using namespace std;
#define clr(x,y) memset(x,y,sizeof(x));
int mer[26][26];
int opp[26][26];
int main() {
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T; cin>>T;
    for (int t=1;t<=T;t++){
        printf("Case #%d: ",t);
        int C,D,N;
		cin>>C;
        clr(mer,-1); clr(opp,-1);
        while (C--){
            string str;
            cin>>str;
            int x=str[0]-'A' , y=str[1]-'A' ,z=str[2];
            mer[x][y]=mer[y][x]=z;
        }
		cin>>D;
        while (D--){
            string str;
            cin>>str;
            int x=str[0]-'A' , y=str[1]-'A' ,z=str[2];
            opp[x][y]=opp[y][x]=z;
        }
		cin>>N;
        string str;
        vector<char> res;
        cin>>str;
        for (int i=0;i<str.size();i++){
            int x=str[i]-'A';
            if(res.size()==0){
                res.push_back(char(x+'A'));
                continue;
            }
            int y=res[res.size()-1]-'A';
            if (mer[x][y]!=-1){
                res.pop_back();
                res.push_back(char(mer[x][y]));
            }else{
			    int flag=0;
                for (int j=0;j<res.size();j++){
                    int k=res[j]-'A';
                    if (opp[x][k]!=-1){
                        res.clear();
						flag=1;
                        break;
                    }
                }
				if (!flag)
					res.push_back(str[i]);
            }
        }
		if (res.empty()){
			printf("[]\n");
			continue;
		}
        printf("[");
        for (int i=0;i<res.size()-1;i++){
            printf("%c, ",res[i]);
        }
        printf("%c]\n",res[res.size()-1]);
    }
    return 0;
}

