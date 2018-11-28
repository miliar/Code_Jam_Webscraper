#include<iostream>
#include<vector>
using namespace std;

 int main()
{
    freopen("out.txt","w",stdout);
  //  freopen("in.txt", "r", stdin);
    freopen("C-large.in", "r", stdin);

    long long int T;
    cin>>T;
    
    for(long long int I=1;I<=T;I++)
    {
        long long int R,K,N;
        
        cin>>R>>K>>N;
        long long int iniK=K;
        vector<long long int> q;
        
      //  if(I==15) cout<<R<<" "<<K<<" "<<N<<endl;
        for(long long int i=0;i<N;i++)
        {
                long long int h;
                cin>>h;
           //    if(I==15) cout<<h<<' ';
                q.push_back(h);
                
        }
       // cout<<endl;
        
        vector<long long int> v(q.size(),0);
        long long int c=-1;
        long long int order=1;
        bool begin=true;
        vector<long long int> steps;
        long long int rekbo=0;
        for(long long int i=0;i<=N;i++)
        {
            if(i==N) i=0;
            
            if(begin&&v[i]){ c=i; break;}
            if(q[i]<=K && rekbo<N)
            {
            if(begin){ v[i]=order; order++;  begin = false;}
            rekbo++;
            
          
            K-=q[i];
            
            }else
            {
                 steps.push_back(iniK-K);
              //   cout<<iniK-K<<endl;
                 K=iniK;
                 begin = 1;
                 i--;
                 rekbo=0;
            
                 
            }
            
        //    for(long long int x=0;x<v.size();x++)
          //  cout<<v[x]<<" ";
            
         //   cout<<endl;
         
        }
        c = v[c]-1;
 //   if(I==15)   cout<<"C"<<c<<endl;
        vector<long long int>cycle;
        for(long long int i=c;i<steps.size();i++)
          cycle.push_back(steps[i]);
          
   //     for(long long int i=1;i<steps.size();i++)
     //     steps[i]+=steps[i-1];
          long long int pC=0;
        for(long long int i=0;i<cycle.size();i++)
        {
      //          cout<<cycle[i]<<endl;
        pC+=cycle[i];
        }
    //    cout<<"X"<<pC<<endl;
        if(R<=steps.size()){R--; 
        long long int sum=0;
        for(long long int i=0;i<=R;i++)
        sum+=steps[i];
        cout<<"Case #"<<I<<": "<<sum<<endl; }
        
       
        else
        {
         //  if(c>0) R-= c-1;
         long long int prof=0;
         if(c>0)
          for(long long int i=0;i<c;i++) prof+= steps[i];
         
         R-=c;
      //  cout<<"P"<<prof<<endl;
         long long int D= (R/cycle.size());
         
         D*= pC;
        // cout<<"D"<<D<<endl;
         long long int moves = R%cycle.size();
        // cout<<"MOVES"<<moves<<endl;
         for(long long int i=0;i<moves;i++)
         D+=cycle[i];
         
         D+=prof;
      //   cout<<"D"<<D<<endl;
         cout<<"Case #"<<I<<": "<<D<<endl;
      //   while(R>0)
        // {
          ///    prof += cycle[R%(cycle.size())];
             // R-=cycle.size();
              //cout<<"P"<<prof<<"R"<<R<<endl;
       //  }
        //    long long int D=(R)/cycle.size();
         //   cout<<"X"<<D<<" "<<cycle.size()<<endl;
          //  D*=steps[steps.size()-1];
         
      //      cout<<"Z"<<D<<endl;
      //       if(c>0){
        //             D+= steps[ c-1 ];
                  //   R-= c-1;
          //         }
            
           
            
        //    R = (R-1) % cycle.size();
            
        //    D+= cycle[R];   
            
       //     cout<<prof<<endl;
            
        }  
        /*
        for(long long int i=0;i<steps.size();i++)
        {
                cout<<steps[i]<<" ";
        }
        
        cout<<endl<<c<<endl;*/
    }
   // system("pause");
    return 0;
    
      
}
