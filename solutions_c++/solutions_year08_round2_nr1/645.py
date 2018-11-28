#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    long trees, A, B, C, D, x0, y0, M;
    int *px,*py;
    for(int i = 0; i < n; i++)
    { 
        cin>>trees;
        cin>>A;
        cin>>B; 
        cin>>C; 
        cin>>D; 
        cin>>x0; 
        cin>>y0; 
        cin>>M;
        px = new int[trees];
        py = new int[trees];
        
        px[0] = x0%3;
        py[0] = y0%3;
        int nr = 0;
        long long g,h;
        g = x0;
        h = y0;
        for(int kl = 1; kl<trees; kl++)
        {
            g = (A * g + B) % M;    
            px[kl] = g%3;
            h = (C * h + D) % M;
            py[kl] = h%3;
        }
        
        long long u,v,w,xt,yt;
        xt = yt =0;
        for(u = 0; u<trees; u++)
        {
            xt = px[u];
            yt = py[u]; 
             
            for(v = u+1; v<trees; v++)
            {
                  xt += px[v];
                  yt += py[v];  
                  
                  for(w = v+1; w<trees; w++)
                  {
                        xt += px[w];
                        yt += py[w];  
                        
                        if((xt%3==0)&&(yt%3==0))
                        {
                             nr++;
                        }
                        xt -= px[w];
                        yt -= py[w];
                        
                  }  
                  xt -= px[v];
                  yt -= py[v]; 
             }                   
        }
        cout<<"Case #"<< (i+1)<<": "<<nr<<"\n";
        delete px,py;
    }
    return 0;
}
