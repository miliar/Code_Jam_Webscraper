#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
using namespace std;
int main()
{

    char mapme[123]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113
};

int T;char tmp;
cin>>T;
cin>>tmp;
for(int k=1;k<=T;k++)
{

    string line;
    getline(cin,line);
    int len=line.length();
    for(int i=0;i<len;i++)
    line[i]=mapme[line[i]];
    if(k==1)
    cout<<"Case #"<<k<<": "<<mapme[tmp]<<line<<endl;
    else
    cout<<"Case #"<<k<<": "<<line<<endl;

}
    return 0;
}
