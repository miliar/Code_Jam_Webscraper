#include<set>
#include<cmath>
#include<vector>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    char mi[100]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>t;
    getchar();
    for (int cnt=1;cnt<=t;cnt++)
    {
        string gl,el;
        getline(cin,gl);
        cout<<"Case #"<<cnt<<": ";
        for (int i=0;i<gl.length();i++)
            if (gl[i]!=' ') cout<<mi[gl[i]-'a'];
            else cout<<" ";
        cout<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
//int main()
//{
//    freopen("A.in","w",stdout);
//    char my[100];
//    int t;
//    cin>>t;
//    getchar();
//    while(t--)
//    {
//        string gl,el;
//        getline(cin,gl);
//        getline(cin,el);
//        for (int i=0;i<gl.length();i++)
//        {
//            my[gl[i]-'a']=el[i];
//        }
//    }
//    for (int i=0;i<26;i++)
//    {
//        cout<<char(39)<<my[i]<<char(39)<<',';
//    }
//    fclose(stdout);
//}

/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities
de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
*/
