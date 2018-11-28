#include<iostream>
#include<math.h>
using namespace std;
int main()
{
   freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\A-small-attempt4.in","r", stdin);
    freopen("C:\\Documents and Settings\\All Users\\×ÀÃæ\\out.txt","w", stdout);
    int T;
    cin>>T;
    int i;
    for(i=0;i<T;i++)
    {      
        int n,pd,pg;
        cin>>n>>pd>>pg;
        cout << "Case #"<<i+1<<": ";
        if(pg==0&&pd!=0)
        {
             cout << "Broken" << endl;
             continue;
        }
        
        if(pg==100&&pd!=100)
        {
             cout << "Broken" << endl;
             continue;
             }
        if(pd == 0)
        {
             cout << "Possible" << endl;
             continue;
             }
        int j,sum2=0,sum5=0;
        int tmp = pd;
        while(tmp%2==0)
        {
            sum2++;
            tmp >>= 1;
        }
        tmp = pd;
        while(tmp%5==0)
        {
            sum5++;
            tmp/=5;
        }
        if(sum2>2) sum2 = 2;
        if(sum5>2) sum5 = 2;
        tmp = (int)pow(2,2-sum2)*(int)pow(5,2-sum5);
        if(tmp <= n)
           cout << "Possible" << endl;
        else
           cout << "Broken" << endl;
    }
   //system("pause");
    return 0;
}
