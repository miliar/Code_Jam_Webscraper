#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <vector>
#include <map>

#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>


using namespace std;
typedef vector<string> VS;
typedef vector<VS> VSS;
VSS dirPaths;
int N,M;

VS tokPath(string str)
{
    VS v;v.clear();
    for(int i = 0; i < str.size(); )
    {
        if(str[i]=='/') {
            i++;
            continue;
        }
        string s = "";
        while(i<str.size()&&str[i]!='/') {
            s+=str[i];
            i++;
        }
        v.push_back(s);
    }
    return v;
}

int main()
{
    //freopen("test.in","r",stdin);
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("A-small-attempt1.out","w",stdout);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++) {
        int ret = 0;
        dirPaths.clear();
        cin>>N>>M;
        for(int i = 0; i < N; i++) {
            string str;cin>>str;
            dirPaths.push_back(tokPath(str));
        }

        for(int i =0 ; i < M; i++) {
            string str;cin>>str;
            VS vPath = tokPath(str);
            int size=dirPaths.size();
            int max_match= 0;
            for(int j = 0; j < size; j++) {
                int p = min((int)vPath.size(),(int)dirPaths[j].size());
                int k;
                for(k = 0; k < p; k++) {
                    if(dirPaths[j][k]!=vPath[k]) {
                        break;
                    }
                }
                max_match=max(max_match,k);
            }
            ret+=vPath.size()-max_match;
            dirPaths.push_back(vPath);
        }
        cout<<"Case #"<<tc<<": "<<ret<<endl;
    }


}


