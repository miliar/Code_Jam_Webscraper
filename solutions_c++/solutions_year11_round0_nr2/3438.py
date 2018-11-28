#include <iostream>
#include <vector>
#include <string>
using namespace std;

void solve(int casen){
    int a,b,c,tmpi,ttmp;
    string tmp;
    vector<int> v;
    int conv[30][30], hate[30][30];
    for (int k=0;k<30;++k)
        for (int i=0;i<30;++i){
            conv[k][i]=-1;
            hate[k][i]=0;
    }
    cin >> a;
    for (int k=0;k<a;++k){
        cin >> tmp;
        conv[ tmp[0]-65][ tmp[1]-65]=tmp[2]-65;
        conv[ tmp[1]-65][ tmp[0]-65]=tmp[2]-65;
            
    }
    cin >> b;
    for (int k=0;k<b;++k){
        cin >> tmp;
        hate [ tmp[0]-65][tmp[1]-65]=1;
        hate [ tmp[1]-65][tmp[0]-65]=1;
        
        
    }
    cin >> c;
    cin >> tmp;
    for (int k=0;k<c;++k){
        int done=0;
        tmpi=tmp[k]-65;
        if (v.size()==0) v.push_back(tmpi);
        
        else {
            ttmp=v.back();
            if (conv[ttmp][tmpi]!=-1){
                v.pop_back();
                v.push_back( conv[ ttmp][tmpi]);
                done=1;
            }
            for (int i=0;i<v.size() && done!=1;++i)
                if (hate [ v[i] ][ tmpi] ) {
                    done =1;
                    v.clear();
                    break;
                }
            if (done==0)
                v.push_back(tmpi);    
                
                
        }  
            
    }
         
    if (v.size()==0) printf("Case #%d: []\n", casen);
    else{
        printf("Case #%d: [", casen);
        for (int k=0;k<v.size()-1;++k){
            printf("%c, ", v[k]+65);
        }
        printf("%c]\n", v.back()+65);
        return;
    }
}


int main(void){
    int n;
    scanf("%d",&n);
    
    for (int k=0;k<n;++k)
        solve(k+1);
    
    //system("pause");
    return 0;
        
}
