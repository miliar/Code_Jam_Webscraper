///  Mahesh
#include<iostream>
#include<cstdio>
using namespace std;
char cc[500];
int p[500], no[500], nb[500];
int main()

{
    freopen("1.txt", "r", stdin);
    freopen("jam.txt", "w", stdout);

    int t;
    cin>>t;
    for(int T=0;T<t;T++){
        int n;
        cin>>n;
        for(int i=0;i<n;i++){
            string s; char c;
            cin>>s; cc[i] =s[0];
            cin>>p[i];
        }
        no[n] = nb[n] = 0;
        for(int i=n-1;i>=0;i--){
            if (cc[i]=='O'){
                no[i] = p[i];
                nb[i] = nb[i+1];
            }
            else{
                no[i]= no[i+1];
                nb[i] = p[i];
            }
        }
        int i = 0;
        int ans = 0, x =1, y=1;
        while (i<n){
            if (cc[i]=='O'){
  //              cout<<"if \n";
                if (nb[i]!=0 && y!=nb[i]){
                    y>nb[i]?(y--):(y++);
                //    cout<<"B moved to "<<y<<", ";
                }
                if (x!=p[i]){
                    x>p[i]?(x--):(x++);
                  //  cout<<"o moved to "<<x<<endl;
                }
                else{
                    //cout<<"o took "<<p[i]<<endl;
                    i++;
                }
            }
            else{
//                cout<<"else \n";
//                if (ans==3) cout<<no[i]<<" "<<x<<endl;
                if (no[i]!=0 && x!=no[i]){
                    x>no[i]?(x--):(x++);
                   // cout<<"O moved to "<<x<<", ";
                }
                if (y!=p[i]){
                    y>p[i]?(y--):(y++);
                //    cout<<"B moved to "<<y<<endl;
                }
                else{
                  //  cout<<"B took "<<p[i]<<endl;
                    i++;
                }
            }
            ans++;
        }
        printf("Case #%d: %d\n", T+1, ans);
    }
    return 0;
}
