#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<cstdio>
using namespace std;

void convert(const string &s1,string &s2)
{
 	 s2=s1;
 	 map<char,char> s;
 	 s['a']='y';
     s['b']='h';
	 s['c']='e';
	 s['d']='s';
	 s['e']='o';
	 s['f']='c';
     s['g']='v';
	 s['h']='x';
	 s['i']='d';
	 s['j']='u';
	 s['k']='i';
     s['l']='g';
	 s['m']='l';
	 s['n']='b';
	 s['o']='k';
	 s['p']='r';
     s['q']='z';
	 s['r']='t';
	 s['s']='n';
	 s['t']='w';
	 s['u']='j';
     s['v']='p';
	 s['w']='f';
	 s['x']='m';
	 s['y']='a';
	 s['z']='q';
	 s[' ']=' ';
	 int i;
	 for(i=0;i<s1.size();i++)
	   s2[i]=s[s1[i]];
}
	   
   
int main()
{
 // freopen("A-small-attempt.in","r",stdin);
 //	freopen("o.out","w",stdout);
 	int n,i;
 	cin>>n;
  	getchar();
 	vector<string> s1(n),s2(n);
 	for(i=0;i<n;i++){
 	  getline(cin,s1[i]);
      convert(s1[i],s2[i]);
	  }
    for(i=0;i<n;i++)
      cout<<"Case #"<<i+1<<": "<<s2[i]<<endl;
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 //	system("pause");
 	return 0;
}
