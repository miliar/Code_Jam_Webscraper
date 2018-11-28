    #include<iostream>
    #include<cmath>
    using namespace std;
    
    main()
    
    {     int t,k=1;
          cin>>t;
          while(t--)
      {
                    int arr[1000],x=0,i,sum=0,n,ans,small;
          cin>>n;
          
           for(i=0;i<n;i++)
             { cin>>arr[i];
          x=arr[i]^x;
          sum=sum+arr[i];
                         }
          small=arr[0];
          if(x!=0)
          cout<<"Case #"<<k<<": NO"<<endl;
          else
          {
              for(i=1;i<n;i++)
              {if(arr[i]<small)
              small=arr[i];
              }
              ans=sum-small;
              
         cout<<"Case #"<<k<<": "<<ans<<endl;    
         }
              
          
           k++;
 
}
    return 0;
    }
    
