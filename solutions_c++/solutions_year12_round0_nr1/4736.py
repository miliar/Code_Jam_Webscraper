#include<iostream>
#include<cstdio>
#include<string>
#include<cstdlib>

using namespace std;

int ar[26];
void init()
{
    ar[0]='y';
    ar[1]='h';
    ar[2]='e';
    ar[3]='s';
    ar[4]='o';
    ar[5]='c';
    ar[6]='v';
    ar[7]='x';
    ar[8]='d';
    ar[9]='u';
    ar[10]='i';
    ar[11]='g';
    ar[12]='l';
    ar[13]='b';
    ar[14]='k';
    ar[15]='r';
    ar[16]='z';
    ar[17]='t';
    ar[18]='n';
    ar[19]='w';
    ar[20]='j';
    ar[21]='p';
    ar[22]='f';
    ar[23]='m';
    ar[24]='a';
    ar[25]='q';
    for(int i=0;i<26;++i) ar[i]-='a';
}    

int main()
{
    init();
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int test;
    cin>>test;
    getchar();
    string str,ans;
    for(int t=1;t<=test;++t) {
        ans= "";
        getline(cin,str);
        int len= str.length();
        for(int i=0;i<len;++i) {
            if(str[i]==' ') ans+=' ';
            else ans += (ar[str[i]-'a']+'a');
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}            
