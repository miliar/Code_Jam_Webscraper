#include <iostream>
#include <map>
#include <string>
using namespace std;

string t[16];
int a[16];
int mx,ans=0;
int l,d,n;
map<string,int> dic;

int rec(int ind,string f)
{
//cout<<"ind=="<<ind<<endl;
if (ind==mx) {
	//string final;
	//for (int i=0;i<mx;++i)
	//	final+=t[i][a[i]];
//	cout<<"final =="<<f<<endl;		
	if (dic[f]==1)
		++ans;
	return 1;
}
while(a[ind]<t[ind].size())
{
   f+=t[ind][a[ind]];
    if (dic[f]==1)	
   	rec(ind+1,f);
   f.erase(f.size()-1);
   a[ind]++;	
}
a[ind]=0;
return 1;
}

int main()
{
//char str[100];
string str;
string inp;

cin>>l>>d>>n;
for(int i=0;i<d;++i)
    {
	cin>>str;
	for (int i=1;i<str.size();++i)
		{
			dic[str.substr(0,i)]=1;	
//			cout<<"str=="<<str.substr(0,i)<<endl;	
		}
	dic[string(str)]=1;    
    }
 for(int tc=1;tc<=n;++tc)
  {
 	cin>>str;
//	cout<<"str=="<<str<<endl;
 	int ind=0,ob,cb;
 	for (int i=0;str[i]!='\0';++i)
 	{
    	      if (str[i]=='(') {
		if(inp=="")
			continue;
		for(int k=0;k<inp.size();++k)
			{t[ind]=inp[k];a[ind++]=0;}
		inp="";
		continue;
		}
	      if(str[i]==')') {
			t[ind]=inp;a[ind++]=0;
			inp="";
			continue;
		}					
              inp+=str[i];	
        }
	if (inp!="") {
		for(int k=0;k<inp.size();++k)				
			{t[ind]=inp[k];a[ind++]=0;}
			inp="";
		}

   mx=ind;
   if (ind==l)
  	rec(0,"");
   cout<<"Case #"<<tc<<": "<<ans<<endl;
    ans=0;
  }
}
