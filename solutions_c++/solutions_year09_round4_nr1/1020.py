# include<iostream>
# include<vector>

using namespace std;

int main ()
{
    int test;
    int val=1;
    cin>>test;
    while (test--)
    {
         vector <int> min;
         int N;
         cin>>N;
         for (int i=0;i<N;i++)
         {
             int h=-1;
             string num;
             cin>>num;
             //cout<<num<<endl;
             for (int j=0;j<num.size();j++)
             {
                 if ((num[j]-'0')==1)
                 {
                    h=j;
                 }
             }
             //cout<<h<<endl;
             min.push_back(h);
         }
         int ans=0;
         for (int i=0;i<min.size();i++)
         {
             //cout<<"MIN"<<min[i]<<endl;
             int j=i;
             while (min[j]>i)
             {
                   j++;
             }
             //cout<<j<<endl;
             ans+=(j-i);
             int temp=min[j];
             for (int k=j;k>i;k--)
             {
                 min[k]=min[k-1];     
             }
             min[i]=temp;
            // for (int l=0;l<min.size ();l++)
                 //cout<<min[l]<<" ";
         }
         cout<<"Case #"<<val<<": "<<ans<<endl;
         val++;
    }
    return 0;
}                              
                  
