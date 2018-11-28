#include<iostream>
#include<string>
using namespace std;

bool intersects(int a1, int b1, int a2, int b2)
{
     int diffa = a1 - a2;
     int diffb = b1 - b2;
     if(diffa * diffb < 0)
         return true;
     else
         return false;
}

int main()
{
    int T,t,i,j,val,N;
    int A[1000], B[1000];
    cin>>T;
    for(t=1; t<=T; t++)
    {
        cin>>N;
        val = 0;
        for(i=0; i<N; i++)
            cin>>A[i]>>B[i];
        for(i=0; i<N-1; i++)
            for(j=i+1; j<N; j++)
                if(intersects(A[i],B[i],A[j],B[j]))
                    val++;
        
        cout<<"Case #"<<t<<": "<<val<<endl;
    }
}
