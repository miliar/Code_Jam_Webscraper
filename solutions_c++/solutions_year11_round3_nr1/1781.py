#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<string>
#include<iomanip>
#define beginT int _T; cin>>_T; for(int _t=1;_t<=_T;_t++)
#define printT(_ans) cout<<"Case #"<<_t<<": "<<_ans<<endl
using namespace std;

int main()
{
  beginT
  {
        int r,c,b=0;
        cin>>r>>c;
        char arr[r][c];
        for(int i=0;i<r;i++)
        {
                for(int j=0;j<c;j++)
                {
                     cin>>arr[i][j];
                     if(arr[i][j]=='#')
                                     b++;
                }
        }
        printT("");
        if(b==0)
        {
                for(int i=0;i<r;i++)
                {
                        for(int j=0;j<c;j++)
                        {
                                cout<<arr[i][j];
                        }
                        cout<<endl;
                }
        }
        else if((b%4)!=0)
        {
                cout<<"Impossible"<<endl;
        }
        else
        {
            bool v[r][c];
            for(int i=0;i<r;i++)
                    for(int j=0;j<c;j++)
                            v[i][j]=0;
            for(int i=0;i<r;i++)
            {
                    for(int j=0;j<c;j++)
                    {
                            if(v[i][j]==1) continue;
                            if(arr[i][j]=='#' && arr[i+1][j]=='#' &&
arr[i][j+1]=='#' && arr[i+1][j+1]=='#')
                            {
                                            arr[i][j]=arr[i+1][j+1]='/';
                                            arr[i+1][j]=arr[i][j+1]='\\';

v[i][j]=v[i+1][j]=v[i][j+1]=v[i+1][j+1]=1;
                                            b-=4;
                            }
                    }
            }
            if(b!=0)
                    cout<<"Impossible"<<endl;
            else
            {
                for(int i=0;i<r;i++)
                {
                        for(int j=0;j<c;j++)
                        {
                                cout<<arr[i][j];
                        }
                        cout<<endl;
                }
            }
        }
  }
  return 0;
}
