#include<iostream>
using namespace std;
int main()
{
  //  cout << (double)5/2<<endl;
  freopen("C:\\Users\\Administrator\\Desktop\\A-large.in","r",stdin);
  freopen("C:\\Users\\Administrator\\Desktop\\out","w",stdout);
    int T,i,n;
    cin>>T;
    for(i=0;i<T;i++)
    {
        cin>>n;
        char a[101][101];
        int j;
        int k;
        char c;
        for(j=0;j<n;j++)
        {
           for(k=0;k<n;k++)
              cin>>a[j][k];
        }
       
        double wp[101],owp[101],oowp[101];
        int pre[101][2];
        memset(pre,0,sizeof(pre));
      //  cout << n<<endl;
        for(j=0;j<n;j++)
           for(k=0;k<n;k++)
              if(a[j][k]=='1')
                 pre[j][0]++;
              else if(a[j][k]=='0')
                 pre[j][1]++;
        double all = 0;
        double sum=0;
        int cou=0;
        for(j=0;j<n;j++)
        {
            wp[j] = (double)pre[j][0]/(pre[j][0]+pre[j][1]);
            sum = 0;
            cou = 0;
            for(k=0;k<n;k++)
            {
                if(j!=k)
                {
                    if(a[j][k]=='1')
                    {
                       sum += (double)pre[k][0]/(pre[k][0]+pre[k][1]-1);
                       cou++;
                       }
                    if(a[j][k]=='0')
                    {
                                    cou++;
                       sum += (double)(pre[k][0]-1)/(pre[k][0]+pre[k][1]-1);
                       }
                  //  if(a[j][k]=='.')
                    //   sum += (double)pre[k][0]/(pre[k][0]+pre[k][1]);
                }
                
            }
            sum /= cou;
            owp[j] = sum;
            all += sum;
        }
        for(j=0;j<n;j++)
        {
            sum=0;
            cou=0;
            for(k=0;k<n;k++)
               if(a[j][k]!='.')
               {
                   sum+=owp[k];
                   cou++;
               }
            oowp[j] = sum/cou;
        }
        cout << "Case #" << i+1 << ":" << endl;
        for(j=0;j<n;j++)
          cout << 0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]<<endl;
    }
   // system("pause");
    return 0;
} 
