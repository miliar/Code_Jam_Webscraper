#include<vector>
#include<fstream>
#include<algorithm>
using namespace std;

int main(){
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("B-large.out");
    int R;
    fin>>R;
    for (int r=0;r<R;r++){
        int n,s,p;
        vector<int> a;
        fin>>n>>s>>p;
        for (int i=0;i<n;i++){
            int x;
            fin>>x;
            a.push_back(x);
        }
        sort(a.begin(),a.end());
        int ans =0;
        int i;
        for (i=n-1;i>=0 && a[i]>=((p>0)?p*3-2:0);i--) ans++;
        for (;i>=0 && s>0 && a[i]>=((p>1)?p*3-4:((p>0)?1:0));i--,s--) ans++;
        fout<<"Case #"<<r+1<<": "<<ans<<endl;
    }
    
}
