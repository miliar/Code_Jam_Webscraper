    #include<iostream>
    #include<stdio.h>
    #include<algorithm>
    #include<vector>
    using namespace std;
    
    int main()
    {
        int x;
        scanf("%d",&x);
        int t=1;
        while(t<=x){
           int n,s,p;
           scanf("%d%d%d",&n,&s,&p);
           int i;
           int arr[n];
           for(i=0;i<n;i++)
              scanf("%d",&arr[i]);
           //vector <int> triplet(
           sort(arr,arr+n);
           int min_sum = 2*(p-2)+p;
           int sum = 2*(p-1)+p;
           if(p==1)
             min_sum=1;
           if(p==0){
              min_sum=0;
              sum=0;
           }
           int out=0;
           for(i=0;i<n;i++){
              if(arr[i]>=sum)
                break;
              if(arr[i]>=min_sum)
                 out++;
           }
           if(out>s)
              out=s;
           out = out + n - i;
           printf("Case #%d: %d\n",t,out);
           t++;
        }
        return 0;
    }
