#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<set>
using namespace std;

//double PI =  3.14159265358979323846;
#define ll long long
#define VI vector<int>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >

int main() {
    int cas;
    cin>>cas;
    for (int tt=0;tt<cas;tt++) {
        //cout<<"qqq"<<t<<" . "<<cas<<endl;
        int n,m,q,w,t;
        cin>>n>>m;
        VVI a;
        for (int i=0;i<m;i++) {
            cin>>t;
            VI x = VI(n,2);
            for (int j=0;j<t;j++) {
                cin>>q>>w;q--;
                if (x[q]==2) x[q]=w;
                else if (x[q]==0||x[q]==1) {
                     if (x[q]!=w) x[q]=3;     
                }    
            }            
            a.PB(x);
        }    
        int all=1<<n;
        //cout<<"4444"<<endl;
        cout<<"Case #"<<tt+1<<": ";
        bool found=false;
        for (int i=0;i<all;i++) {
            bool ok=true;
            vector<bool> gd(m,false);
            for (int j=0;j<m;j++) {
                //cout<<"#"<<j<<" "; for (int k=0;k<n;k++) cout<<" "<<a[j][k]; cout<<endl;
                for (int k=0;k<n;k++) if (a[j][k]==3) gd[j]=true;
                for (int k=0;k<n;k++) if (a[j][k]==0||a[j][k]==1) {
                    int num = (i&(1<<k)); if (num!=0) num=1;
                    if (a[j][k]==num) gd[j]=true;
                }     
            }
            for (int j=0;j<m;j++) if (!gd[j]) ok=false;
            if (ok) {
                       found=true; 
                       int po=i;
                       for (int p=0;p<n;p++) {
                               cout<<po%2;
                               if (p!=n-1) cout<<" ";
                               po/=2;
                       } cout<<endl;
                       break;
            }    
        }
        if (!found) cout<<"IMPOSSIBLE"<<endl;
    }
}
