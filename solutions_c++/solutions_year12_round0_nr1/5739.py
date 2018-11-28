#include<iostream>
#include<algorithm>
#include<iomanip>
#include<cstring>
#include<string>
#include<cstdio>
#include<cmath>
#include<queue>
#include<map>
#include<set>
using namespace std;
int main()
{
    map<char,char> mp;
    mp['a']='y';mp['b']='h';mp['c']='e';mp['d']='s';mp['e']='o';mp['f']='c';mp['g']='v';
    mp['h']='x';mp['i']='d';mp['j']='u';mp['k']='i';mp['l']='g';mp['m']='l';mp['n']='b';
    mp['o']='k';mp['p']='r';mp['q']='z';mp['r']='t';mp['s']='n';mp['t']='w';
    mp['u']='j';mp['v']='p';mp['w']='f';mp['x']='m';mp['y']='a';mp['z']='q';
    int i,n;
    cin>>n;
    char a[2];
    cin.getline(a,1);
    for(i=1;i<=n;i++)
    {
        string str;
        getline(cin,str);
        printf("Case #%d: ",i);
        for(int j=0;j<str.size();j++)
        {
            if(str[j]!=' ')
                cout<<mp[str[j]];
            else
                cout<<str[j];
        }
        cout<<endl;
    }
	return 0;
}
