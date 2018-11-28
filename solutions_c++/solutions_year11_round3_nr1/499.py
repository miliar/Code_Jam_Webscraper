#include<iostream>
#include<vector>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<map>

using namespace std;

int main()
{
    
    freopen("A22.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t ;
    scanf("%d",&t);
    for(int i = 0; i < t; i++){
        int r,c;
        scanf("%d%d",&r,&c);
        vector<string> v;
        for(int j  =0; j < r; j++){
          string s;
          cin>>s;
          v.push_back(s);
          
        }
        
        for(int j = 0; j < v.size();j++){
            for(int k = 0; k < v[j].size();k++){
                if(v[j][k] == '#'){
                    if((j+1 < r) && (k+1 < c)){
                        if((v[j][k+1] == '#') &&(v[j+1][k+1] == '#') &&(v[j+1][k] == '#')){
                            v[j][k] = '/';
                            v[j+1][k+1] = '/';
                            v[j][k+1] = '\\';
                            v[j+1][k] = '\\';
                        }
                    } 
                }
            }
        }
        
        cout<<"Case #"<<i+1<<":"<<endl;
        int ans = 0;
        for(int j = 0; j < v.size();j++){
            for(int k = 0; k < v[j].size();k++){
                if(v[j][k] ==  '#'){
                    ans = 1;
                    break;
                }
            }
        }
        
        if (ans == 1){
            cout<<"Impossible"<<endl;
        }
        else{
            for(int j = 0; j < v.size();j++){
                cout<<v[j]<<endl;
            }
        }
        
     }
//     system("pause");
    return 0;
}
