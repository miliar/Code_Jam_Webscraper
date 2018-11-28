#include<iostream>
using namespace std;
int main()
{
  //  cout << (double)5/2<<endl;
  freopen("C:\\Users\\Administrator\\Desktop\\B-small-attempt0.in","r",stdin);
  freopen("C:\\Users\\Administrator\\Desktop\\out","w",stdout);
    int T,i,n;
    cin>>T;
    for(i=0;i<T;i++)
    {
        int C,D;
        cin>>C>>D;
        int j;
        double v[101];
        int k=0;
        int pos,num;
        for(j=0;j<C;j++)
        {
            cin>>pos>>num;
            while(num--)
               v[k++] = pos;
        }
    //    cout << k<< endl;
   //     for(j=0;j<k;j++)
    //      cout << v[j] << endl;
        num = k;
        double time = 0;
        for(j=1;j<num;j++)
        {
            if(v[j]-v[j-1]>=D)
            {
                 if(time>=v[j]-v[j-1]-D)
                   v[j] = v[j-1]+D;
                 else
                   v[j] = v[j]-time;
            }
            else
            {
                  double tmp = v[j-1]+D-v[j];
                  if(time>=tmp)
                  {
                      v[j] = v[j-1]+D;
                      continue;
                  }
                  tmp -= time;
                  for(k=0;k<j;k++)
                     v[k] = v[k]-(tmp/2);
                  time += tmp/2;
                  v[j] = v[j-1]+D;
            }
        }
        cout <<"Case #"<<i+1<<": "<<time<<endl;
    }
  //  system("pause");
    return 0;
} 
