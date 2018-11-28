#include<iostream>
using namespace std;
long long arr1[1010][1010],arr2[1010][1010],arr3[1000100];
int main()
{
    long long int t,c=1,i,j,k,n,sum,stp,ans,arr[1010],x,r;
    freopen("C://Users//abir//Desktop//Topcoder//C.in","r",stdin);
    freopen("C://Users//abir//Desktop//Topcoder//C.out","w",stdout);
    cin>>t;
    while(t--)
    {
        cin>>r>>k>>n; 
        for(i=0;i<n;i++)
        {
            cin>>arr[i];
        }    
        for(i=0;i<n;i++)
        for(j=0;j<n;j++)arr2[i][j]=-1;
        i=0;
        j=0;
        stp=1;
        ans=0;
        arr3[0]=0;
        while(1)
        {
            
            int co=0;
            sum=0;
            while(sum+arr[j]<=k)
            {
                if(i==j&&co>0)break;
                sum+=arr[j];
                j=(j+1)%n;
                co++;
            }    
            if(arr2[i][j]!=-1)
            {
    //            cout<<i<<" "<<j<<endl;
                x=stp-arr2[i][j];
             //   cout<<arr3[stp-1]<<endl;
              //  cout<<arr3[arr2[i][j]-1]<<endl;
                //cout<<r<<" "<<stp<<" "<<x<<endl;
                //cout<<arr3[arr2[i][j]+(r-stp+1)%x]<<endl;
               // for(j=1;j<stp;j++)cout<<arr3[j]<<endl;
      //          cout<<" b4 "<<ans<<endl;
                
                ans+=(arr3[stp-1]-arr3[arr2[i][j]-1])*((r-stp+1)/x);
        //        cout<<" aft "<<ans<<endl;
                ans+=( arr3[arr2[i][j]+(r-stp+1)%x-1]-arr3[arr2[i][j]-1]);
          //      cout<<" result "<<ans<<endl;
                break;   
            }
            else
            {
                ans+=sum;
            //    cout<<i<<" "<<j<<endl;
                arr3[stp]=ans;
                //arr1[i][j]=sum;
                arr2[i][j]=stp;
                i=(j%n);
                j=i;
            }
              if(stp==r)break;
              stp++;
        }
        
        cout<<"Case #"<<c++<<": "<<ans<<endl;
        //else cout<<"Case #"<<c++<<": OFF"<<endl;
    }
    
    cin>>i;

return 0;    
}   
