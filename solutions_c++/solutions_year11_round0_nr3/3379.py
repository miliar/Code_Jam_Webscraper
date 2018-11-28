#include <iostream>
#include <fstream>

using namespace std;

int main ()
{
    ifstream in;
    in.open("input.in");
    ofstream out;
    out.open("output.out");
    int T = 0;
    int N = 0;
    unsigned long long int *arr;
    
    //program
    in>>T;//cout<<"test"<<T<<endl;
    for (int j=0; j<T; j++)
    {
        in>>N;//cout<<"elements"<<N<<endl;
        arr = new unsigned long long int[N];
        for(int i=0; i<N; i++)
        {
                in>>arr[i];//cout<<arr[i]<<" ";
        }//cout<<endl;
        //sort
        unsigned long long int min(99999999),index(0);
        for(int i=0; i<N; i++)
        {
                min = arr[i];
                index = i;
                for(int i1=i+1; i1<N; i1++)
                        if (min > arr[i1]) {index = i1; min = arr[i1];}
                if (index != i) {arr[i] = arr[i] + arr[index];
                              arr[index] = arr[i] - arr[index];
                              arr[i] = arr[i] - arr[index];}
        }
                        
        
        //process
        //if (check != 0) {out<<"Case #"<<(j+1)<<": "<<"NO"<<endl; }//cout<<"Case #"<<(j+1)<<": "<<"NO"<<endl;}
        //else
        {
            unsigned long long int a(0), b(0);
            /*int separator = N/2;
            do
            {
                if (a<b) separator++; else if (a>b) separator--;
                  //First Half
                  for(int i=0; i<separator; i++)
                          a ^= arr[i];
                  for(int i=separator; i<N; i++)
                          b ^= arr[i];
            }while (a!=b);*/
            int separator = 0;
            unsigned long long int max = 0;
            //if (j==50) system("pause");
            while (separator<N-1)
            {
                  a=0;
                  b=0;
                  do
                  {
                      a=b=0;
                      separator++;
                        //if (a<b) separator++; else if (a>b) separator--;
                        //First Half
                        for(int i=0; i<separator; i++){
                                a ^= arr[i]; }//cout<<"A"<<arr[i]<<" ";cout<<endl;}
                        for(int i=separator; i<N; i++){
                                b ^= arr[i]; }//cout<<"B"<<arr[i]<<" ";cout<<endl;}
                        //if (j==50) cout<<a<<" - "<<b<<" - "<<separator<<" - "<<max<<endl;
                  }while( (a!=b) && (separator<N) );
                  
                  if ( (a==b) && (separator != 0) && (separator < N) )
                  {//cout<<"HERE"<<endl;
                       a=0;
                       b=0;
                       for(int i=0; i<separator; i++)
                               a += arr[i];
                       for(int i=separator; i<N; i++)
                               b += arr[i];
                       //if (j==50) cout<<"HERE"<<a<<" - "<<b<<" - "<<separator<<" - "<<max<<endl;
                       if ( max < ((a<b)?b:a) ) max = ((a<b)?b:a);
                  }
            }
            if (max==0) out<<"Case #"<<(j+1)<<": "<<"NO"<<endl;
            else
            out<<"Case #"<<(j+1)<<": "<<max<<endl;
            /*if (j==50){
            cout<<"Case #"<<(j+1)<<": "<<max<<" "<<N<<endl;
            cout<<a<<" - "<<b<<" - "<<separator<<" - "<<endl;system("pause");}*/
        }
        //end
        
        delete arr;
    }
    //end
    
    in.close();
    out.close();
    //system("pause");
    return 0;
}
