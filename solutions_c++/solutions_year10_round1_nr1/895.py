#include <iostream>
using namespace std;
#define N 60

char a[N][N],b[N][N];
int k,n;
bool red,blue;
int dx[4] = {1,0,1,1};
int dy[4] = {0,1,-1,1};

void init(){
    cin>>n>>k;
    for (int i=0 ;i<n ;++i) cin>>a[i];
    red = false;
    blue = false;
}

//[r,c] -> [c,n-1-r]    
int rotate(char a[N][N],char b[N][N]){
    for (int r = 0 ; r<n ;++r)
        for (int c=0; c<n ;++c)
            b[c][n-1-r] = a[r][c];
}
    
void gravity(char a[N][N]){
    for (int c=0 ;c <n ;++c){
        for (int r=n-2; r>=0 ;--r){
            if (a[r][c] != '.'){
                char x = a[r][c];
                a[r][c] = '.';
                int k = r+1;
                while (k<n && a[k][c] == '.') ++k;
                --k;
                a[k][c] = x;
            }    
        }    
    }    
}
    
void print(char a[N][N]){
    cout<<"Matrix:"<<endl;
    for (int i=0 ;i<n ;++i){
        for (int j=0 ;j<n ;++j) cout<<a[i][j];
        cout<<endl;
    }    
}
    
bool check(int i,int j){
    return i>=0 && j>=0 && i<n && j<n;
}
    
int get(int i,int j,char x){
    int res = 0;
    for (int k=0 ;k<4; ++k){
        int t = 1;
        int ti = i + dx[k];
        int tj = j + dy[k];
        while (check(ti,tj) && b[ti][tj] == x){
            ++t;
            ti += dx[k];
            tj += dy[k];
        }    
        if (res < t) res = t;
    }    
    return res;
}
    
bool find(char x){
    for (int i=0 ;i<n ;++i)
        for (int j=0 ;j<n ;++j)    
            if (b[i][j] == x) {
                int t = get(i,j,x);
                //cout<<"!!"<<i<<" "<<j<<" "<<t<<endl;
                if (t >= k) return true;
            }    
    return false;
}
    
int main(){
    freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    int T;
    int index = 0;
    cin>>T;
    while (T--){
        init();
        rotate(a,b);
       // print(a);
       // print(b);
        gravity(b);
       // print(b);
        cout<<"Case #"<<++index<<": ";
        red = find('R');
        blue = find('B');
        if (red && blue) cout<<"Both"<<endl;
        else if (red) cout<<"Red"<<endl;
        else if (blue) cout<<"Blue"<<endl;
        else cout<<"Neither"<<endl;
    }        
    return 0;
}   
