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
        
        int n,m;
        cin>> n >>m ;
            
        char bla[n][m];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                cin>>bla[i][j];
            }
        }
        bool error = false;
         for(int i = 0; i < n; i++){

            if(error) break;

            for(int j = 0; j < m; j++){


                if(bla[i][j] == '#'){
//                    cout<<"i = "<<i <<  "j = " << j << endl;
                    bla[i][j] = '/';
                    
                    if(j + 1 < m && bla[i][j+1] == '#'){
                        bla[i][j+1] = '\\';
                    }
                    else{ error = true; break;}

                    if(i + 1 < n && bla[i+1][j] == '#'){
                        bla[i+1][j] = '\\';
                    }
                    else{ error = true; break;}

                    
                    if( i+1 < n && j+1 < m && bla[i+1][j+1] == '#'){
                            bla[i+1][j+1] = '/';
                    }
                    else{ error = true; break;}

                }
            }
        }
        
        
		printf("Case #%d:\n",tt+1);
        if(error){ cout<<"Impossible"<<endl; continue;}
            
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                cout<<bla[i][j];
            }
            cout<<endl;
        }
	}
	return 0;

}



