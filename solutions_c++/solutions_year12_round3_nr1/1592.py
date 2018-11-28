#include <iostream>
#include <map>
#include <vector>
#include <String>
#include <algorithm>

using namespace std;

int main(){
    int t,n,k,x,s1,s2;
     vector<int>::iterator it;
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        scanf("%d",&n);
        vector<int> z;
        vector < vector <int> > m(n+1, z);
        for (int j=1;j<=n;j++){        
            scanf("%d",&k);
            for (int k2=0;k2<k;k2++){
                scanf("%d",&x);                
                m[j].push_back(x);
                }
            }
        s1=0;
        s2=0;    
        for (int j=1;j<=n&&s1==s2;j++){        
/*
            cout << j << ": ";
            for (int k2=0;k2<m[j].size();k2++){
                cout << m[j].at(k2) << " ";
                }
            cout << endl;
*/
            for (int k2=0;k2<m[j].size();k2++){
                x=m[j].at(k2);
                if (m[x].size()>0){
                    m[j].erase(m[j].begin()+k2);
                    k2--;
                    for (int k3=0;k3<m[x].size();k3++){
                        m[j].push_back(m[x].at(k3));
                        }
                    }
                }               
            s1=m[j].size();
            sort(m[j].begin(),m[j].end());
            it=unique (m[j].begin(), m[j].end());                
            m[j].resize( it - m[j].begin() ); 
            s2=m[j].size();
            }
        printf("Case #%d: ",i);
        if (s1!=s2)
           printf("Yes\n");                    
           else
               printf("No\n");                    
        }
    return 0;
    }
