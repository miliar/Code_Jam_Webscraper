#include <iostream>
#include<vector>

using namespace std;

int main()
{
    int T,A,B,i,k,j,warunek,C;
    cin>>T;
    for(i=0;i<T;i++)
    {
        cin>>A;
        cin>>B;
        cin>>C;
        int tab[A];
        for(j=0;j<A;j++)
        {
        cin>>tab[j];
        }
        vector <int> vec;
        for(j=B;j<=C;j++)
        {
            warunek=0;
            for(k=0;k<A;k++)
            {
                if(tab[k]<j)
                {
                    if(j%tab[k]!=0) warunek=1;
                }
                else
                {
                    if(tab[k]%j!=0) warunek=1;

                }
            }
            if (warunek==0)
            {
                vec.push_back(j);
            }
        }
        if(!vec.empty()) cout<<"Case #"<<i+1<<": "<<vec[0]<<endl;
        else cout<<"Case #"<<i+1<<": NO"<<endl;
    }
    return 0;
}
