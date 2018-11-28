#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
#define all(v) (v).begin(),(v).end()
using namespace std ;
long long toint(string s){istringstream is(s);long long t;is>>t;return t;}
string tos(long long t){stringstream st;st<<t;return st.str();}
int c[501][6];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    long long t;
    cin>>t;
    for(int caso=0;caso<t;caso++)
    {
        long long h;
        cin>>h;
        for(int i=0;i<h;i++)
            for(int j=0;j<6;j++)
            cin>>c[i][j];
        vector<long long>v(6);
        for(int i=0;i<6;i++)
        {   
            long long sum=0;
            for(int j=0;j<h;j++)
                sum+=c[j][i];
            v[i]=sum;
        }
        long long a,b,c,d,e,f;
        d=v[0];e=v[1];f=v[2];a=v[3];b=v[4];c=v[5];
        
        long long dev=2*(a*d+b*e+c*f);
        double tiempo=0;
        if(dev>=0)tiempo=0;
            else
                tiempo=-(a*d+b*e+c*f)/(double)(a*a+b*b+c*c);    
        double div=(double)h;
        double dis= ((a*tiempo+d)/div)*((a*tiempo+d)/div) +((b*tiempo+e)/div)*((b*tiempo+e)/div)
                                +((c*tiempo+f)/div)*((c*tiempo+f)/div);
        dis=sqrt(dis);
        cout<<"Case #"<<caso+1<<": ";
        printf("%8lf",dis);cout<<" ";printf("%8lf",tiempo);cout<<endl;
    }
    //system("pause");
    return 0;
}


