
#include<iostream>
#include<set>
#include<map>
#include<deque>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

class pontos{
    public:
    int a,b;
};

int main(){

	int n;
	int t = 1;
    cin>>t;

    for(int tt = 0 ; tt < t; tt++){
        
        int n,l,h;
        cin>> n>> l >> h;
        vector<int> nots(n);
        int resp = -100;

        for(int i = 0; i < n; i++){
            cin>> nots[i];
        }

        for(int i = l ; i <= h; i++){
            bool erro = false;
            
            for(int j = 0; j < n; j++){
                if( nots[j] % i == 0 || i % nots[j] == 0){
                    continue;
                }
                else{
                    erro = true;
                    break;
                }
            }
            if(!erro){
                resp = i;
                break;
            }    
        }

		printf("Case #%d:",tt+1);
        if(resp == -100) 
            cout<<" NO"<<endl;
        else
            cout<<" "<<resp<<endl;
	}

	return 0;

}



