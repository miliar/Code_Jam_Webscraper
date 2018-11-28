#include <iostream>
#include <cstdio>
#include <list>
#include <vector>
using namespace std;
//unsigned long n,a,b,c,d,x0,y0,m;
int64_t n,a,b,c,d,x0,y0,m;
vector<int> adj[100000];
void readinput(){
    cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
    //cout << endl;
    //cout << n << " " << a << " "<< b << " "<< c << " "<< d << " "<< x0 << " "<< y0 << " "<< m << endl;
    for(int i=0;i<n;i++){
            adj[i].clear();
    }
    int x=x0,y=y0;
    //cout << x << " - " << y << endl;
    int k=0;
    adj[k].push_back(x);
    adj[k].push_back(y);
    k++;
    for(int i=1;i<=n-1;i++,k++){
            x = (a*x+b)%m;
            y = (c*y+d)%m;
            adj[k].push_back(x);
            adj[k].push_back(y);
            //cout << x << " - " << y << endl;
    }

}
void process(int num){
     /*for(int i=0;i<n;i++){
         cout << adj[i][0] << " + " << adj[i][1] << endl;   
     }*/
     int sum=0;
     for(int i1=0;i1<n;i1++){
             for(int i2=i1+1;i2<n;i2++){
                     for(int i3=i2+1;i3<n;i3++){                             
                             if((adj[i1][0]+adj[i2][0]+adj[i3][0])%3 == 0 && (adj[i1][1]+adj[i2][1]+adj[i3][1])%3 == 0){
                                           /*float m1=0,m2=0,m3=0;   
                                           //cout << (float)(adj[i1][1]-adj[i2][1])/(adj[i1][0]-adj[i2][0]) << endl;                       
                                           if((adj[i1][1]-adj[i2][1]) != 0 && (adj[i1][0]-adj[i2][0]) != 0)
                                           m1 = (float)(adj[i1][1]-adj[i2][1])/(adj[i1][0]-adj[i2][0]);
                                           if((adj[i1][1]-adj[i3][1]) != 0 && (adj[i1][0]-adj[i3][0]) != 0)
                                           m2 = (float)(adj[i1][1]-adj[i3][1])/(adj[i1][0]-adj[i3][0]);
                                           if((adj[i2][1]-adj[i3][1]) != 0 && (adj[i2][0]-adj[i3][0]) != 0)
                                           m3 = (float)(adj[i2][1]-adj[i3][1])/(adj[i2][0]-adj[i3][0]);
                                                    cout << m1 << " " << m2 << " " << m3 << endl;
                                                    cout << (adj[i1][0]+adj[i2][0]+adj[i3][0]) << " and " << (adj[i1][1]+adj[i2][1]+adj[i3][1]) << endl;
                                                    cout << i1 <<" * " << i2 << " * " << i3 << endl;
                                                     //cout << " Is "<<endl; 
                                                     if(m1 != m2 && m2 != m3 && m1 != m3)*/
                                                     sum++;
                             }
                     }        
             }        
     }   
     cout << "Case #" << num << ": " << sum << endl;
}
int main(){
    int k;
    cin >> k;
    for(int i=1;i<=k;i++){
            readinput();
            //cout << "=========="<<endl;
            process(i);
    }
    return 0;    
}
