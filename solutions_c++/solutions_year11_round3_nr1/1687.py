#include <cstdio>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>

#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )

using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair <int,int> pii;
typedef map <string,int> msi;

int main(){
	int i,j,k,t,tt;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++){
		int r,c;
		char red[4]={'/','\\','\\','/'};
		bool flag=true;
        cin>>r>>c;
        char tiles[r][c];
        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
                cin>>tiles[i][j];
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(tiles[i][j]=='#'){
                    int cnt=0;
                    for(int x=0;x<2;x++){
                        for(int y=0;y<2;y++){
                            if(i+x<r&&j+y<c&&tiles[i+x][j+y]=='#'){
                             //   cout<<"cnt:"<<cnt<<":"<<red[cnt]<<endl;
                                tiles[i+x][j+y]=red[cnt];

                            }else{
                                flag=false;
                            }
                            cnt++;
                        }
                    }
                    if(cnt!=4) flag=false;
                }
            }
        }
        printf("Case #%d:\n",t);
        if(!flag){
            cout<<"Impossible"<<endl;
        }else{
            for(i=0;i<r;i++){
                for(j=0;j<c;j++)
                    cout<<tiles[i][j];
                cout<<endl;
            }
        }

	}
	return 0;
}
