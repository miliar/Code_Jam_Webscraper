#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <map>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
//const int MAX=100,INF=1<<30;
//
//bool alp[26];
//char mapTable[26];
//
//int main()
//{
//#ifndef ONLINE_JUDGE
//    freopen("i.txt", "r", stdin);
//    freopen("o.txt", "w", stdout);
//
//#endif
//    int n;
//    cin>>n;
//    string s1,s2;
//
//    for(int i=0;i<26;i++) mapTable[i]=i+'a';
//
//    cin.ignore();
//    while(n--){
//
//        getline(cin,s1);
//        getline(cin,s2);
//
////        cout<<s1<<endl<<s2<<endl;
//
//        for(int i=0;i<(int)s1.size();i++){
//
//            if(s1[i]==' ')
//                continue ;
//
//            if(!(alp[s1[i]-'a'])){
//                alp[s1[i]-'a']=1;
//                mapTable[s1[i]-'a']=s2[i];
//            }
//        }
//    }
//
//    cout<<"char mapTable[26] ={ "<<endl;
//    for(int i=0;i<26;i++){
////        if(!alp[i])
////            cout<<"Fuck"<<endl;
//        if(i)
//            cout<<',';
//        cout<<"'";
//        cout<<mapTable[i];
//        cout<<"'";
//    }
//    cout<<endl<<"};"<<endl;
//
//    return 0;
//}


char mapTable[26] ={
'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'
};

int main(){
    //freopen("A-small-attempt1.in","r",stdin);
    //freopen("o.txt","w",stdout);

    int n;
    cin>>n;
    int num=1;
    cin.ignore() ;
    while(n--){
        cout<<"Case #"<<num++<<": ";
        string s;
        getline(cin,s);
        for(int i=0;i<(int)s.size() ;i++){
            if(s[i]==' '){
                cout<<' ';
                continue ;
            }
            cout<<mapTable[s[i]-'a'];
        }
        cout<<endl;
    }
}
