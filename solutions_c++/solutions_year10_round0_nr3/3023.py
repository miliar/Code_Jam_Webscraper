#include<vector>
#include<stdio.h>
#include<iostream>
#include<fstream>
#include<bitset>
#include<algorithm>
#include<string.h>

using namespace std;

int main()
{
    int temp,sum=0,max;
    int n_test_cases,z,i,j,k,n;
    char ch;
    
    int K,N,Kmod2,R,euro,curr_pos,space_left,q[1005],ride_pos;
    
   
    
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>n_test_cases;
    cout<<n_test_cases;
    
    for(z=1;z<=n_test_cases;z++)
    {
                                fin>>R>>K>>N;
                                for(i=0;i<=N-1;i++)
                                fin>>q[i];
                                euro=0;
                                curr_pos=0;
                                for(i=1;i<=R;i++)
                                {
                                                 ride_pos=curr_pos;
                                                 space_left=K;
                                                 while(1)
                                                 {
                                                         
                                                         if(space_left<q[curr_pos])
                                                         break;
                                                         else
                                                         {
                                                             space_left=space_left-q[curr_pos];
                                                             euro=euro+q[curr_pos];
                                                             curr_pos=(curr_pos+1)%N;
                                                         }
                                                         if(curr_pos==ride_pos)
                                                         break;
                                                 }
                                                 
                                }
                                fout<<"Case #"<<z<<": "<<euro;
                                cout<<"Case #"<<z<<": "<<euro;
                                //cin>>ch;
                                fout<<endl;
                                                 
                                
    }
    fout.close();
    fin.close();
    
    
    
}
