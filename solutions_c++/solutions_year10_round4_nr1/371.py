#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int n;
string s[1000];

bool ok(int x,int y)
{
    for(int i=0;i<2*n-1;i++)
        for(int j=0;j<2*n-1;j++)if(s[i][j]!=' '){
                if(x*2-i>=0 && x*2-i<2*n-1)if(s[x*2-i][j]!=' ' && s[2*x-i][j]!=s[i][j])return false;
                if(y*2-j>=0 && y*2-j<2*n-1)if(s[i][y*2-j]!=' ' && s[i][y*2-j]!=s[i][j])return false;
            }
    return true;
}

int cal(int x,int y)
{
    int t = max(y,2*n-2-y);
    int tt = abs(n-x-1);
    int ans = tt+t;
    t = max(x,2*n-2-x);
    tt = abs(n-y-1);
    if(ans < tt+t)ans =tt+t;
    return ans;
}

int cc(int x)
{
    return x*(1+x)/2+(x-1)*x/2;
}

    
int  work()
{
    cin >> n;
    getline(cin,s[0]);
    int min = 0x7fffffff;
    for(int i =0;i<2*n-1;i++){
        getline(cin,s[i]);
        //  cout <<i<<' '<< s[i].size()<< endl;
        while(s[i].size()<2*n-1)s[i].push_back(' ');
        
    }
//    cout << (ok(2,3))<< endl;
    for(int i =0;i<2*n-1;i++)
        for(int j=0;j<2*n-1;j++)
            if(ok(i,j)){
                int temp = cal(i,j);
                if(min >temp)min =temp;
            }
    // cout << min+1<< endl;
    return cc(min+1)-cc(n);
}

int main()
{
    int t;
    cin >> t;
    for(int i =1;i<=t;i++)
        cout << "Case #" <<i<<": "<<work()<< endl;
    
}
