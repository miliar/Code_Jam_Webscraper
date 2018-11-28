#include<fstream>
#include<string>
#include<vector>
using namespace std;
int main(){
    ifstream fin ("in.txt");
    ofstream fout ("out.txt");
    bool boo=true,too=false;
    int ans=0,k=0,ct=0,a=0,b=0,z,mm=0;
    string s,str,x,xx;
    char c;
    vector<string>v;
    int l,d,n;
    fin>>l>>d>>n;
    for(int i=0;i<d;i++){
            fin>>s;
            v.push_back(s);
    }     
    for(int i=0;i<n;i++){
            fin>>xx;
            for(int j=0;j<v.size();j++){
                    x="";
                    x=xx;
                    while(k!=l){
                          a=x.find('(');
                          if(a==-1){
                              if(x.substr(ct)!=v[j].substr(k)) boo=false;
                              break;
                          }
                          x[a]='.';
                          if(mm=0||b-a!=1){
                              str="";
                              str=x.substr(ct,a-ct);
                              if(str!=""&&v[j].substr(k,a-ct)!=str){
                                        boo=false;
                              } 
                              mm=1;
                          }     
                          if(!boo) break;
                          b=x.find(')');
                          x[b]='.';
                          z=a-ct;
                          ct=a+1;
                          k+=z;
                          str="";
                          str=x.substr(ct,b-a-1);
                          c=v[j][k];
                          k+=1;
                          for(int d=0;d<str.length();d++){
                                  if(str[d]==c) too=true;
                          }
                          if(!too) {
                                   boo=false;
                                   break;
                          }
                          too=false;
                          ct=b+1;
                    }
                    if(boo) ans++;  
                    boo=true;
                    mm=ct=k=0;
            }   
            fout<<"Case #"<<i+1<<": "<<ans<<endl;
            ans=0;
    }  
      
      return 0;
}                       
                          
                                  
                          
                                      
                              
                    
               
            
    
    
