#include<iostream>
#include<string>
#include<map>
using namespace std;
int main(){
    int cnt;
   // freopen("in.txt",'r',stdin);
    freopen("input.txt","r",stdin); 
    freopen("output.txt","w",stdout); 

    
    scanf("%d\n",&cnt);
    //fflush(stdin);
    map<char,char> ma;
    ma['a']='y';
    ma['b']='h';
    ma['c']='e';
    ma['d']='s';
    ma['e']='o';
    ma['f']='c';
    ma['g']='v';
    ma['h']='x';
    ma['i']='d';
    ma['j']='u';
    ma['k']='i';
    ma['l']='g';
    ma['m']='l';
    ma['n']='b';
    ma['o']='k';
    ma['p']='r';
    ma['q']='z';
    ma['r']='t';
    ma['s']='n';
    ma['t']='w';
    ma['u']='j';
    ma['v']='p';
    ma['w']='f';
    ma['x']='m';
    ma['y']='a';
    ma['z']='q';
    ma[' ']=' ';
    
    for(int i=0;i<cnt;i++)
    {
            string tem="";
            getline(cin,tem);
           /// cin>>tem;
            cout<<"Case #"<<i+1<<": ";
            for(int j=0;j<tem.size();j++)
            {
                 cout<<ma[tem[j]]; 

            }
            
            cout<<endl;
            
    }
    

    
}
