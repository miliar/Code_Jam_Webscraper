#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<set>
using namespace std;
main(){
    map <char,char> mp;
    string s1,s2;
    s1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    s2="our language is impossible to understand";
    for(int i=0;i<s1.length();++i)
        mp[s1[i]]=s2[i];
    s1="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    s2="there are twenty six factorial possibilities";
    for(int i=0;i<s1.length();++i)
        mp[s1[i]]=s2[i];
    s1="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    s2="so it is okay if you want to just give up";
    for(int i=0;i<s1.length();++i)
        mp[s1[i]]=s2[i];
    mp['q']='z';
    mp['z']='q';
    
    int t,Kase=1;
    scanf("%d\n",&t);
    while(t--){
        cout<<"Case #"<<Kase++<<": ";
        getline(cin,s1);
        for(int i=0;i<s1.length();i++)
            cout<<mp[s1[i]];
        cout<<"\n";
    }
    //system("pause");
    return 0;
}

