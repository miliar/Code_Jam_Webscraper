#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
int main(){
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	 int a[26],i,l,t;
     for(i=0;i<26;i++)a[i]=65;
        string s,o;
        s="ejp mysljylc kd kxveddknmc re jsicpdrysi";
        o="our language is impossible to understand";
        l=s.size();
        for(i=0;i<l;i++)if(s[i]!=' ')a[s[i]-'a']=o[i];
        s="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
        o="there are twenty six factorial possibilities";
        l=s.size();
        for(i=0;i<l;i++)if(s[i]!=' ')a[s[i]-'a']=o[i];
        s="de kr kd eoya kw aej tysr re ujdr lkgc jv";
        o="so it is okay if you want to just give up";
        l=s.size();
        for(i=0;i<l;i++)if(s[i]!=' ')a[s[i]-'a']=o[i];
        a['q'-'a']='z';a['z'-'a']='q';s="";
        cin>>t;//fflush(stdin);
        int c=1;getline(cin,s);
        while(t--){ getline(cin,s);
        //cout<<s<<"this is s\n";
        l=s.size();cout<<"Case #"<<c<<": ";c++;
        for(i=0;i<l;i++)if(s[i]==' ')cout<<" ";else cout<<(char)a[s[i]-'a'];cout<<endl; }
        return 0;
}
