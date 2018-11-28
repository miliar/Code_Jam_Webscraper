#include <iostream>
#include <set>

using namespace std;

char arr[100]; 

int TC = 1, T, N, C,sum,bin_sum1,bin_sum2,temp_sum1,temp_sum2;

multiset<int> candy;
multiset<int>::iterator it,it2,end;

int main ()
{

    cin>>T;
    for (; TC <= T; TC++)
    {
        sum=0;
        cin>>N;
        candy.clear();
        while(N--)
        {
            cin>>C;
            candy.insert(C);
        }
        /*for ( it=candy.begin();it!= candy.end();it++)
        {
            cout<<*it<<", ";
        }
        cout<<endl;*/
        it=candy.begin();
        for ( it++;it!= candy.end();it++)
        {
            temp_sum1=0;
            temp_sum2=0;
            bin_sum1=0;
            bin_sum2=0;
            for (it2=candy.begin(); it2!=it; it2++)
            {
                bin_sum1=bin_sum1^*it2;
                temp_sum1+=*it2;
                //cout<<*it2<<" ";
            }
            //cout<<"and ";
            for (; it2!=candy.end(); it2++)
            {
                bin_sum2=bin_sum2^*it2;
                temp_sum2+=*it2;
                //cout<<*it2<<" ";
            }
            //cout<<endl<<bin_sum1<<" "<<bin_sum2<<" and "<<temp_sum1<<" "<<temp_sum2<<endl;
            if(bin_sum1==bin_sum2)
            {
                if(temp_sum1>temp_sum2)
                {
                    if(sum<temp_sum1)
                        sum=temp_sum1;
                }
                else
                {
                    if(sum<temp_sum2)
                        sum=temp_sum2;
                }
            }  
        }
        printf ("Case #%d: ", TC);
        if(sum>0)
        {
            cout<<sum<<endl;
        }
        else
        {
            cout<<"NO\n";
        }
    }
    return 0;
}
