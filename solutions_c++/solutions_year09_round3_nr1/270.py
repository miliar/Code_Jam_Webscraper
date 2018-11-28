#include<iostream>
#include<string>
#include<map>
using namespace std;
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("ans.txt", "w", stdout);
    int cas, T, i, cnt;
    cin >> T;
    for(cas = 1; cas <= T; cas++)
    {
        printf("Case #%d: ",cas);
        map<char, int> m;
        string str;
        cin>>str;
        m[str[0]] = 1;
        for(i = 1; i < str.size(); i++)
            if( m.find(str[i]) == m.end() ){
                m[str[i]] = 0;
               // printf("%c %d\n",str[i], m[str[i]]);
                break;
            }
        cnt = 1;
        for( ; i < str.size(); i++)
            if( m.find(str[i]) == m.end() )
            {
                m[str[i]] = (++cnt);
                //printf("%c %d\n",str[i], m[str[i]]);
            }
        cnt = m.size();
        if(cnt<=1)cnt=2;
        //cout<<cnt<<endl;
        long long ans = 0;
        for(i = 0; i < str.size(); i++)
            ans = m[str[i]] + ans *cnt;
       
        printf("%lld\n",ans);
    }

}