#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
 using namespace std;
#define FOR(a,with,b) for(a=with;a<b;a++)

int _min(int a,int b){if(a<b)return a; return b;}
int _max(int a,int b){if(a>b)return a; return b;}

 int main()
 {
     freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
     int orange[302],blue[302],current[302];
     int n,m,i,k,v,j;
     char ch;
     cin>>n;
     k=1;
     while(n--)
     {  cin>>m;
        int ind1=0,ind2=0;
        int calc,a_opu,b_opu,x,y,seconds;
        memset(orange,0,sizeof(orange));
        memset(blue,0,sizeof(blue));
        memset(current,0,sizeof(current));
        FOR(i,0,m)
        {       cin>>ch>>v;
                if(ch=='O')
                {   current[i]=1;
                    orange[ind1]=v;
                    ind1=ind1+1;
                }
                else if(ch=='B')
                {   current[i]=2;
                    blue[ind2]=v;
                    ind2=ind2+1;
                }
        }
        a_opu=1;b_opu=1;
        x=0;y=0;seconds=0;
        FOR(i,0,m)
        {       if(current[i]==1)
                {   calc=abs(a_opu-orange[x])+1;
                    seconds+=calc;
                    a_opu=orange[x++];
                    if(y<ind2)
                          b_opu=(b_opu<blue[y])?_min(blue[y],calc+b_opu):_max(blue[y],b_opu-calc);
                }
                else if(current[i]==2)
                {       calc=abs(b_opu-blue[y])+1;
                        seconds+=calc;
                        b_opu=blue[y++];
                        if(x<ind1)
                            a_opu=(a_opu<orange[x])?_min(orange[x],a_opu+calc):_max(orange[x],a_opu-calc);
                }
        }
        cout<<"Case #"<<k<<": "<<seconds<<endl;
        k++;
     }
     return 0;
 }
