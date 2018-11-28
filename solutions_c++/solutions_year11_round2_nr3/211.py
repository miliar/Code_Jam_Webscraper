#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 8;

int n;
vector<vector<int> > lst;
vector<vector<int> > rooms;

void printroom(vector<int>& room){
    for(int i=0;i<room.size();++i){
        cout << room[i] << " ";
    }
    cout << "\n";
}

void getrooms(vector<int>& room){
    //printroom(room);
    bool haswall = false;
    int m = room.size();
    for(int i=0;i<room.size();++i) if(!haswall){
        for(int j=0;j<lst[room[i]].size();++j){
            bool isin = false;
            for(int h=0;h<room.size();++h){
                if(room[h] == lst[room[i]][j]){
                    isin = true;
                }
            }
            if(isin && lst[room[i]][j] != room[(i+1)%m] && lst[room[i]][j] != room[(i-1+m)%m]){
                haswall = true;
                int k;
                for(k=0;k<room.size();++k){
                    if(room[k] == lst[room[i]][j]){
                        break;
                    }
                }
                
                vector<int> room1;
                for(int h=i;h<=k;++h){
                    room1.push_back(room[h]);
                }
                //printroom(room1);
                
                vector<int> room2;
                for(int h=k;h<room.size();++h){
                    room2.push_back(room[h]);
                }
                for(int h=0;h<=i;++h){
                    room2.push_back(room[h]);
                }
                //printroom(room2);
                getrooms(room1);
                getrooms(room2);
                break;
            }
        }
    }
    
    if(!haswall){
        rooms.push_back(room);
    }
}

int color[MAXN];
int ret[MAXN];

bool test(int c){
    for(int i=0;i<rooms.size();++i){
        bool mrk[MAXN];
        for(int j=1;j<=c;++j){
            mrk[j] = false;
        }
        
        for(int j=0;j<rooms[i].size();++j){
            mrk[color[rooms[i][j]]] = true;
        }
        
        for(int j=1;j<=c;++j){
            if(!mrk[j]){
                return false;
            }
        }
        
    }
    
    for(int i=0;i<n;++i){
        ret[i] = color[i];
    }
    
    return true;
}

bool assign(int v,int c){
    if(v == n){
        return test(c);
    }
    bool ret = false;
    for(int i=1;i<=c;++i){
        color[v] = i;
        ret |= assign(v+1,c);
    }
    
    return ret;
}

bool ispossible(int c){
    color[0] = c;
    return assign(1,c);
}

int main(){
    int t;
    cin >> t;
    
    for(int lp=1;lp<=t;++lp){
        rooms.clear();
        int m;
        cin >> n >> m;
        
        lst.clear();
        lst.resize(n);
        
        vector<int> u(m),v(m);
        for(int i=0;i<m;++i){
            cin >> u[i];
            --u[i];
        }
        for(int i=0;i<m;++i){
            cin >> v[i];
            --v[i];
        }
        for(int i=0;i<m;++i){
            lst[u[i]].push_back(v[i]);
            lst[v[i]].push_back(u[i]);
        }
        
        vector<int> initial;
        for(int i=0;i<n;++i){
            initial.push_back(i);
        }
        
        getrooms(initial);
        
        int resp;
        for(resp=1;resp<=n;++resp){
            if(!ispossible(resp)){
                break;
            }
        }
        resp--;
        
        cout << "Case #" << lp << ": " << resp << "\n";
        for(int i=0;i<n;++i){
            cout << ret[i] << " ";
        }
        cout << "\n";
    }
    
    return 0;
}