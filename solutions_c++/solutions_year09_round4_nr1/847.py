#include<iostream>
#include<vector>
#include<string>
#include<cassert>

int main()
{
    int t;
    std::cin>>t;
    int n;
    for(int cn = 1;cn<=t;cn++)
    {
        std::cin>>n;
        std::vector<int> mat(n);
        for(int i=0;i<n;i++)
        {
            std::string str;
            std::cin>>str;
            assert(str.size()==n);
            int l = 0;
            for(int i=0;i<str.size();i++)
            {
                if(str[i]=='1')l=i+1;
            }
            mat[i]=l;
     //       std::cout<<l<<"\n";
        }
        int swaps = 0;
        for(int i=0;i<n;i++)
        {
            if(mat[i]>i+1)
            {
                int j;
                for(j=i+1;j<n;j++)
                {
                    if(mat[j]<=i+1)
                        break;
                }
                for(int k=j;k>i;--k)
                {
                    std::swap(mat[k],mat[k-1]);
                    swaps++;
                }
            }
        }
        std::cout<<"Case #"<<cn<<": "<<swaps<<"\n";
    }


}
