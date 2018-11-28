#include <iostream>
#include <cstring>
using namespace std;

FILE* inputstream;
FILE* outputstream;
void init()
{
	inputstream = freopen("B-small-attempt0.in", "r", stdin);
	outputstream = freopen("output.txt", "w", stdout);
}

int main ()
{
    init();
    int N, X, ans, A[100], B[100], C[100];
    float D[100];
    
    cin >>N;
    
    for (int i=0; i<N; i++)
    {
        cin >> A[i] >> B[i] >> C[i];
        ans = 0;
        X = B[i];
        for (int j=0; j<A[i]; j++)
        {
            cin >> D[j];
            if (D[j]==0&&C[i]==0){ans=ans+1;}
            if (D[j]!=0&&D[j]/3.0>=C[i]){ans=ans+1;}
            if (D[j]!=0&&D[j]/3.0<C[i]&&C[i]*3-D[j]<=2){ans=ans+1;}
            if (D[j]!=0&&D[j]/3.0<C[i]&&C[i]*3-D[j]<=4&&X>0){ans=ans+1;X=X-1;}  
        }
        cout << "Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
}
