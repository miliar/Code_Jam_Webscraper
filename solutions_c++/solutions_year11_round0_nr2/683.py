#include <fstream>
#include <iostream>
#include <string>
#include <deque>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("output.txt");
#define cin fin
#define cout fout

string c[100],d[100];
char q[1000];int top;

int main()
{
	int n;
	cin>>n;
	for(int x=1;x<=n;x++){
		int cc,cd,ce;
		cin>>cc;
		for(int i=0;i<cc;i++) cin>>c[i];
		cin>>cd;
		for(int i=0;i<cd;i++) cin>>d[i];
		cin>>ce;
		string s;cin>>s;
		top=0;
		for(int i=0;i<s.length();i++)
		{
			if(top==0){
				q[top++]=s[i];
			}else{
				char x,y;x=q[top-1];y=s[i];
				bool suc=true;
				for(int j=0;j<cc && suc;j++){
					if((c[j][0]==x && c[j][1]==y)||(c[j][0]==y && c[j][1]==x)) q[top-1]=c[j][2],suc=false;
				}
				for(int j=0;j<cd && suc;j++){
					for(int k=0;k<top;k++)
						if((d[j][0]==q[k] && d[j][1]==y)||(d[j][0]==y && d[j][1]==q[k])) top=0,suc=false;
				}
				if(suc) q[top++]=s[i];
			}
		}
		if(top==0){
			cout<<"Case #"<<x<<": []"<<endl;
		}else{
			cout<<"Case #"<<x<<": [";
			for(int i=0;i<top-1;i++)
			{
				cout<<q[i]<<", ";
			}
			cout<<q[top-1]<<"]"<<endl;
		}
	}
}