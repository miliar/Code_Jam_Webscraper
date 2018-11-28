#include<iostream>
#include<string>
#include<map>

using namespace std;

int main()
{
    string str1, str2;
    str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    str2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    int length = str1.length();
    map<char,char> m;
    map<char,char> :: iterator it;

    m['z'] = 'q';
    m['q'] = 'z';

    for(int i=0; i<length; i++)
    {
        m[str1[i]] = str2[i];
    }

   /* for(it = m.begin(); it!= m.end(); it++)
    {
        cout<<(*it).first<<" = "<<(*it).second<<endl;
    }
    */

    int t,l;
    string str;

    cin>>t;
    getline(cin,str);

    for(int i=1;i<=t;i++)
    {
        getline(cin,str);
        l=str.length();

        cout<<"Case #"<<i<<": ";
        for(int j=0;j<l;j++)
        {
            cout<<m[str[j]];
        }
        cout<<endl;
    }


    return 0;
}
