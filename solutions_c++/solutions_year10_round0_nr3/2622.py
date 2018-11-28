#include  <queue>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("C-small-attempt0.in");
    ofstream fout("Theme Park.out");
    int t,r,n,k,i,j,v,m;
    fin>>t;
    for(i=0;i<t;i++){
       fout<<"Case #"<<i+1<<": ";
       queue<int> a;
       fin>>r>>k>>n;
       for(j=0;j<n;j++){
        fin>>v;
        a.push(v);
       }
       int totsum=0;
       for(m=0;m<r;m++){
           int sum=0;
            for(j=0;j<n;j++){
                int tt=a.front();
                if(tt+sum<=k){
                    a.push(tt);
                    sum+=tt;
                    a.pop();
                }
                else{
                    break;
                }
            }
            totsum+=sum;
        }
        fout<<totsum<<endl;
    }
}
