    #include<iostream>
    #include<cmath>
    using namespace std;
    
    main()
    
    {     int t,k=1;
          cin>>t;
          while(t--)
      {
                    int arr[1000],ctr=0,i,j,temp,ans,n;
          cin>>n;
          
        for(i=0;i<n;i++)
        {
                         cin>>arr[i];
                         if(arr[i]!=i+1)
                         ctr++;
                         }
         
        
              
         cout<<"Case #"<<k<<": "<<ctr<<".000000"<<endl; 
            k++;
            }
          return 0;
         }
              
          
         
   



