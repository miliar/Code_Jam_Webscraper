#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <numeric>
using namespace std;
    template <typename Iterator>
inline bool next_combination(const Iterator first, Iterator k, const Iterator last)
{
    /* Credits: Thomas Draper */
    if ((first == last) || (first == k) || (last == k))
        return false;
    Iterator itr1 = first;
    Iterator itr2 = last;
    ++itr1;
    if (last == itr1)
        return false;
    itr1 = last;
    --itr1;
    itr1 = k;
    --itr2;
    while (first != itr1)
    {
        if (*--itr1 < *itr2)
        {
            Iterator j = k;
            while (!(*itr1 < *j)) ++j;
            std::iter_swap(itr1,j);
            ++itr1;
            ++j;
            itr2 = k;
            std::rotate(itr1,j,last);
            while (last != j)
            {
                ++j;
                ++itr2;
            }
            std::rotate(k,itr2,last);
            return true;
        }
    }
    std::rotate(first,k,last);
    return false;
}
unsigned int xorf(vector<unsigned int>::iterator begin,vector<unsigned int>::iterator end){
    unsigned int ans=(*begin);
    begin++;
    while(begin!=end){
        ans^=(*begin);
        begin++;
    }
    return ans;
}
int main(){
    unsigned int t;
    cin>>t;
    for(unsigned int z=1;z<=t;z++){
        unsigned int n;
        scanf("%d",&n);
        vector<unsigned int> c;
        unsigned int tmp;
        for(unsigned int i=0;i<n;i++){
            scanf("%d",&tmp);
            c.push_back(tmp);
        }
        sort(c.begin(),c.end());
        unsigned int s=accumulate(c.begin(),c.end(),0); 
        bool flag=false;
        unsigned int ans=0;
        do{
            vector<unsigned int>::iterator it=c.begin();
            unsigned int p=(*it);
            it++;
            unsigned int t=xorf(it,c.end());
            /*if(p==t){
                flag=true;
                unsigned int sum=max(accumulate(c.begin(),it,0),accumulate(it,c.end(),0));
                if(sum>ans)
                     ans=sum;
            }*/
            for(;it!=c.end();it++){
                if(p==t){
                    flag=true;
                    unsigned int sum=max(accumulate(c.begin(),it,0),accumulate(it,c.end(),0));
                    if(sum>ans)
                        ans=sum;
                }
                p^=(*it);
                t^=(*it);
            }
        }while(next_combination(c.begin(),c.end(),c.end()));
        cout<<"Case #"<<z<<": ";
        if(flag)
            cout<<ans<<endl;
        else
            cout<<"NO"<<endl;
    }
    return 0;
}
