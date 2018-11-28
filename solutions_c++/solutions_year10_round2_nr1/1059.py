#include<iostream>
#include<vector>

using namespace std;
vector<vector<string> > v;

vector<string > parse(string s){
   vector<string> v; string temp;
   for(int i=0;i<s.size();i++){
     if( s[i]=='/' ){
          if( temp.size() ) v.push_back(temp);
          temp="";
     }
     else temp.push_back(s[i]);
     }
     if( temp.size() ) v.push_back(temp);
     return v;
}

int cou(string &s){ //t<<s<<endl;
    vector<string > t=parse(s); int ret=10000000;
    for(int i=0;i<v.size();i++){
        if( v[i][0]==t[0] ){ //ut<<"ins s"<<i<<endl;
           int k=0;
           while( k<t.size() && k<v[i].size() && t[k]==v[i][k] ) k++;
           if( k==t.size() ) return 0;
           int c=0;
           while( k<t.size() ){
                 k++; c++;
           }
           ret=min(ret, c);
        }
        
    }
    v.push_back(t);
    if( ret!=10000000 ) return ret;
    
    return t.size();
}

int main(){   freopen("input.cpp","r",stdin); freopen("output.cpp","w",stdout);
    int _case=1;
    int t;scanf("%d",&t);
    while(t--){
      int n,m; scanf("%d %d",&n,&m);
      v.clear(); string s;
      for(int i=0;i<n;i++ ){
        cin>>s; v.push_back( parse(s) );
      }
      int ans=0;
      for(int i=0;i<m;i++){
        cin>>s; //cout<<s<<endl;
        ans+=cou(s); //cout<<ans<<endl;
      }
     
      
       
       printf("Case #%d: %d\n",_case++,ans);
       
    
    }
    
    //cout<<"\nTime take :: "<<clock()<<" ::ms"<<endl;while(true);
    return 0;
}
