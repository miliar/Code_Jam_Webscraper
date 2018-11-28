#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>

using namespace std;

char arr[60][60];
int n,m;

void paint(int x, int y)
{
    arr[x][y]='/';
    bool flag=false;
    if (y+1>0 && y+1< m) 
    	if (arr[x][y+1]=='#') 
    	{
    		arr[x][y+1]='\\'; 
    		flag= 1;
    	}
    	
    if (!flag) 
    	arr[x][y] = '#';
    
    flag = 0;
    if (x+1>0 && x+1< n) 
    	if (arr[x+1][y]=='#') 
    	{
    		arr[x+1][y]='\\'; 
    		flag = 1;
    	}
    	
    if (!flag)
    {
        arr[x][y]='#';
        arr[x+1][y]='#';
    }
    
    flag=0;
    if (x+1>0 && x+1<n && y+1>0 && y+1<m) 
    	if (arr[x+1][y+1]=='#') 
    	{ 
    		arr[x+1][y+1]='/'; 
    		flag = 1;
    	}
    	
    if (!flag)
    {
    
        arr[x][y] = '#';
        arr[x+1][y] = '#';
        arr[x+1][y+1] = '#';
    }
}

int main(){
    int t;
    cin>>t;
    for(int r=1; r<=t; r++)
    {

        cin>>n>>m;
        int c  = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++){
                cin>>arr[i][j];
                if (arr[i][j] == '#') c++;
            }
        }
        cout<<"Case #"<<r<<":\n";
        if (c % 4 != 0){
            cout<<"Impossible\n";
            continue;
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if (arr[i][j]=='#'){
                    paint(i,j);
                }
            }
        }
        bool f = true;
        bool si=true;
        for(int i = 0; i < n && si; i++){
            for(int j = 0; j < m && si; j++){
                if (arr[i][j] == '#')
                {
                    f = false;
                    si=false;
                }
            }
        }
        
        if (!f) cout<<"Impossible\n";
        else {
            for(int i = 0; i < n; i++){
                for(int j = 0; j < m; j++){
                    cout<<arr[i][j];
                }
                cout<<endl;
            }
        
        }
        
    }
    return 0;
}
