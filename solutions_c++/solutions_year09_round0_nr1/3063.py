#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<fstream>

using namespace std;

   
int main(){
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int l,d,n;
    fin>>l>>d>>n;
    vector<string> v(d);
    for(int i=0;i<v.size();i++)fin>>v[i];
    string a;
    for(int xx=0;xx<n;xx++){
            fin>>a;
            vector<vector<char> > v1(l,vector<char> (0));
            int o=0;
            for(int i=0;i<a.size();i++){
                    if(a[i]=='('){
                                  i++;
                                  while(a[i]!=')'){
                                                   v1[o].push_back(a[i]);
                                                   i++;
                                                   }
                                  }
                    else v1[o].push_back(a[i]);
                    o++;
            }
            int count=0;
            for(int y=0;y<d;y++){
                    bool b=1;
                    for(int x=0;x<l;x++){
                            if(find(v1[x].begin(),v1[x].end(),v[y][x])>=v1[x].end()){b=0;break;}
                            }
                    if(b==1)count++;
            }
            fout<<"Case #"<<xx+1<<": "<<count<<endl;
            }
            fin.close();
            fout.close();
            }
           
            
                                                   
                                                   
                    
