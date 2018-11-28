#include <cstdio>
#include <set>
#include <string>
#include <iostream>
using namespace std;
int main(){
    // freopen("input.txt","r",stdin);
    int t;
    cin >> t;
    for(int tc=1; tc<=t; tc++){
        int ans = 0;

        int n,m;
        cin >> n >> m;
        set<string> s;
        while(n--){
            string temp;
            cin >> temp;
            s.insert(temp);
        }

        while(m--){
            string a;
            cin >> a;
            if(s.count(a))
                continue;
            bool ok =false;
            for(int i=(int)a.size()-1; i>=0; i--){
                if(a[i] == '/'){

                    string b =a.substr(0,i);
                //    cout << b << endl;
                    if(s.count(b) > 0){
                        ok = true;
                        for(int j=i; j<(int)a.size(); j++){
                            if(a[j]=='/'){
                                ans++;
                            }
                        }
                        break;
                    }

                }
            }
            if(ok==false){
                for(int i=0; i<(int)a.size(); i++)
                    if(a[i]=='/')
                        ans++;
              //  s.insert(a);
            }
        //    else
                s.insert(a);
                for(int i=1; i<(int)a.size()-1; i++)
                    if(a[i] == '/')
                        s.insert(a.substr(0,i));
        }

        printf("Case #%d: %d\n",tc,ans);
    }
    return 0;
}
