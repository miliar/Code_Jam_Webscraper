#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main()
{
    int t,n;
    cin >> t;
    string s;
    
    for(int i=1; i<=t; i++) {
        cin >> n;
        vector<string> v;
        vector<vector<int> > op(n);
        vector<double> wp(n);
        vector<double> owp(n);
        vector<double> oowp(n);
        
        for(int j=0; j<n; j++) {
            cin >> s;
            v.push_back(s);
            for(int k=0; k<n; k++) {
                if(s[k]=='1' || s[k]=='0') {
                    op[j].push_back(k);
                }
            }
        }                
        
        for(int j=0; j<n; j++) {
            double ctr=0;
            for(int k=0; k<n; k++) {
                if(v[j][k]=='1')                    
                    ctr=ctr+1;
            }
            ctr=ctr/op[j].size();
            wp[j]=ctr;
        }
        
        for(int j=0; j<n; j++) {
            double d=0;
            for(int k=0; k<op[j].size(); k++) {
                string ss=v[op[j][k]];
                ss[j]='.';
                int ctr1=0,ctr2=0;
                for(int a=0; a<n; a++) {                
                    if(ss[a]=='1' || ss[a]=='0') {
                        ctr1++;
                        if(ss[a]=='1')
                            ctr2++;
                    }
                }
                d=d+((double)(ctr2)/ctr1);
            }
            d=d/op[j].size();
            owp[j]=d;
        }
                
        for(int j=0; j<n; j++) {
            double d=0;
            for(int k=0; k<op[j].size(); k++) {
                d=d+owp[op[j][k]];
            }
            d=d/op[j].size();
            oowp[j]=d;
        }    
        
        cout << "Case #" << i << ":"<<endl;
        for(int j=0; j<n; j++) {
            double r=0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j];            
            printf("%.12f\n",r);
        }        
    }
                
    return 0;
}
