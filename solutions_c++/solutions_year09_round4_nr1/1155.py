#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<string,int> ps;
int N;
string grid[100];
vector<ps> vs;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int T;
    cin>>T;
    for(int t=1;t<=T;t++) {

        cin>>N;
        for(int i=0;i<N;i++) {
            cin>>grid[i];
        }
        int ret=0;
        for(int i=0;i<N;i++) {
            int next=-1;
            for(int j=i+1;j<N;j++) {
                if(grid[i][j]=='1') next=j;
            }
            if(next==-1) continue;
            int cur=i;

            //find between this and
            for(int j=cur+1;j<N;j++) {
                int valid=1;
                for(int k=cur+1;k<N;k++) if(grid[j][k]=='1') valid=0;
                if(valid) {
                    //cout<<j<<endl;
                    for(int k=j;k>cur;k--) {
                        swap(grid[k],grid[k-1]);
                        ret++;
                    }
                    break;
                }
            }


        }




        cout<<"Case #"<<t<<": ";
        cout<<ret<<endl;
    }
    return 0;
}

