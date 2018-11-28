#include <iostream>
#include <utility>



using namespace std;

typedef pair<int,int> PII;

PII parents[100][100];
char basins[100][100];

int dirx[]={0,-1,1,0};
int diry[]={-1,0,0,1};

PII getParent(PII a){ return (parents[a.first][a.second] == a?a:parents[a.first][a.second]=getParent(parents[a.first][a.second]));}


int main(){
    int T;
    cin >> T;
    int map[100][100];
    
    for(int x=1;x<=T;x++){
        int h,w;
        cin >> h >> w;
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                parents[i][j] = PII(i,j);
                basins[i][j] = 0;
                cin >> map[i][j];
            }
        }
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                int mindir=-1;
                int minflow = map[i][j];
                for(int k=0;k<4;k++){
                    if(i+diry[k]<0 || i+diry[k]==h || j+dirx[k]<0 || j+dirx[k]==w) continue;
                    if(map[i+diry[k]][j+dirx[k]]<minflow){
                        minflow = map[i+diry[k]][j+dirx[k]];
                        mindir = k;
                    }
                }
                if(mindir>-1){
                    PII me = getParent(PII(i,j));
                    parents[me.first][me.second] = getParent(PII(i+diry[mindir],j+dirx[mindir]));
                }
            }
        }
        
        char curr='a';
        
        cout << "Case #" << x << ":" << endl;
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                PII temp = getParent(PII(i,j));
                if(basins[temp.first][temp.second] == 0){
                    basins[temp.first][temp.second] = curr;
                    curr++;
                }
                cout << (j>0?" ":"") << basins[temp.first][temp.second];
            }
            cout << endl;
        }
    }
}
