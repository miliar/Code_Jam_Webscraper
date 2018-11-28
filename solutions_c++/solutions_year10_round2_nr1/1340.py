#include<iostream>
#include<map>
#include<vector>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>

using namespace std;

int main()
{
    
      freopen("abc1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int k2;
    cin>>k2;
    for(int l =0 ; l < k2; l++){
    
    int n,m;
    cin>>n>>m;
    
    map<string,int> m1,m2;
    map<string,int>:: iterator p;
    vector<string> v,v1;
    vector<string>:: iterator it;
    for(int i = 0; i < n ; i++){
            string s;
            cin>>s;
            string s1;
            for(int j = 0; j < s.size(); j++){
            
                   
                    if(s[j] == '/') {
                            v.push_back(s1);
                            m1[s1] = i;
                               
                    }
                     s1.push_back(s[j]);
                         
            }
                    v.push_back(s); 
                    m1[s] = i;
    }
    
     for(int i = 0; i < m ; i++){
            string s;
            cin>>s;
            string s1;
            for(int j = 0; j < s.size(); j++){
            
                   
                    if(s[j] == '/') {
                            v1.push_back(s1);
                            m2[s1] = i;
                               
                    }
                     s1.push_back(s[j]);
                         
            }
                    v1.push_back(s); 
                    m2[s] = i;
    }
    p = m2.begin();
    m2.erase(p);
    int count  =0;
    
    
    for(p = m2.begin(); p!= m2.end();p++){
              string s;
              s = p->first;
              if(s[s.size() -1] != '/'){
                            int chk = 0;
                            for(int j = 0; j< v.size(); j++ ){
                                    if(v[j] ==  s){
                                            chk = 1;
                                            break;
                                    }
                            }
                            if(chk == 0){
                                   count = count + 1;
                            }
              }
    }
    
    cout<<"Case #"<<l+1<<": "<<count<<endl;
  }
    
 //   system("pause"); 
}
