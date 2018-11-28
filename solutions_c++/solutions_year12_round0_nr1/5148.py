#include<iostream>

using namespace std;

int main()
{
    char googlerese[26];
    string o1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string o2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string o3 =  "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string g1 = "our language is impossible to understand";
    string g2 ="there are twenty six factorial possibilities";
    string g3 = "so it is okay if you want to just give up";


    for(int i = 0; i < o1.size(); i++){
        googlerese[o1[i]- 'a'] = g1[i];
    }
    for(int i = 0; i < o2.size(); i++){
        googlerese[o2[i]- 'a'] = g2[i];
    }
    for(int i = 0; i < o3.size(); i++){
        googlerese[o3[i]- 'a'] = g3[i];
    }
    googlerese['q'-'a']= 'z';
    googlerese['z'-'a']= 'q';

    int cases;
    cin>>cases;
    cin.ignore();
    for(int i = 1; i <= cases; i++){
        string s;
        getline(cin, s);
        cout<<"Case #"<<i<<": ";
        for(int j = 0; j < s.size(); j++){
            int ch = s[j]-'a';
            if(ch<26 ){
                cout<<googlerese[ch];
            }
            else{
                cout<<ch;
            }
        }
        cout<<endl;
    }
    return 0;
}
