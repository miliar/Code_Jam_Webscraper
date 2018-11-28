#include <iostream>
#include <string>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n;
    cin >> n;
    for(int _n=1; _n<=n; _n++)
    {
        int N, S, p;
        cin >> N >> S >> p;
        int res=0, sur=0, low=p;
        for(int i=0; i<N; i++)
        {
            int t;
            cin >> t;
            
            if(t%3 == 0)
            {
                int a = t/3;
                if(a >= p) res++; // without surprise
                else if(t >= p*3-4 && a-1>=0) sur++; // with surprise
            }
            else if((t+1)%3 == 0)
            {
                int a = (t+1)/3;
                if(a >= p) res++; // without surprise
                else if(a+1 >= p) sur ++; // with surprise
            }
            else if((t+2)%3 == 0)
            {
                int a = (t+2)/3;
                if(a >= p) res++; // without surprise
            }
            
            /*            
            if(t >= low) res++;
            else if(t >= low-2)
            {   
                if(low == 30 || 
                sur ++;
            }
            else if(t >= low-4)
            {
                /*
                if(t%3 == 0)
                {
                    int a = t/3;
                    if(a + 1 >= p) res++;
                }
                else if((t+1)%3 == 0)
                {
                    int a = (t+1)/3;
                    if(a + 1 >= p) res++;
                }
            }*/
        }
        
        if(sur > S) res += S;
        else res += sur;
        
        printf("Case #%d: %d\n", _n, res);

    }
}
