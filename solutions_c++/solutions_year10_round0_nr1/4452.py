#include<iostream>
#include<vector>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

int main()
{
    
    freopen("input1.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int k2;
    cin>>k2;
    for(int ch = 1; ch <= k2; ch++ ){
    int n;
    int  k;
    
    cin>>n;
    cin>>k;
    vector<int> v(n,0);
    for(int i = 0; i < k ; i++){
            vector<int> temp(n,0);
            for(int j = 0; j < n; j++){
            
                    if (j == 0) {
                        if(v[j] == 0){
                                temp[j] = 1;
                        }
                    
                    }
                    
                    else if(j >0){
                         int check = 1;
                         for(int l =0;l <j ; l++){
                                 if(v[l] != 1){
                                         check =0;
                                         break;
                                 }
                         }
                         if(check == 1){
                                  if(v[j] == 1)
                                  temp[j] = 0;
                                  
                                   if(v[j] == 0)
                                   temp[j] = 1;
                         }
                         else{
                              temp[j] = v[j];     
                         }
                         
                    }
                    
            }
            
            v = temp;
            
    }
    int check =1;
    for(int i = 0; i < v.size(); i++){
            if(v[i] != 1){
                    check = 0;
                    break;
            }
    }
    if(check == 1){
             cout<<"Case #"<<ch<<": "<<"ON"<<endl;
    }
    else if(check == 0){
          cout<<"Case #"<<ch<<": "<<"OFF"<<endl;
    }
    }
}
