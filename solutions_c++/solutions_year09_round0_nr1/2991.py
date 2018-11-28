#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstdio>
#include<map>
#include<queue>
#include<cstdlib>
#include<sstream>
using namespace std;
typedef unsigned long long LL;
int main()
{
    int len,D,cases;
    cin>>len>>D>>cases;
    vector<string> dict(D);
    for(int i=0;i<D;i++)
    cin>>dict[i];
    for(int T=1;T<=cases;T++)
    {
    	string s;
    	cin>>s;
    	vector<string> v;
    	int f=0;
    	string t;
    	for(int i=0;i<s.length();i++)
    	{
    		if(f==0 && s[i]=='(')
    		{f=1;t="";}
    		else if(f==1 && s[i]!=')')
    		t+=s[i];
    		else if(s[i]==')')
    		{
    			f=0;
    			v.push_back(t);
    			t="";
    		} 
    		else
    		 {
    		t+=s[i];
    		v.push_back(t);
    		t="";
    		}
    	}
    	int ret=0;
    	for(int i=0;i<D;i++)
    	{
    		int f=0;
    		for(int j=0;j<dict[i].length();j++)
    		{
    			if((find(v[j].begin(),v[j].end(),dict[i][j]))!=v[j].end())
    			f=1;
    			else {f=0;break;}
    		}
    		if(f==1)
    		ret++;
    	
    	}   
    	cout<<"Case #"<<T<<": "<<ret<<endl;	
    	
    }    
    
  return 0;
}

