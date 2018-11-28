#include<iostream>
#include<fstream>
#include<sstream>
#include<map>
using namespace std;

int main()
{
    ifstream input("A-small-attempt0.in");
    ofstream output("1.txt");
    
    map<char,char> m;
    m['a']='y';    
    m['b']='h';    
    m['c']='e';    
    m['d']='s';    
    m['e']='o';   
    m['f']='c';     
    m['g']='v';     
    m['h']='x';     
    m['i']='d';     
    m['j']='u';     
    m['k']='i';     
    m['l']='g';     
    m['m']='l';     
    m['n']='b';     
    m['o']='k';     
    m['p']='r';     
    m['q']='z'; 
    m['r']='t';     
    m['s']='n';     
    m['t']='w';     
    m['u']='j';     
    m['v']='p';     
    m['w']='f';     
    m['x']='m';     
    m['y']='a';     
    m['z']='q'; 
    m[' ']=' ';
    
    int N;
    input>>N;
    input.get();
//    cout<<N;
    int temp_id;
    for(temp_id=1;temp_id<=N;++temp_id)
    {
       string s;
       getline(input, s);
       istringstream iss;
       iss.str(s);
       
       output<<"Case #"<<temp_id<<": ";
       while(iss)
       {
           char ch = iss.get();
           if(ch!=-1) output<<m[ch];
           
       }
       output<<endl;
    }
    cin>>N;
}
