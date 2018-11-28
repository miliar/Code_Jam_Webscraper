#include<iostream>
#include<map>
#include<string>
using namespace std;

char ar[26][2]={{'a','y'},
{'b','h'},
{'c','e'},
{'d','s'},
{'e','o'},
{'f','c'},
{'g','v'},
{'h','x'},
{'i','d'},
{'j','u'},
{'k','i'},
{'l','g'},
{'m','l'},
{'n','b'},
{'o','k'},
{'p','r'},
{'q','z'},
{'r','t'},
{'s','n'},
{'t','w'},
{'u','j'},
{'v','p'},
{'w','f'},
{'x','m'},
{'y','a'},
{'z','q'},
};


int main()
{
    int t,tt=1,i;
    string s;
     cin>>t;
     getchar();
    while(t--)
    {
    
    getline(cin,s);
    printf("Case #%d: ",tt++);
    for(i=0;i<s.length();i++)
    if(s[i]==' ')cout<<' ';
    else cout<<ar[s[i]-'a'][1];
    cout<<endl;
    
    }

return 0;
}
    
    
    
