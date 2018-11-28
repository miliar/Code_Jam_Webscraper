#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

#define pb push_back

int main() {
    long long int N,n,a,b,c,d,x,y,X,Y,m;
    ifstream fin;
    ofstream fout;
    fin.open("in.txt");
    fout.open("out.txt");
    if(!fin)
        cout<<"Unable to open";
    fin>>N;
    for(int i=1;i<=N;i++) {
        long long ret=0;
        vector <int> xs(0),ys(0);
        fin>>n>>a>>b>>c>>d>>x>>y>>m;
        X=x;
        Y=y;
        xs.pb(X);
        ys.pb(Y);
        for(int j=1; j<n;j++) {
            X=(a*X+b)%m;
            Y=(c*Y+d)%m;
            xs.pb(X);
            ys.pb(Y);
        }
  /*      for(int j=0;j<n;j++) 
            cout<<xs[j]<<","<<ys[j]<<"\n";
        system("pause");*/
            
        for(int j=0;j<n-2;j++) {
            for(int k=j+1;k<n-1;k++) {
                for(int l=k+1;l<n;l++) {
                    double cx=(xs[j]+xs[k]+xs[l])/3.0;
                    double cy=(ys[j]+ys[k]+ys[l])/3.0;
//                    cout<<j<<"   "<<cx<<"  "<<cy<<"\n";
                    if(cx==int(cx) && cy==int(cy))
                        ret++;
                }
            }
        }
//        system("pause");
        fout<<"Case #"<<i<<": "<<ret<<"\n";
    }    
}
