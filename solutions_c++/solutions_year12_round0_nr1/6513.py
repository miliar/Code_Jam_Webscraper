#include<iostream>
using namespace std;

char buf[1024*1024];

int main()
{
    
    freopen("hello.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
    string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string q = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    
    char map[27] = {' '};
    for(int i=0; i<s.length(); i++)
    {
            if(s[i] != ' ')
                 map[(int)s[i] - 96] = q[i];
    }
    map[26]='q';
    map[17]='z';
    
    gets(buf);
    int x = atoi(buf);
    
    string p;
    string result = "";
    int z=1;
    while( x )
    {
           x--;
           getline (cin,p);
           //cout<<p<<endl;
           for(int i=0;i<p.length();i++)
           {
                   if( p[i] != ' ')
                   {
                       result = result + map[(int)p[i] - 96];
                   }else
                   {
                        result = result + " ";
                   }
           }
           //cout<<result;
           cout<<"Case #"<<z<<": "<<result;
           z++;
           result = "";
           if(x !=0 ) cout<<endl;
    }
       
}
