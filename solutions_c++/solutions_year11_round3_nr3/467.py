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
    
    freopen("C21.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t ;
    scanf("%d",&t);
    for(int i = 0; i < t; i++){
        int n,l,h;
        scanf("%d%d%d",&n,&l,&h);
        vector<int> v;
        for(int j = 0; j < n;j++){
            int num;
            scanf("%d",&num);
            v.push_back(num);
        }
        int ans =-1;
        for(int j = l; j <= h;j++){
            int cnt = 0;
            for(int k = 0; k < v.size();k++){
                if((j%v[k] == 0) || (v[k]%j ==  0)){
                    cnt++;
                 // continue;
                }
                else{
                    break;
                } 
            }
            
            if(cnt ==  v.size()){
                ans = j;
                break;
            }
        }
        
        if(ans  == -1){
          cout<<"Case #"<<i+1<<": NO"<<endl;
        }
        else
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
        
    }
//    system("pause");
    return 0;
}
