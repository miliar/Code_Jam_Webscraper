#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>        //max heap implementation
#include <limits.h>




#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define mkp make_pair
#define fi first
#define se second
#define debug(a) { for( typeof(a.begin()) it = a.begin() ; it != a.end() ; it++ ) cout << *it << " "; cout << endl; }

using namespace std;

//class comparators for queue and others
class classcomp{
    public:
        bool operator() (const int& l, const int& r)const{
            return l<r;
        }
};

#define ll long long



int main()
{
    //char a[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    freopen("input1.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n,x,o,t,d,f;
    cin>>n;

    for(int i=0;i<n;++i)
    {   f=0;d=0;
        char a[6][6];

        for(int j=1;j<=4;++j)
        for(int k=1;k<=4;++k)
        cin>>a[j][k];

        for(int j=1;j<=4;++j)
        {   x=0;t=0;o=0;
            for(int k=1;k<=4;++k)
            {
                if(a[j][k]=='X')
                x+=1;
                if(a[j][k]=='O')
                o+=1;
                if(a[j][k]=='T')
                t+=1;
                if(a[j][k]=='.')
                d+=1;
            }
            if((x==4)||(x==3 && t==1))
            {cout<<"Case #"<<i+1<<":"<<" "<<"X won"<<endl;f=1;break;}
            if((o==4)||(o==3 && t==1))
            {cout<<"Case #"<<i+1<<":"<<" "<<"O won"<<endl;f=2;break;}
        }

        if(f==1 || f==2)continue;
        for(int j=1;j<=4;++j)
        {   x=0;t=0;o=0;
            for(int k=1;k<=4;++k)
            {
                if(a[k][j]=='X')
                x+=1;
                if(a[k][j]=='O')
                o+=1;
                if(a[k][j]=='T')
                t+=1;

            }
            if((x==4)||(x==3 && t==1))
            {cout<<"Case #"<<i+1<<":"<<" "<<"X won"<<endl;f=1;break;}
            if((o==4)||(o==3 && t==1))
            {cout<<"Case #"<<i+1<<":"<<" "<<"O won"<<endl;f=2;break;}
        }
        if(f==1 || f==2)continue;
        x=0;o=0;t=0;


        for(int j=1;j<=4;++j)
        if(a[j][j]=='X')x++;
        else if(a[j][j]=='O')o++;
        else if(a[j][j]=='T')t++;


        if((x==4)||(x==3 && t==1))
        {cout<<"Case #"<<i+1<<":"<<" "<<"X won"<<endl;f=1;}
        if((o==4)||(o==3 && t==1))
        {cout<<"Case #"<<i+1<<":"<<" "<<"O won"<<endl;f=2;}

         if(f==1 || f==2)continue;

        x=0;o=0;t=0;
        for(int j=1;j<=4;++j)
        if(a[j][4-j+1]=='X')x++;
        else if(a[j][4-j+1]=='O')o++;
        else if(a[j][4-j+1]=='T')t++;


        if((x==4)||(x==3 && t==1))
        {cout<<"Case #"<<i+1<<":"<<" "<<"X won"<<endl;f=1;}
        if((o==4)||(o==3 && t==1))
        {cout<<"Case #"<<i+1<<":"<<" "<<"O won"<<endl;f=2;}

         if(f==1 || f==2)continue;





         if(d==0){cout<<"Case #"<<i+1<<":"<<" "<<"Draw"<<endl;continue;}

         cout<<"Case #"<<i+1<<":"<<" "<<"Game has not completed"<<endl;
    }
}
