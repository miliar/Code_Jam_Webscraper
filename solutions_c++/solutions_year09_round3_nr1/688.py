#include <algorithm>
#include <iostream>
#include <sstream>
#include <cmath>
#include <set>
#include <string>
#include <vector>
#define  f(x,y,i) for(int i=x;i<y;i++)
using namespace std;

int main()
{
    int T,L; char c; set<char> A; istringstream leer;
    scanf("%d\n",&T); char cad[61]; int k=0,n=0; long long s;
    string st; vector<char> B; set<char>::iterator p; vector<int>::iterator it;
    f(1,T+1,x){
        leer.clear();
        gets(cad); 
        st=cad; leer.str(cad);
        B.clear();
        A.clear(); n=0; s=0; k=0;
        while(leer>>c){
            if(find(B.begin(),B.end(),c)==B.end() ) B.push_back(c);
        }
        n=B.size(); //cout<<" **"<<n<<endl;
//        f(0,n,ij) cout<<B[ij]<<" ";
        if(n==1) n=2;
        f(0,st.size(),t){
            c=st[t];
            int i;
            i=find(B.begin(),B.end(),c)-B.begin();
            if(i<2)i=1-i;
            s=s*(long long)n+(long long)(i); 
        }
        printf("Case #%d: ",x); cout<<s<<endl;    
        
    }
}
