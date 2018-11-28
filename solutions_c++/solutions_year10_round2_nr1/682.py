#include <fstream>
#include <vector>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");
int n,m,t,ans=0,p;
struct nam{
    vector<int> son;
    string s;
}a[100000];    
int dfs(string s,int x){
    if(s.size()==0)return 0;
    string name="",ss="";
    int i,j;
    for(i=1;s[i]!='/'&&i<s.size();i++)
    	name+=s[i];
	for(;i<s.size();i++)
		ss+=s[i];
	for(i=0;i<a[x].son.size();i++)
	    if(name==a[a[x].son[i]].s){
	    	dfs(ss,a[x].son[i]);
	    	break;
	 }   	
 	if(i==a[x].son.size()){
 		a[x].son.push_back(p);
 		a[p].s=name;
 		ans++;
 		p++;
 		dfs(ss,p-1);
	}
 	return 0;
}  		
int main(){
    int i,j,u;
    cin>>t;
    for(u=0;u<t;u++){
        for(i=0;i<=p;i++)
        	a[i].son.clear();
        p=1;
        //memset(a,0,sizeof(a));
        cin>>m>>n;
        string s;
        for(i=0;i<m;i++){
            cin>>s;
            dfs(s,0);
        }
        ans=0;
        for(i=0;i<n;i++){
            cin>>s;
            dfs(s,0);
        }
        cout<<"Case #"<<u+1<<": "<<ans<<endl;
    }
    //system("pause");
    return 0;
}            
