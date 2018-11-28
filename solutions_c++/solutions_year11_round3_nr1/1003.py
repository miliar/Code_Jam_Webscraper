#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>

using namespace std;

int main(){
    freopen("a.in","rt",stdin);
    freopen("a.out","wt",stdout);
    int t,r,c;
    cin>>t;
    char grid[51][51];
    for (int i=1 ;i<=t ; i++){
        cin>>r>>c;
        int num=0;
        for (int j=0 ; j<r ; j++)
            for (int k=0 ; k<c ; k++){
                cin>>grid[j][k];
                if (grid[j][k] == '#')num++;
            }
        
        for (int j=0 ; j<r-1 ; j++){
            for (int k=0 ; k<c-1 ; k++){
                if (grid[j][k]=='#' && grid[j][k+1]=='#' && grid[j+1][k]=='#' && grid[j+1][k+1]=='#'){
                                    num-=4;
                                    grid[j][k]='/';
                                    grid[j][k+1]='\\';
                                    grid[j+1][k]='\\';
                                    grid[j+1][k+1]='/';
                }
            }
        }
        cout<<"Case #"<<i<<":\n";
        if (num == 0){
                
                for (int j=0 ; j<r ; j++){
                    for (int k=0 ; k<c ; k++)
                        cout<<grid[j][k];
                    cout<<endl;
                }
        }else{
              cout<<"Impossible\n";
        }
        
    }
    //system("pause");
    return 0;
}
