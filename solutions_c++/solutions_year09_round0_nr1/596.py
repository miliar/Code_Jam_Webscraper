#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

bool check[16][26];

void make_map(string pat,int l)
{
for(int a=0;a<16;a++)
	for(int b=0;b<26;b++)		
		check[a][b]=false;

int pos=0;
for(int i=0;i<l;i++)
	{
	//cout<<i<<" "<<pos<<endl;
	if(pat[pos]>='a' && pat[pos]<='z') { check[i][pat[pos]-'a']=true; pos++; }
	else {
		pos++;// (
		while(pat[pos]>='a' && pat[pos]<='z') { check[i][pat[pos]-'a']=true; pos++; } 	
	        pos++; // )
	     }
	}
//cout<<"Done..>"<<endl;
return;
}

string print_all(int L)
{
string tmp="";
string r;
for(int i=0;i<L;i++)
	{
	for(int j=0;j<26;j++)
		{
		if(check[i][j]) tmp+=('a'+j);
		}
	r+="("+tmp+")";
	tmp="";
	}
return r;
}

bool check_pat(string s,int l)
{
//cout<<"check_________pat"<<endl;
//int l=s.length();
for(int i=0;i<l;i++)
	if(check[i][s[i]-'a']==false) return false;
return true;
}

int count(vector<string> dict,int L)
{
//cout<<"count fn......."<<endl;
int c=0;
int z=dict.size();
for(int i=0;i<z;i++)
	{
	if(check_pat(dict[i],L)==true) { c++; 
				     //cout<<dict[i]<<" Yes"<<endl;
				     }
	//else cout<<dict[i]<<" No"<<endl;
	}
//cout<<"returning ..."<<c<<endl;
return c;
}

int main()
{
int L,D,N;
cin>>L>>D>>N;
string str;
vector<string> dict;

for(int i=0;i<D;i++)
	{
	cin>>str;
	dict.push_back(str);
	}
//cout<<"Done with dict.."<<endl;


for(int i=0;i<N;i++)
	{
	cin>>str;
	//cout<<str<<endl;
	make_map(str,L);
	//string s2=print_all(L);
	//if(s2!=str) cout<<"Problem!!!!! "<<str<<" "<<s2<<endl;
	int c=count(dict,L);
	cout<<"Case #"<<i+1<<": "<<c<<endl; 
	}

return 0;
}



