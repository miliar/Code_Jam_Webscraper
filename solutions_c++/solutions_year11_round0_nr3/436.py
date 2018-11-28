#include <iostream>
using namespace std;
int tn,t,n;
int sum,mini,res;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i;
    cin >> tn;
    for (t=1;t<=tn;t++)
    {
        cin >> n;
        sum=res=0;
        mini = 2147483647;
        int tmp;
        
        for (i=0;i<n;i++)
        {
            cin >> tmp;
            sum+=tmp;
            mini=min(mini,tmp);
            res=res^tmp;  
        } 
        
        cout << "Case #" << t << ": ";
        if (res!=0)
           cout << "NO" << endl;
        else    
            cout << sum-mini << endl;
    }
}
