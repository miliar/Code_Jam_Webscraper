#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string>dic;
int len, D, ca;

bool match(string y, string x)
{
    //cout << x << y << endl;
    int i, j, k = x.size();
    for(i=0,j=0;i<k;i++)
    {
        if(y[j]!='(' && y[j]!=x[i]) return false;
        else if(y[j]=='('){
            j++;
            bool t = false;
            while(y[j]!=')'){
                if(y[j]==x[i]) t = true;
                j++;
            }
            if(!t) return false;
        }
        j++;
    }
    return true;
}
    
int main()
{
    
    freopen("A-large.in", "r", stdin);
    freopen("out.txt","w",stdout);
    
    cin >> len >> D >> ca;
    cin.ignore();
    int i, j, k;
    
    string t;
    for(i=1;i<=D;i++){
        cin>>t;
        cin.ignore();
        
        dic.push_back(t);
    }
    for(int cnt=1;cnt<=ca;cnt++)
    {
        cin>>t;
        cin.ignore();
        
        int ans=0;
        for(j=0;j<D;j++)
            if(match(t, dic[j])) ans++;
        cout << "Case #" << cnt <<": " << ans << endl;
    }
    cin >> D;
    return 0;
}
        
    
