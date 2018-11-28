
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

int main(){

	int t;
    cin>> t;

	for(int i = 0 ; i < t ; i++){
		int n, pd, pg;

        cin >> n >> pd >> pg;
        int k = 0;
        bool possivel = false;

		for(int d = 1; d <= 100 && d <= n; d++){
            if( (d * pd) % 100 == 0){
                k = d;
                possivel = true;
                break;
            }
        }
        
        if(!possivel){
		    cout<<"Case #"<<i+1<< ": Broken"<<endl;
            continue;
        }

        for( int g = k; g <= k * 100; g++){
            
            if( (g * pg) % 100 == 0){ //solucao
            
                if( k - (pd * k)/100  > g - (pg*g)/100){
                    possivel = false;
                    continue;
                }
                if( pd*k/100 > pg*g /100){
                    possivel = false;
                    continue;
                }
                possivel = true;
                break;
            }
            possivel = false;

        }
        
		cout<<"Case #"<<i+1<< ":";
        cout<<( possivel ? " Possible" : " Broken") << endl;
	}

	return 0;

}



