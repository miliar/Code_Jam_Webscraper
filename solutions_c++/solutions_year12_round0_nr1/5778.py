#include<iostream>
#include<map>
#include<string>
#include<fstream>

using namespace std;

int main()
{
    fstream fin,fout;
    fin.open("Sample Input.txt");
    fout.open("Sample Output.txt");
    int t;
    fin>>t;
    map<char,char> g;
    g['a']='y';
    g['b']='h';
    g['c']='e';
    g['d']='s';
    g['e']='o';
    g['f']='c';
    g['g']='v';
    g['h']='x';
    g['i']='d';
    g['j']='u';
    g['k']='i';
    g['l']='g';
    g['m']='l';
    g['n']='b';
    g['o']='k';
    g['p']='r';
    g['q']='z';
    g['r']='t';
    g['s']='n';
    g['t']='w';
    g['u']='j';
    g['v']='p';
    g['w']='f';
    g['x']='m';
    g['y']='a';
    g['z']='q';
    g[' ']=' ';
    
    for(int i=1;i<=t;i++)
    {
    string s,ans;
    if(i==1)     
                 getline(fin,s);
    getline(fin,s);
    ans="Case #";
    int n;
    n=i;
    string a;
    while(n>0)
              {
               
               a+=n%10+48;
              n=n/10;
              }
    for(int k=a.length()-1;k>=0;k--)          
            ans+=a[k];
    ans+=": ";
    for(int j=0;j<s.length();j++)
            ans+=g[s[j]];
  //  cout<<ans<<endl;
    fout<<ans<<endl;
            
    }
fin.close();
fout.close();
//system("pause");    
return 0;
}
